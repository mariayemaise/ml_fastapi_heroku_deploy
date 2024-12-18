# -*- coding: utf-8 -*-
"""
Created on Tue Dec 10 14:06:40 2024

@author: Ajose Maria
"""

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import pickle
import json


app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],)


class model_input(BaseModel):
    
    pressure : float
    dewpoint : float
    humidity : int
    cloud : int 
    sunshine : float
    winddirection : float
    windspeed : float 
    
    
#loading the save model
with open('rain_prediction_model.pkl', 'rb') as f:
    rain_model = pickle.load(f)
    

 
@app.post('/rainfall_prediction')
def rainfall_predict(input_parameters : model_input):
    
    input_data = input_parameters.json()
    input_dictionary = json.loads(input_data)
    
    Pressure = input_dictionary['pressure']
    Dewpoint = input_dictionary['dewpoint']
    Humidity = input_dictionary['humidity']
    Cloud = input_dictionary['cloud']
    Sunshine = input_dictionary['sunshine']
    Winddirection = input_dictionary['winddirection']
    Windspeed = input_dictionary['windspeed']
    
    input_list = [ Pressure, Dewpoint, Humidity, Cloud, Sunshine, Winddirection, Windspeed]
    
    prediction = rain_model.predict([input_list])
    
    if prediction[0] == 0:
        return 'No rain expected'
    else:
        return 'Rain expected'
        
  
