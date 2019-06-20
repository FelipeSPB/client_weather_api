from flask_marshmallow import Marshmallow
from api import app
ma = Marshmallow(app)
from models import dataModel 

class weather_schema(ma.ModelSchema):
    class Meta:
        model = dataModel.weather_table

    

