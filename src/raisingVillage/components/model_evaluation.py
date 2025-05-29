import json
import joblib
import pandas as pd
import numpy as np
from raisingVillage import logger
import mlflow
from sklearn.metrics import (
                            accuracy_score, 
                            precision_score, 
                            recall_score,
                            f1_score, 
                            roc_auc_score, 
                            confusion_matrix,
                            classification_report)
from urllib.parse import urlparse
from raisingVillage.entity.entity_config import ModelEvaluationConfig

class ModelEvaluation:
    def __init__(self, config: ModelEvaluationConfig):
        self.config = config
        
    def eval_metrics(self, actual, pred, proba=None):
        """Calculate all evaluation metrics with proper type handling"""
        # Convert predictions to binary if needed (threshold at 0.5)
        if np.issubdtype(pred.dtype, np.floating):
            pred = (pred >= 0.5).astype(int)
        
        # Ensure actual values are integers
        actual = actual.astype(int)
        
        metrics = {
            "accuracy": accuracy_score(actual, pred),
            "precision": precision_score(actual, pred, zero_division=0),
            "recall": recall_score(actual, pred, zero_division=0),
            "f1_score": f1_score(actual, pred, zero_division=0),
            "confusion_matrix": confusion_matrix(actual, pred).tolist(),
            "classification_report": classification_report(actual, pred, output_dict=True, zero_division=0)
        }
        
        if proba is not None:
            metrics["roc_auc"] = roc_auc_score(actual, proba)
        return metrics

    def log_into_mlflow(self):
        """Main method to execute full evaluation workflow"""
        try:
            # Load data and model
            test_data = pd.read_csv(str(self.config.test_data_path))
            model = joblib.load(str(self.config.model_path))
            
            # Handle target column
            target_column = "target_binary"
            if target_column not in test_data.columns:
                raise ValueError(f"Target column '{target_column}' not found in test data")
            
            # Prepare test data
            test_x = test_data.drop([target_column], axis=1)
            test_y = test_data[target_column].astype(int)  # Ensure binary target
            
            # Set MLflow tracking URI
            mlflow.set_registry_uri(self.config.mlflow_uri)
            
            with mlflow.start_run():
                # Get predictions and probabilities
                predictions = model.predict(test_x)
                probabilities = model.predict_proba(test_x)[:, 1] if hasattr(model, "predict_proba") else None
                
                # Calculate metrics
                metrics = self.eval_metrics(test_y, predictions, probabilities)
                
                # Save and log metrics
                self._save_metrics(metrics)
                params_to_log = dict(self.config.all_params) if hasattr(self.config.all_params, 'to_dict') else self.config.all_params
                mlflow.log_params(params_to_log)
                
                mlflow.log_metrics({
                    "accuracy": metrics["accuracy"],
                    "precision": metrics["precision"],
                    "recall": metrics["recall"],
                    "f1_score": metrics["f1_score"],
                })
                
                if "roc_auc" in metrics:
                    mlflow.log_metric("roc_auc", metrics["roc_auc"])
                
                # Model registry
                tracking_url_type_store = urlparse(mlflow.get_tracking_uri()).scheme
                if tracking_url_type_store != "file":
                    mlflow.sklearn.log_model(model, "model", registered_model_name="GradientBoostingModel")
                else:
                    mlflow.sklearn.log_model(model, "model")
                    
        except Exception as e:
            logger.error(f"Error during model evaluation: {str(e)}")
            raise RuntimeError(f"Model evaluation failed: {str(e)}") from e
    
    def _save_metrics(self, metrics):
        """Save metrics to JSON file"""
        try:
            self.config.root_dir.mkdir(parents=True, exist_ok=True)
            metrics_path = self.config.root_dir / "metrics.json"
            with open(metrics_path, "w") as f:
                json.dump(metrics, f, indent=4)
                
            report_path = self.config.root_dir / "classification_report.json"
            with open(report_path, "w") as f:
                json.dump(metrics["classification_report"], f, indent=4)
        except Exception as e:
            logger.error(f"Failed to save metrics: {str(e)}")
            raise