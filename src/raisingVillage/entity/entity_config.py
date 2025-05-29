from dataclasses import dataclass
from pathlib import Path
from typing import Dict, Any
@dataclass(frozen=True)
class DataIngestionConfig:
    root_dir: Path
    source_url: str
    local_data_file: Path 
    unzip_dir: Path   
    
@dataclass(frozen=True)
class DataValidationConfig:
    root_dir: Path
    STATUS_FILE: str
    unzip_data_dir: Path 
    all_schema: dict
    
@dataclass(frozen=True)
class DataProcessingConfig:
    root_dir: Path
    unzip_data_dir: Path
    selected_data_file: Path 
    validation_report: str
    all_schema: dict
    target_column: str
    
@dataclass(frozen=True)
class DataTransformationConfig:
    root_dir: Path
    selected_data_file: Path
    processed_data_file: Path
    
@dataclass(frozen=True)
class DataSplittingConfig:
    root_dir: Path
    processed_data_file: Path
    train_set_path: Path
    test_set_path: Path
    test_size: float
    random_state: int

@dataclass(frozen=True)
class ModelTrainingConfig:
    root_dir: Path
    train_set_path: Path
    test_set_path: Path 
    model_name: str 
    tfidf_params: Dict[str, Any]  # Stores TfidfVectorizer params
    gb_params: Dict[str, Any]  # Stores GradientBoosting params       
    target_column: str
    

@dataclass(frozen=True)
class ModelEvaluationConfig:
    root_dir: Path
    test_data_path: Path 
    model_path: Path 
    all_params: dict
    metric_file_name: Path
    target_column: str
    mlflow_uri: str