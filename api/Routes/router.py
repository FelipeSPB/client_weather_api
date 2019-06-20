from flask import Flask, jsonify, request

from db.db import init_db
from db.db import db_session
from models import dataModel
from models import outputModel
from methods.methods import *


def view(id,date_initial,date_end):
    checking_number_days = difference_date(date_initial,date_end)
    if checking_number_days > 7:
        return jsonify({'error_403':'method_not_allowed','cause':'The difference between the dates exceeds 7 days'})
    checking_procedures = checker(id, date_initial,date_end)
    if checking_procedures == True:
        result = dataModel.weather_table.query.filter_by(city_id=id).all()
        output_schema = outputModel.weather_schema(many=True)
        output_serialised = output_schema.dump(result).data
        index_initial = discovering_index(output_serialised,date_initial)
        index_end = discovering_index(output_serialised,date_end)
        return jsonify({'data': output_database(output_serialised, index_initial,index_end)})
    data = get_data(id)
    save_db = save_data(data,id)
    return jsonify({'data': output_after_save(data)})



