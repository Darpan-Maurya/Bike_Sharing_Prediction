from bike_rental.config.configuration import ConfigurationManager
from bike_rental.components.data_ingestion import DataIngestion
from bike_rental import logger
 
STAGE_NAME="Data Ingestion Stage"

class data_ingestion_training_pipeline:
    def __init__(self):
        pass
    def main(self):
        config = ConfigurationManager()
        data_ingestion_config = config.get_data_ingestion_config()
        data_ingestion = DataIngestion(config=data_ingestion_config)
        data_ingestion.download_file()
        
if __name__ == '__main__':
    try:
        logger.info(f">>> stage {STAGE_NAME} started >>>")
        obj=data_ingestion_training_pipeline()
        obj.main()
        logger.info(f"<<< stage {STAGE_NAME} completed <<<\n")
    except Exception as e:
        logger.exception(e)
        raise e