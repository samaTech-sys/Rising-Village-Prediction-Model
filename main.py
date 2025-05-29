from raisingVillage import logger
from raisingVillage.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from raisingVillage.pipeline.stage_02_data_validation import DataValidationTrainingPipeline
from raisingVillage.pipeline.stage_03_data_processing import DataProcessingTrainingPipeline
from raisingVillage.pipeline.stage_04_data_transformation import DataTransformationTrainingPipeline
from raisingVillage.pipeline.stage_05_data_splitting import DataSplittingTrainingPipeline
from raisingVillage.pipeline.stage_06_model_training import ModelTrainingTrainingPipeline

STAGE_NAME = "Data Ingestion Stage"
try:
    logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
    obj = DataIngestionTrainingPipeline()
    obj.main()
    logger.info(f">>>>> {STAGE_NAME} completed >>>>>\n\nx=========x")
except Exception as e:
    logger.exception(e)
    
STAGE_NAME = "Data Validation Stage"
try:
    logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
    obj = DataValidationTrainingPipeline()
    obj.main()
    logger.info(f">>>>> {STAGE_NAME} completed >>>>>\n\nx=========x")
except Exception as e:
    logger.exception(e)

   
STAGE_NAME = "Data Processing Stage"
try:
    logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
    obj = DataProcessingTrainingPipeline()
    obj.main()
    logger.info(f">>>>> {STAGE_NAME} completed >>>>>\n\nx=========x")
except Exception as e:
    logger.exception(e)

STAGE_NAME = "Data Transformation Stage"
try:
    logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
    obj = DataTransformationTrainingPipeline()
    obj.main()
    logger.info(f">>>>> {STAGE_NAME} completed >>>>>\n\nx=========x")
except Exception as e:
    logger.exception(e)


STAGE_NAME = "Data Processing Stage"
try:
    logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
    obj = DataProcessingTrainingPipeline()
    obj.main()
    logger.info(f">>>>> {STAGE_NAME} completed >>>>>\n\nx=========x")
except Exception as e:
    logger.exception(e)

STAGE_NAME = "Data Splitting Stage"
try:
    logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
    obj = DataSplittingTrainingPipeline()
    obj.main()
    logger.info(f">>>>> {STAGE_NAME} completed >>>>>\n\nx=========x")
except Exception as e:
    logger.exception(e)

STAGE_NAME = "Model Training Stage"
try:
    logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
    obj = ModelTrainingTrainingPipeline()
    obj.main()
    logger.info(f">>>>> {STAGE_NAME} completed >>>>>\n\nx=========x")
except Exception as e:
    logger.exception(e)


