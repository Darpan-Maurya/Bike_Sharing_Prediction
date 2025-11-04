from bike_rental.config.configuration import ConfigurationManager
from bike_rental.components.training import ModelTrainer
from bike_rental import logger

STAGE_NAME="Training Stage"

class training_pipeline:
    def __init__(self):
        pass
    
    def main(self):
        config = ConfigurationManager()
        training_config = config.get_training_config()
        trainer = ModelTrainer(training_config)
        trainer.train()
        
if __name__ == '__main__':
    try:
        logger.info(f">>> stage {STAGE_NAME} started >>>")
        obj=training_pipeline()
        obj.main()
        logger.info(f"<<< stage {STAGE_NAME} completed <<<\n")
    except Exception as e:
        logger.exception(e)
        raise e
        
