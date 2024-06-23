import os
import sys
import mlflow
import mlflow.sklearn
import numpy as np
import pickle
from src.utils.utils import load_object
from urllib.parse import urlparse
from sklearn.metrics import mean_squared_error,mean_absolute_error,r2_score
from src.logger.logging import logging
from src.exception. exception import customexception

class ModelEvaluation:
    def __init__(self):
        logging.info("evaluation started")

    def eval_metrics(self,actual,pred):
        rmse = np.sqrt(mean_squared_error(actual, pred))# RMSE
        mae = mean_absolute_error(actual, pred)# MAE
        r2 = r2_score(actual, pred)# r3 value
        logging.info("evaluation metrics captured")
        return rmse, mae, r2

    def initiate_model_evaluation(self,train_array,test_array):
        try:
             X_test,y_test=(test_array[:,:-1], test_array[:,-1])

             model_path=os.path.join("artifacts","model.pkl")
             model=load_object(model_path)

             logging.info("model has register")

             tracking_url_type_store=urlparse(mlflow.get_tracking_uri()).scheme

             print(tracking_url_type_store)



             with mlflow.start_run():

                prediction=model.predict(X_test)

                (rmse,mae,r2)=self.eval_metrics(y_test,prediction)

                mlflow.log_metric("rmse", rmse)
                mlflow.log_metric("r2", r2)
                mlflow.log_metric("mae", mae)

                if tracking_url_type_store != "file":

                    mlflow.sklearn.log_model(model, "model", registered_model_name="ml_model")
                else:
                    mlflow.sklearn.log_model(model, "model")


        except Exception as e:
            raise customexception(e,sys)