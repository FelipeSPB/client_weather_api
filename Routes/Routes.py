from flask import Flask
from api import app
import requests
from methods import methods


@app.route('/', methods=["GET"])
def view():  
    return 'hello world'
