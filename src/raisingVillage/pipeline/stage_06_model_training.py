from raisingVillage.config.configuration import ConfigurationManager
from raisingVillage.components.model_training import ModelTrainer
from raisingVillage import logger

STAGE_NAME = "Model Training Stage"

class ModelTrainingTrainingPipeline:
    def __init__(self):
        pass
    
    def main(self):
        config = ConfigurationManager()
        model_training_config =config.get_model_training_config()
        model_training = ModelTrainer(config=model_training_config)
        model_training.train()     
        
if __name__ == '__main__':
    try:
        logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
        obj = ModelTrainingTrainingPipeline()
        obj.main()
        logger.info(f">>>>> {STAGE_NAME} completed >>>>>\n\nx=========x")
    except Exception as e:
        logger.exception(e)