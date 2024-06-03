from sklearn.metrics import r2_score,mean_squared_error,mean_absolute_percentage_error,mean_absolute_error
import numpy as np
from logger import logging


class Performamce_metrics:
    def __init__(self,y_train,y_pred_train,y_test,y_pred_test):
       try:
            self.y_train = y_train
            self.y_pred_train = y_pred_train
            self.y_test = y_test
            self.y_pred_test = y_pred_test
            self.metrics()
            self.Errors()
            logging.info("Performance metrics Class done")
       except Exception as e:
           print(f"{e} at Performamce metrics class constructor")
           logging.error(e)
    def metrics(self):
        try:
            self.tr=r2_score(self.y_train,self.y_pred_train)
            self.te=r2_score(self.y_test,self.y_pred_test)
            print(f"R2score on training dataset{self.tr}")
            print(f"R2score on testing dataset{self.te}")
            

            # Calculate adjusted R^2
            self.adjusted_r2_score_training = 1 - ((1 - self.tr) * (45584 - 1) / (45584 - 20 - 1))
            self.adjusted_r2_score_testing = 1 - ((1 - self.te) * (45584 - 1) / (45584 - 20 - 1))
            # Print the result
            print(f"Adjusted R^2 score for Training: {self.adjusted_r2_score_training}")
            print(f"Adjusted R^2 score for Testing: {self.adjusted_r2_score_testing}")
            logging.info("Metrics() from Performance metrics class done ")
        except Exception as e:
            print(f"{e} at metrics() from Performance metrics class")
            logging.error(f"{e} at metrics() from Performance metrics class")
        
    def Errors(self):
        try:
            self.tr=r2_score(self.y_train,self.y_pred_train)
            self.te=r2_score(self.y_test,self.y_pred_test)
            print(f"MSE : {mean_squared_error(self.y_train,self.y_pred_train)}")
            print(f"RMSE : {np.sqrt(mean_squared_error(self.y_train,self.y_pred_train))}")
            print(f"MAE : {mean_absolute_error(self.y_train,self.y_pred_train)}")
            print(f"MAP : {mean_absolute_percentage_error(self.y_train,self.y_pred_train)}")
            logging.info("Errors() from Performance metrics class done")
        except Exception as e:
            print(f"{e} at Errors()")
            logging.error(f"{e} at Errors()from Performance metrics class")


