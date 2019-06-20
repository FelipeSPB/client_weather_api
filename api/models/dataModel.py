from sqlalchemy import Column, Integer, String, Float
from db.db import Base

class weather_table(Base):
    __tablename__ = 'rawData'
    id_table = Column('id_Raw',Integer, primary_key = True)
    city_id = Column(String)
    sample_date = Column(String)
    max_temperature = Column(Float)
    min_temperature = Column(Float)
    rain_probability = Column(Float)
    rain_precipitation = Column(String)

    
    def __init__(self,city_id,sample_date, max_temperature, min_temperature, rain_probability, rain_precipitation):
        self.city_id = city_id
        self.sample_date = sample_date
        self.max_temperature = max_temperature
        self.min_temperature = min_temperature
        self.rain_probability = rain_probability
        self.rain_precipitation = rain_precipitation

    def __repr__(self):
        return '%r %r %r %r %r %r' % (self.city_id,self.sample_date, self.max_temperature, self.min_temperature, self.rain_probability, self.rain_precipitation)
