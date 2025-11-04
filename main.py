from bike_rental import logger
from bike_rental.pipeline.stage_1_data_ingestion import data_ingestion_training_pipeline
from bike_rental.pipeline.stage_2_data_preprocessing import data_preprocessing_pipeline
from bike_rental.pipeline.stage_3_training_pipeline import training_pipeline
from bike_rental.pipeline.stage_4_evaluation_pipeline import evaluation_pipeline

STAGE_NAME="Data Ingestion Stage"
try:
        logger.info(f">>> stage {STAGE_NAME} started >>>")
        obj=data_ingestion_training_pipeline()
        obj.main()
        logger.info(f"<<< stage {STAGE_NAME} completed <<<\n")
except Exception as e:
        logger.exception(e)
        raise e

STAGE_NAME="Data Transformation/Preprocessing Stage"
try:
        logger.info(f">>> stage {STAGE_NAME} started >>>")
        obj=data_preprocessing_pipeline()
        obj.main()
        logger.info(f"<<< stage {STAGE_NAME} completed <<<\n")
except Exception as e:
        logger.exception(e)
        raise e

STAGE_NAME="Training Stage"
try:
        logger.info(f">>> stage {STAGE_NAME} started >>>")
        obj=training_pipeline()
        obj.main()
        logger.info(f"<<< stage {STAGE_NAME} completed <<<\n")
except Exception as e:
        logger.exception(e)
        raise e

STAGE_NAME="Evaluation Stage"
try:
        logger.info(f">>> stage {STAGE_NAME} started >>>")
        obj=evaluation_pipeline()
        obj.main()
        logger.info(f"<<< stage {STAGE_NAME} completed <<<\n")
except Exception as e:
        logger.exception(e)
        raise e






