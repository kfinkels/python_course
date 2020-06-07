import json
import random
import string

import requests


def test_add_pet():
    url = 'http://localhost:8080/pets'

    headers = {'Content-Type': 'application/json'}

    random_name = ''.join(random.choice(string.ascii_lowercase) for i in range(8))

    payload = {
        'animal_type': 'Cat',
        'name': random_name
    }

    # convert dict to json by json.dumps() for body data.
    resp = requests.post(url, headers=headers, data=json.dumps(payload))

    # Validate response headers and body contents, e.g. status code.
    assert resp.status_code == 201
    resp_body = resp.json()
    assert resp_body['id'] > 1


def test_add_pet_failed():
    url = 'http://localhost:8080/pets'

    headers = {'Content-Type': 'application/json'}

    random_name = ''.join(random.choice(string.ascii_lowercase) for i in range(8))

    payload = {
        'animal_type': 'Cat',
        'name': random_name
    }

    # convert dict to json by json.dumps() for body data.
    resp = requests.post(url, headers=headers, data=json.dumps(payload))

    # Validate response headers and body contents, e.g. status code.
    assert resp.status_code == 201

    # Try to add the same pet again
    resp = requests.post(url, headers=headers, data=json.dumps(payload))

    # Validate status code 404
    assert resp.status_code == 404
