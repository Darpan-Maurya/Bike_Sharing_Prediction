from bike_rental.constants import *
from bike_rental.utils.common import read_yaml, create_directories
from bike_rental.entity.config_entity import DataIngestionConfig,datapreprocessing,TrainingConfig,EvaluationConfig

class ConfigurationManager:
    def __init__(
        self,
        config_filepath = CONFIG_FILE_PATH,
        params_filepath = PARAMS_FILE_PATH):

        self.config = read_yaml(config_filepath)
        self.params = read_yaml(params_filepath)

        create_directories([self.config.artifacts_root])

    
    def get_data_ingestion_config(self) -> DataIngestionConfig:
        config = self.config.data_ingestion

        create_directories([config.root_dir])

        data_ingestion_config = DataIngestionConfig(
            root_dir=config.root_dir,
            source_URL=config.source_URL,
            local_data_file=config.local_data_file
        )

        return data_ingestion_config
    
    def get_data_preprocessing(self) ->datapreprocessing:
        
        config=self.config.data_preprocessing
        create_directories([config.root_dir])
        
        data_preprocessing_config =datapreprocessing(
            root_dir=Path(config.root_dir),
            n_features_to_select=self.params.n_features_to_select,
            data_path=Path(config.data_path),
            transformed_train_path=Path(config.transformed_train_path),
            transformed_test_path=Path(config.transformed_test_path),
            preprocessor_obj_path=Path(config.preprocessor_obj_path)      
        )
        
        return data_preprocessing_config
    
    def get_training_config(self) -> TrainingConfig:
        config = self.config.training

        # Create training artifact directory
        create_directories([config.root_dir])

        training_config = TrainingConfig(
            root_dir=Path(config.root_dir),
            transformed_train_path=Path(config.transformed_train_path),
            model_path=Path(config.model_path)
        )

        return training_config
    
    def get_evaluation_config(self) -> EvaluationConfig:
        
        config = self.config.evaluation
    
        evaluation_config= EvaluationConfig(
            root_dir=Path(config.root_dir),
            test_data_path=Path(config.test_data_path),
            model_path=Path(config.model_path),
            metrics_path=Path(config.metrics_path)
        )
        create_directories([evaluation_config.root_dir])
        
        return evaluation_config
      