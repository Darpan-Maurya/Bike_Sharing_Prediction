from dataclasses import dataclass
from pathlib import Path


@dataclass(frozen=True)
class DataIngestionConfig:
    root_dir: Path
    source_URL: str
    local_data_file: Path
    
@dataclass(frozen=True)
class datapreprocessing:
    root_dir: Path
    n_features_to_select: int
    data_path: Path
    transformed_train_path: Path
    transformed_test_path: Path
    preprocessor_obj_path: Path
    test_size: float = 0.3
    random_state: int = 100

@dataclass(frozen=True)
class TrainingConfig:
    root_dir: Path
    transformed_train_path: Path
    model_path: Path

@dataclass(frozen=True)
class EvaluationConfig:
    root_dir: Path
    test_data_path: Path
    model_path: Path
    metrics_path: Path


