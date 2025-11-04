import pandas as pd
import pickle
import statsmodels.api as sm
from bike_rental import logger
from bike_rental.entity.config_entity import TrainingConfig

class ModelTrainer:
    def __init__(self, config:TrainingConfig):
        self.config = config

    def train(self):
        logger.info("Reading preprocessed training data...")
        train = pd.read_csv(self.config.transformed_train_path)

        # Split features and target
        X_train = train.drop("cnt", axis=1)
        y_train = train["cnt"]

        # Final selected features from VIF analysis
        selected_features = [
            'yr', 'temp', 'holiday', 'Sep', 'Light Snow', 'Mist + Cloudy',
            'spring', 'summer', 'winter', 'Jan'
        ]

        X_train_sel = X_train[selected_features]

        # Add constant for OLS
        X_train_sm = sm.add_constant(X_train_sel).astype(float)

        logger.info("Training OLS model with selected features...")
        ols_model = sm.OLS(y_train, X_train_sm).fit()

        # Save trained model + features
        model_artifact = {
            "model": ols_model,
            "features": selected_features
        }
        with open(self.config.model_path, "wb") as f:
            pickle.dump(model_artifact, f)

        logger.info(f"Model trained and saved at {self.config.model_path}")
        logger.info(ols_model.summary())

        return ols_model, selected_features
