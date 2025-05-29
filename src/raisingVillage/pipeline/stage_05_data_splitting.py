from raisingVillage.config.configuration import ConfigurationManager
from raisingVillage.components.data_splitting import DataSplitting
from raisingVillage import logger

STAGE_NAME = "Data Splitting Stage"

class DataSplittingTrainingPipeline:
    def __init__(self):
        pass
    
    def main(self):
        config = ConfigurationManager()
        data_splitting_config =config.get_data_splitting_config()
        data_splitting = DataSplitting(config=data_splitting_config)
        data_splitting.train_test_splitting()
            
if __name__ == '__main__':
    try:
        logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
        obj = DataSplittingTrainingPipeline()
        obj.main()
        logger.info(f">>>>> {STAGE_NAME} completed >>>>>\n\nx=========x")
    except Exception as e:
        logger.exception(e)