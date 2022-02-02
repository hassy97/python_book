from time import timezone
from unicodedata import name
from fastapi import FastAPI
'''to create a new city first create a model in my app'''
from pydantic import BaseModel  
import requests

hassy_db  = []
app = FastAPI()     #creating an object same as i did 

class City(BaseModel):
    name: str   ## object type
    timezone:str

@app.get('/')
def index():
    return {'key' : 'value'}

# Gettign the data of cities from the db 
@app.get('/cities')
def get_cities():
    results = []  # store the results 
    for city in hassy_db:
        r = requests.get(f'http://worldtimeapi.org/api/timezone/{city["timezone"]}')
        current_time = r.json()['datetime']
        results.append({'name': city['name'],'timezone':city['timezone'], 'current_time':current_time })
    return results


@app.get('/cities/{city_id}')
def get_cities(city_id:int):
    return hassy_db[city_id -1 ]

# # create the cities 
@app.post('/cities')
def create_city(city:City):
    hassy_db.append(city.dict())
    return hassy_db[-1]


@app.delete('/cities/{city_id}')
def delete_cities(city_id:int):
    hassy_db.pop(city_id-1)
    return {}