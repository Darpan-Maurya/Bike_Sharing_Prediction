import os
import pickle
import pandas as pd

class PredictionPipeline:
    def __init__(self):
        # Paths
        self.model_path = os.path.join("artifacts", "training", "model.pkl")                        
        self.preprocessor_path = os.path.join("artifacts", "data_preprocessing", "preprocessor.pkl")

        # Load preprocessor (ColumnTransformer or dict)
        with open(self.preprocessor_path, "rb") as f:
            self.preprocessor = pickle.load(f)
        
        # Load trained model
        with open(self.model_path, "rb") as f:
            self.model = pickle.load(f)

    def predict(self, input_data: dict):
        """
        input_data: dict of original features, e.g.
        {
            "yr": 1,
            "mnth": 9,
            "holiday": 0,
            "weekday": 2,
            "workingday": 1,
            "weathersit": 1,
            "temp": 0.35,
            "hum": 0.65,
            "windspeed": 0.1,
            "season": 3
        }
        """

        df = pd.DataFrame([input_data])  # single row DataFrame

        # Transform using preprocessor (encoding + scaling)
        transformed = self.preprocessor.transform(df)

        # Predict
        prediction = self.model.predict(transformed)

        return float(prediction[0])
