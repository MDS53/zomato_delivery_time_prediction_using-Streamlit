from sklearn.base import BaseEstimator, TransformerMixin
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder,StandardScaler
import lightgbm as lgb
from sklearn.model_selection import train_test_split
from utils import Performamce_metrics
import pandas as pd
import dill
import os
from logger import logging





class Data_distribution:
    try:
        def __init__(self,df):
            self.df =df
            self.X_train,self.X_test,self.y_train,self.y_test =train_test_split(self.df.drop(['Time_taken (min)'],axis=1),self.df[['Time_taken (min)']],test_size=0.30,random_state=45)
            self.X_train,self.X_test,self.y_train,self.y_test
            logging.info("Data distribution done successfully")
    except Exception as e:
        print(f"{e} at Data_distribution class constructor")
        logging.error(f"{e} from Data_distribution class")
    

class Pipes:
    def __init__(self,df):
        try:
            self.df =df
        
            self.X_train,self.X_test,self.y_train,self.y_test =train_test_split(self.df.drop(['Time_taken (min)'],axis=1),self.df[['Time_taken (min)']],test_size=0.30,random_state=45)
        
            self.pipeline(self.X_train,self.X_test,self.y_train,self.y_test)
            logging.info("Pipes's constructor ran successfully")
        except Exception as e:
            print(f"{e} at Pipe constructor")
            logging.error(f"{e} from Pipe class's constructor")
        


    
    
    def pipeline(self,X_train,X_test,y_train,y_test):
        try:
            self.X_train=X_train
            self.X_test=X_test
            self.y_train=y_train
            self.y_test=y_test
            print('train_test_split done...........')
            self.Encoding_tnf=ColumnTransformer(transformers=[
            ("tnf2",OneHotEncoder(drop='first',sparse_output=False,handle_unknown='ignore'),['Weather_conditions','Type_of_order','Festival','City'])
            ],remainder="passthrough")


            self.scaling_tnf=ColumnTransformer(transformers=[
                ("tnf",StandardScaler(),slice(0,18))
                ],remainder="passthrough")

            self.model=lgb.LGBMRegressor(colsample_bytree=0.9769037375988533,learning_rate=0.05854272296061775,max_depth=18,min_child_weight=0.7607736996559302,n_estimators=100,num_leaves=130,subsample=0.5434350673119992)
            
            
            
            self.pipeline_ = Pipeline([
            ('Encoding_tnf',self.Encoding_tnf),
            ('scaling_tnf',self.scaling_tnf),
            ('model',self.model)

            ])
            print('Pipeline Created....................')
            self.pipeline_.fit(self.X_train,self.y_train)

            self.y_pred_train=self.pipeline_.predict(X_train)
            self.y_pred_test=self.pipeline_.predict(X_test)
            Performamce_metrics(self.y_train,self.y_pred_train,self.y_test,self.y_pred_test)
            

            with open('transformer.pkl', 'wb') as f:
                dill.dump(self.pipeline_, f)
                print("Anything working??")
            print("All done")
            logging.info("pipeline() from Pipe class ran successfully")
        except Exception as e:
            print(f"{e} at pipeline()")
            logging.error(f"{e} at pipeline() from Pipe class ")

            
df=pd.read_csv('Semi_Cleaned_data3.csv')
df.drop([df.columns[0]],axis=1,inplace=True)
p=Pipes(df)

