import dill
import pandas as pd
import numpy as np
from logger import logging

class Predictor:
        def results(self,data):
                self.data=data
                try:
                        with open('transformer.pkl', 'rb') as f:
                                self.transformer = dill.load(f)


                        # Specified columns
                        self.columns = ['Delivery_person_ID', 'Delivery_person_Age', 'Delivery_person_Ratings',
                                'Weather_conditions', 'Road_traffic_density', 'Vehicle_condition',
                                'Type_of_order', 'Type_of_vehicle', 'multiple_deliveries', 'Festival',
                                'City', 'Distance in kms', 'Order_Day', 'Order_month', 'Order_year',
                                'Time_Orderd_Hour', 'Time_Orderd_mins', 'Time_Order_picked_Hour',
                                'Time_Order_picked_mins']

                        
                        #frequency encodings:
                        with open("dict_vals.txt", "r") as self.f:
                                self.dataa = self.f.readlines()
                        self.p={}
                        self.p=dict(self.p)
                        
                        for self.line in self.dataa:
                        # Process each line
                                self.key, self.value = self.line.strip().split(":")
                                self.p[self.key]=self.value# Remove extra spaces and split
                        #print(str(self.test['Delivery_person_ID']))
                        if self.data[0] in self.p.keys():
                                print('HOOOOOOIIIIIIIII')
                                self.data[0]=self.p[self.data[0]]
                                
                        else:
                                print('PPPPPPPPHOOOOOOIIIIIIIII')
                                self.data[0]=1 
                        
                        
                        
                        
                        # Provided dataa
                        
                        print(self.data[0])
                        # Creating the DataFrame
                        self.test = pd.DataFrame([self.data], columns=self.columns)
                        
                        
                        self.results=self.transformer.predict(self.test)
                        print(f"results : {self.results}")
                        logging.info("Prediction_Pipeline.py ran successfully")
                        return self.results
        
                except Exception as e:
                        print(f"{e} came from PredictionPipeline")
                        logging.error(f"{e} at Prediction_Pipeline.py file")
                        

data= ["DEHRES17DEL01", 36.0, 4.2, "Fog", "Jam", 2, "Snack", "motorcycle", 3.0, "No", 
                                "Metropolitian", 10.3, 12, 2, 2022, 21.0, 55.0, 22.0, 10.0]

p=Predictor()
p.results(data)
