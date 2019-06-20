from datetime import datetime
import requests as require
from flask import jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from db.db import db_session 
from models.dataModel import weather_table
from models.token import *


def get_id_city(city_name="São Paulo"):
    url_request = "http://apiadvisor.climatempo.com.br/api/v1/locale/city?name="+cityName+"&token="+str(token)
    response = require.api.get(url_request).json()
    return response[0]['id']

def difference_date(dateStart, dateEnd):
    date_param2 = datetime.strptime(dateEnd,'%Y-%m-%d')        
    date_param1 = datetime.strptime(dateStart,'%Y-%m-%d')
    days = abs((date_param2 - date_param1).days)
    return int(days)
  
def get_data(id):
<<<<<<< HEAD:api/methods/methods.py
    url_request = "http://apiadvisor.climatempo.com.br/api/v1/forecast/locale/"+str(id)+"/days/15?token="+str(token)
=======
    url_request = "http://apiadvisor.climatempo.com.br/api/v1/forecast/locale/"+str(id)+"/days/15?token=Put_your_token"
>>>>>>> 4204b09a948e8178e6be4d3f8773e632916ac19f:methods/methods.py
    responseJson = require.api.get(url_request).json()
    return responseJson['data']

def save_data(response,id,days = 7):  
    for i in range(0,days):
        value_sample_date = response[i]['date']
        value_max_temperature = response[i]['temperature']['max']
        value_min_temperature = response[i]['temperature']['min']
        value_rain_probability = response[i]['rain']['probability']
        value_rain_precipitation = response[i]['rain']['precipitation']
        data_commit =  weather_table(city_id= id,
        sample_date = value_sample_date,
        max_temperature= value_max_temperature, 
        min_temperature= value_min_temperature,
        rain_probability= value_rain_probability,
        rain_precipitation= value_rain_precipitation)
        db_session.add(data_commit)
        db_session.commit()
        

def discovering_index(data, date):
    for i in range(0,len(data)):
        if data[i]['sample_date'] == date:
            return int(i)

def checker(id, date_initial,date_end):
    checking_id_city = weather_table.query.filter_by(city_id = id).first()
    checking_date_initial = weather_table.query.filter_by(sample_date = date_initial).first()
    checking_date_end = weather_table.query.filter_by(sample_date = date_end).first()
    if checking_id_city == None:
        return False
    if checking_date_initial == None:
        return False
    if checking_date_end == None:
        return False
    return True

def output_database(data,index_initial,index_final):
    value_sample_date = []
    value_max_temperature = []
    value_min_temperature = []
    value_rain_probability = []
    value_rain_precipitation = []

    
    for i in range(index_initial,index_final):
        value_sample_date.append(data[i]['sample_date'])
        value_max_temperature.append(data[i]['max_temperature'])
        value_min_temperature.append(data[i]['min_temperature'])
        value_rain_probability.append(data[i]['rain_probability'])
        value_rain_precipitation.append(data[i]['rain_precipitation'])
    
    
    def output_a(value_max_temperature,value_sample_date):
        output_max_data= max(value_max_temperature) 
        index_max = value_max_temperature.index(output_max_data)
        output = {"date": value_sample_date[index_max], "highest_temperature": output_max_data} 
        return output

    def output_b(value_min_temperature,value_sample_date):
        output_min_data= min(value_min_temperature) 
        index_min = value_min_temperature.index(output_min_data)
        output = {"date": value_sample_date[index_min], "lowest_temperature": output_min_data} 
        return output

    def output_c(value_rain_probability,value_rain_precipitation,value_sample_date):
        output_rain_max= max(value_rain_probability) 
        index_rain_max = value_rain_probability.index(output_rain_max)
        output = {"Date": value_sample_date[index_rain_max], "highest_rain_probability": output_rain_max, "rain_precipitation": value_rain_precipitation[index_rain_max]} 
        return output
    return {'output_a': output_a(value_max_temperature,value_sample_date),
            'output_b': output_b(value_min_temperature,value_sample_date), 
            'output_c': output_c(value_rain_probability,value_rain_precipitation,value_sample_date)}

def output_after_save(response, days = 7):
    value_sample_date = []
    value_max_temperature = []
    value_min_temperature = []
    value_rain_probability = []
    value_rain_precipitation = []
    
    for i in range(0,days):
        value_sample_date.append(response[i]['date'])
        value_max_temperature.append(response[i]['temperature']['max'])
        value_min_temperature.append(response[i]['temperature']['min'])
        value_rain_probability.append(response[i]['rain']['probability'])
        value_rain_precipitation.append(response[i]['rain']['precipitation'])
    
    def output_a(value_max_temperature,value_sample_date):
        output_max_data= max(value_max_temperature) 
        index_max = value_max_temperature.index(output_max_data)
        output = {"date": value_sample_date[index_max], "highest_temperature": output_max_data} 
        return output

    def output_b(value_min_temperature,value_sample_date):
        output_min_data= min(value_min_temperature) 
        index_min = value_min_temperature.index(output_min_data)
        output = {"date": value_sample_date[index_min], "lowest_temperature": output_min_data} 
        return output

    def output_c(value_rain_probability,value_rain_precipitation,value_sample_date):
        output_rain_max= max(value_rain_probability) 
        index_rain_max = value_rain_probability.index(output_rain_max)
        output = {"Date": value_sample_date[index_rain_max], "highest_rain_probability": output_rain_max, "rain_precipitation": value_rain_precipitation[index_rain_max]} 
        return output
    return {'output_a': output_a(value_max_temperature,value_sample_date),
            'output_b': output_b(value_min_temperature,value_sample_date), 
            'output_c': output_c(value_rain_probability,value_rain_precipitation,value_sample_date)}
