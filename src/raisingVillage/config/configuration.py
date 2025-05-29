#Importing dependencies 
from raisingVillage.constants import *
from raisingVillage.utils.common import read_yaml, create_directories
from raisingVillage.entity.entity_config import (
    DataIngestionConfig, 
    DataValidationConfig, 
    DataProcessingConfig,
    DataTransformationConfig
)

#Updating the configuration file 
class ConfigurationManager:
    def __init__(
        self, 
        config_filepath = CONFIG_FILE_PATH, 
        params_filepath = PARAMS_FILE_PATH,
        schema_filepath = SCHEMA_FILE_PATH, 
        selected_schema_filepath = SELECTED_SCHEMA_FILE_PATH):

        self.config = read_yaml(config_filepath)
        self.params = read_yaml(params_filepath)
        self.schema = read_yaml(schema_filepath)
        self.selected_schema = read_yaml(selected_schema_filepath)
        
       
        create_directories([self.config.artifacts_root])
    
    def get_data_ingestion_config(self) -> DataIngestionConfig:
        config = self.config.data_ingestion
        create_directories([config.root_dir])
        
        data_ingestion_config = DataIngestionConfig(
            root_dir=config.root_dir,
            source_url=config.source_url,
            local_data_file=config.local_data_file, 
            unzip_dir=config.unzip_dir
        )
        return data_ingestion_config
    
    def get_data_validation_config(self) -> DataValidationConfig:
        config = self.config.data_validation
        schema = self.schema.COLUMNS
        
        create_directories([config.root_dir])
        
        data_validation_config = DataValidationConfig(
            root_dir=config.root_dir,
            STATUS_FILE=config.STATUS_FILE,
            unzip_data_dir=config.unzip_data_dir, 
            all_schema=schema
        )
        return data_validation_config
    
    def get_data_processing_config(self) -> DataProcessingConfig:
        config = self.config.data_processing
        data_validation_config = self.config.data_validation
        selected_schema = self.selected_schema.COLUMNS
        
        # Get target column from schema (adjust this based on your actual schema structure)
        target_column = getattr(self.selected_schema, 'TARGET', None)
        if target_column is None:
            raise ValueError("Target column not specified in schema")
        
        create_directories([config.root_dir])
        
        data_processing_config = DataProcessingConfig(
            root_dir=config.root_dir,
            validation_report=Path(config.validation_report),
            selected_data_file=Path(config.selected_data_file),
            all_schema=selected_schema,
            unzip_data_dir=data_validation_config.unzip_data_dir,
            target_column=target_column  
        )
        return data_processing_config
    
    def get_data_transformation_config(self) -> DataTransformationConfig:
        config = self.config.data_transformation 
        
        create_directories([config.root_dir])
        
        data_transformation_config = DataTransformationConfig(
            root_dir=config.root_dir,
            data_path=config.data_path, 
            processed_data_dir=config.processed_data_dir
        )
        return data_transformation_config