import json

from flask import Flask
import logging

from db import PetStoreDB

logging.basicConfig(level=logging.INFO)
PetStoreDB.init_db()
app = Flask(__name__)


@app.route('/pets/<limit>')
@app.route('/pets/<limit>/<animal_type>')
def get_pets(limit, animal_type=None):
    return json.dumps(PetStoreDB.get_pets(int(limit), animal_type))


@app.route('/pets/<limit>')
@app.route('/pets/<limit>/<animal_type>')
def get_pets(limit, animal_type=None):
    return json.dumps(PetStoreDB.get_pets(int(limit), animal_type))
