from bike_rental.config.configuration import ConfigurationManager
from bike_rental.components.data_preprocessing import data_preprocessing
from bike_rental import logger

STAGE_NAME="Data Transformation/Preprocessing Stage"

class data_preprocessing_pipeline:
    def __init__(self):
        pass
    
    def main(self):
        config = ConfigurationManager()
        data_preprocessing_config = config.get_data_preprocessing()
        data_transforming = data_preprocessing(config=data_preprocessing_config)
        data_transforming.transform_data()
        
if __name__ == '__main__':
    try:
        logger.info(f">>> stage {STAGE_NAME} started >>>")
        obj=data_preprocessing_pipeline()
        obj.main()
        logger.info(f"<<< stage {STAGE_NAME} completed <<<\n")
    except Exception as e:
        logger.exception(e)
        raise e
    
