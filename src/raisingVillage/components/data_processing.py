import os 
from raisingVillage import logger
import pandas as pd 
from raisingVillage.entity.entity_config import DataProcessingConfig

class DataProcessing:
    def __init__(self, config: DataProcessingConfig):
        self.config = config
    
    def extract_and_save_features(self):
        """Load, validate, and save selected features"""
        try:
            df = pd.read_csv(self.config.unzip_data_dir)
            selected_columns = list(self.config.all_schema.keys())
            
            # Validate and select columns
            if missing := [col for col in selected_columns if col not in df.columns]:
                raise ValueError(f"Missing columns: {missing}")
            
            selected_df = df[selected_columns].copy()
            self.config.selected_data_file.parent.mkdir(parents=True, exist_ok=True)
            selected_df.to_csv(self.config.selected_data_file, index=False)
            
            # Log results
            logger.info(f"Saved {len(selected_columns)} features to {self.config.selected_data_file}")
            if hasattr(self.config, 'target_column'):
                logger.info(f"Target column: {self.config.target_column}")
            
            return selected_df
            
        except Exception as e:
            logger.error(f"Feature extraction failed: {e}")
            raise
    
    def validate_all_columns(self) -> bool:
        """Validate data against schema"""
        try:
            data = pd.read_csv(self.config.selected_data_file)
            schema_cols = set(self.config.all_schema.keys())
            data_cols = set(data.columns)
            
            validation_status = data_cols.issubset(schema_cols)
            report_content = (
                f"Validation status: {validation_status}\n"
                f"Data columns: {sorted(data_cols)}\n"
                f"Schema columns: {sorted(schema_cols)}"
            )
            
            self.config.validation_report.parent.mkdir(exist_ok=True, parents=True)
            self.config.validation_report.write_text(report_content)
            
            logger.info(f"Validation {'passed' if validation_status else 'failed'}")
            return validation_status
            
        except Exception as e:
            logger.error(f"Validation failed: {e}")
            raise