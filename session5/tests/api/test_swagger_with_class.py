import json
import random
import string

import requests


class TestSwaggerApp:

    @classmethod
    def setup_class(cls):
        cls.pets_url = 'http://localhost:8080/pets'
        cls.headers = {'Content-Type': 'application/json'}

    def test_add_pet(self):
        random_name = ''.join(random.choice(string.ascii_lowercase) for i in range(8))

        payload = {
            'animal_type': 'Cat',
            'name': random_name
        }

        # convert dict to json by json.dumps() for body data.
        resp = requests.post(self.pets_url, headers=self.headers, data=json.dumps(payload))

        # Validate response headers and body contents, e.g. status code.
        assert resp.status_code == 201
        resp_body = resp.json()
        assert resp_body['id'] > 1
