from dataclasses import dataclass
from pathlib import Path

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