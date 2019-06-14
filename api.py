from flask import Flask, jsonify
import requests as Req
from db.db import init_db
from db.db import db_session
from models.dataModel import  *
from models.outputModel import *


app = Flask(__name__)

init_db()
from methods import methods



@app.route('/<id>/<date_initial>/<date_end>', methods=["GET"])
def view(id,date_initial,date_end):
    checking_number_days = methods.difference_date(date_initial,date_end)
    if checking_number_days > 7:
        return jsonify({'Erro 403':'Método não permitido','Causa':'A data final excede 7 dias'})
    checking_procedures = methods.checker(id, date_initial)
    if checking_procedures == True:
        result = weather_table.query.filter_by(city_id=id).all()
        output_schema = weather_schema(many=True)
        output_serialised = output_schema.dump(result).data
        index_initial = methods.discovering_index(output_serialised,date_initial)
        index_end = methods.discovering_index(output_serialised,date_end)
        print('callback banco')
        return jsonify({'data': methods.output_database(output_serialised, index_initial,index_end)})
    data = methods.get_data(id)
    print(data[0]['date'])
    save_db = methods.save_data(data,id)
    print('callback normal')
    return jsonify({'data': methods.output_after_save(data)})
    
if __name__ == "__main__":
    app.run(port=3000)
