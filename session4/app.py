import json

from flask import Flask
import logging

from db import PetStoreDB

logging.basicConfig(level=logging.INFO)
app = Flask(__name__)


@app.route('/pets/<limit>')
@app.route('/pets/<limit>/<animal_type>')
def get_pets(limit, animal_type=None):
    return json.dumps(PetStoreDB.get_pets(int(limit), animal_type))


if __name__ == '__main__':
    PetStoreDB.init_db()
    app.run(port=8080)
