from flask import Flask, jsonify, request
from db.db import init_db
from db.db import db_session
from models.dataModel import  *
from models.outputModel import *


app = Flask(__name__)

init_db()
from methods import methods
from Routes import router


@app.route('/<id>/<date_initial>/<date_end>', methods=["GET"])
def display(id,date_initial,date_end):
   return router.view(id,date_initial,date_end)
    
if __name__ == "__main__":
    app.run(port=3000)
