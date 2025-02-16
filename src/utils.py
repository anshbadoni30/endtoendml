import os
import sys
import numpy as np
import pandas as pd
from src.exception import CustomException
from src.logger import logging
import dill
from sklearn.metrics import r2_score
import pickle
 
def save_object(file_path,obj):
    try:
        dir_path= os.path.dirname(file_path)

        os.makedirs(dir_path,exist_ok=True)

        with open(file_path,"wb") as file_obj:
            dill.dump(obj,file_obj)

    except Exception as e:
        raise CustomException(e,sys)
    

def evaluate_models(X_train, y_train, X_test, y_test, models):
    try:
        report = {}
        model_names = list(models.keys())  # ✅ Extract model names once
        
        for i in range(len(models)):  # ✅ Directly iterate over model indices
            model = models[model_names[i]]  # ✅ Get model instance
            model.fit(X_train, y_train)  # Train model

            # Make predictions
            y_train_pred = model.predict(X_train)
            y_test_pred = model.predict(X_test)

            trained_model_score = r2_score(y_train, y_train_pred)
            test_model_score = r2_score(y_test, y_test_pred)

            report[model_names[i]] = test_model_score  # ✅ Store model score with correct key

        return report
    
    except Exception as e:
        raise CustomException(e, sys)
    

def load_object(file_path):
    try:  
        with open(file_path,"rb") as file_obj:
            return pickle.load(file_obj)
    
    except Exception as e:
        raise CustomException(e,sys)

    