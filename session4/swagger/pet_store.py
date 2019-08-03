from flask import request, jsonify

from swagger.exceptions import DuplicatePetError
from swagger.service import get_pets_by_type, get_all_pets, put_pet


def get_pets(limit, animal_type=None):
    if animal_type:
        return get_pets_by_type(animal_type), 200
    return get_all_pets(limit), 200


def add_pet():
    data = request.json
    name = data.get('name')
    try:
        return put_pet(name, data.get('animal_type')), 201
    except DuplicatePetError:
        return {'message': f'Pet with name : {name} already Exists'}, 404
