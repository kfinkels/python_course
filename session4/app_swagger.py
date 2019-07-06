#!/usr/bin/env python3
import connexion
import logging

from db import PetStoreDB


logging.basicConfig(level=logging.INFO)
app = connexion.App(__name__)
app.add_api('swagger.yaml')
# set the WSGI application callable to allow using uWSGI:
# uwsgi --http :8080 -w app
application = app.app


def get_pets(limit, animal_type=None):
    return PetStoreDB.get_pets(limit, animal_type)


if __name__ == '__main__':
    PetStoreDB.init_db()
    # run our standalone gevent server
    app.run(port=8080, server='gevent')
