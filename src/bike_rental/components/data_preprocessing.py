from bike_rental import logger
from bike_rental.entity.config_entity import datapreprocessing
import pickle
import os
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler

class data_preprocessing:
    def __init__(self,config: datapreprocessing):
        self.config=config
    
    def transform_data(self):
        logger.info("Reading dataset for preprocessing...")
        df = pd.read_csv(self.config.data_path)

        # --- your mapping + dummy code ---
        df['season'] = df.season.map({1:'spring',2:'summer',3:'fall',4:'winter'})
        df['mnth'] = df.mnth.map({1:'Jan',2:'Feb',3:'Mar',4:'Apr',5:'May',6:'June',
                                  7:'July',8:'Aug',9:'Sep',10:'Oct',11:'Nov',12:'Dec'})
        df['weathersit'] = df.weathersit.map({1:'Clear',2:'Mist + Cloudy',3:'Light Snow',4:'Snow + Fog'})
        df['weekday'] = df.weekday.map({0:'Sun',1:'Mon',2:'Tue',3:'Wed',4:'Thu',5:'Fri',6:'Sat'})

        df = df.drop(['atemp','instant','dteday','casual','registered'], axis=1)

        month = pd.get_dummies(df.mnth, drop_first=True)
        weekday = pd.get_dummies(df.weekday, drop_first=True)
        weathersit = pd.get_dummies(df.weathersit, drop_first=True)
        season = pd.get_dummies(df.season, drop_first=True)

        df = pd.concat([df, month, weekday, weathersit, season], axis=1)
        df.drop(['season','mnth','weekday','weathersit'], axis=1, inplace=True)
        
        scaler = MinMaxScaler()
        scaler_var = ['hum', 'windspeed', 'temp', 'cnt']
        df[scaler_var] = scaler.fit_transform(df[scaler_var])
        
        # --- Split ---
        train, test = train_test_split(df, test_size=0.3, random_state=100)
        train.to_csv(self.config.transformed_train_path, index=False)
        test.to_csv(self.config.transformed_test_path, index=False)

        # --- Save preprocessor object (optional placeholder now) ---
        preprocessor = {
            "scaler": scaler,
            "columns": df.drop("cnt", axis=1).columns.tolist()
        }
        with open(self.config.preprocessor_obj_path, "wb") as f:
            pickle.dump(preprocessor, f)

        logger.info(f"Preprocessing complete. Train & test saved at {self.config.root_dir}")