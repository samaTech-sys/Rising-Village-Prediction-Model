from raisingVillage.config.configuration import ConfigurationManager
from raisingVillage.components.data_processing import DataProcessing
from raisingVillage import logger

STAGE_NAME = "Data Processing Stage"

class DataProcessingTrainingPipeline:
    def __init__(self):
        pass
    
    def main(self):
        config = ConfigurationManager()
        data_processing_config = config.get_data_processing_config()
        data_processing = DataProcessing(config=data_processing_config)
        data_processing.extract_and_save_features()
        data_processing.validate_all_columns()
        
if __name__ == '__main__':
    try:
        logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
        obj = DataProcessingTrainingPipeline()
        obj.main()
        logger.info(f">>>>> {STAGE_NAME} completed >>>>>\n\nx=========x")
    except Exception as e:
        logger.exception(e)