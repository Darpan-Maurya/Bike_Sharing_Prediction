from bike_rental.config.configuration import ConfigurationManager
from bike_rental.components.evaluation import Evaluation
from bike_rental import logger

STAGE_NAME="Evaluation Stage"

class evaluation_pipeline:
    def __init__(self):
        pass
    def main(self):
        config = ConfigurationManager()
        eval_config = config.get_evaluation_config()
        evaluation = Evaluation(config=eval_config)
        results = evaluation.evaluate()
        
if __name__ == '__main__':
    try:
        logger.info(f">>> stage {STAGE_NAME} started >>>")
        obj=evaluation_pipeline()
        obj.main()
        logger.info(f"<<< stage {STAGE_NAME} completed <<<\n")
    except Exception as e:
        logger.exception(e)
        raise e
    

