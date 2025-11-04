import pickle
import os
import pandas as pd
import statsmodels.api as sm
import matplotlib.pyplot as plt
from bike_rental import logger
import json
from sklearn.metrics import r2_score, mean_squared_error, mean_absolute_error
from bike_rental.entity.config_entity import EvaluationConfig

class Evaluation:
    def __init__(self, config: EvaluationConfig):
        self.config = config

    def evaluate(self):
        # Load model
        with open(self.config.model_path, "rb") as f:
            model_artifact = pickle.load(f)

        ols_model = model_artifact["model"]
        selected_features = model_artifact["features"]

        # Load test data
        df_test = pd.read_csv(self.config.test_data_path)

        y_test = df_test.pop("cnt")
        X_test = df_test[selected_features]

        # Add constant
        import statsmodels.api as sm
        X_test_const = sm.add_constant(X_test)

        # Predictions
        y_pred = ols_model.predict(X_test_const)

        # Metrics
        r2 = r2_score(y_test, y_pred)
        mse = mean_squared_error(y_test, y_pred)
        mae = mean_absolute_error(y_test, y_pred)

        
        
        results = {
            "r2_score": r2,
            "mse": mse,
            "mae": mae
        }
        
        # --- Visualization ---
        plt.scatter(y_test, y_pred, alpha=0.5)
        plt.xlabel("y_test")
        plt.ylabel("y_pred")
        plt.title("y_test vs y_pred")
        plt.show()
        
        # Save results
        with open(self.config.metrics_path, "w") as f:
            json.dump(results, f, indent=4)

        logger.info(f"Evaluation complete. Metrics stored at {self.config.metrics_path}")
        return results

    
