# evaluate model

import os
import sys

import numpy as np 
import pandas as pd
import pickle
from sklearn.metrics import r2_score
from sklearn.model_selection import GridSearchCV

from src.exception import CustomException

# Function to Create pickle files at 'Artifact' location
def save_object(file_path, obj):
    try:
        dir_path = os.path.dirname(file_path)

        os.makedirs(dir_path, exist_ok=True)

        with open(file_path, "wb") as file_obj:
            pickle.dump(obj, file_obj)

    except Exception as e:
        raise CustomException(e, sys)
    
# Function to train and evaluate ML model
def evaluate_model(X_train, y_train, X_test, y_test, models, param):
    try:
        report = {}

        for i in range(len(list(models))):
            #1) Extract 'model_object' and 'parameters'
            model = list(models.values())[i] # model = model_object
            para=param[list(models.keys())[i]] #para = model_parameters

            #2) Identify the best parameters 
            gs = GridSearchCV(model,para,cv=3)
            gs.fit(X_train,y_train)

            #3) Extract the best Param from above steps and retrain the model with best params
            model.set_params(**gs.best_params_)
            model.fit(X_train,y_train) #Train model

            #4) Test on 'train' + 'test' data
            y_train_pred = model.predict(X_train)
            y_test_pred = model.predict(X_test)

            #5) r2_scor
            train_model_score = r2_score(y_train, y_train_pred)
            test_model_score = r2_score(y_test, y_test_pred)

            # 6) report = {'model_name' : 'r2_score'}
            report[list(models.keys())[i]] = test_model_score
        return report


    except Exception as e:
        raise CustomException(e, sys)
    

# Function to load Pickle files
def load_object(file_path):
    try:
        with open(file_path, "rb") as file_obj:
            return pickle.load(file_obj)

    except Exception as e:
        raise CustomException(e, sys)