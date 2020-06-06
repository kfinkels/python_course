from flask import request

from swagger.exceptions import DuplicatePetError, PetNotFoundError
from swagger.service import get_pets_by_type, get_all_pets, put_pet, get_pet_by_id, \
    delete_pet_by_id, get_pets_by_creation_date


def get_pets(limit, animal_type=None):
    if animal_type:
        return get_pets_by_type(animal_type), 200
    return get_all_pets(limit), 200


def get_pet(pet_id):
    pet = get_pet_by_id(pet_id)
    return (pet.to_dict(), 200) if pet else ({'message': f'Pet {pet_id} does not exist'}, 404)


def delete_pet(pet_id):
    try:
        delete_pet_by_id(pet_id)
        return '', 204
    except PetNotFoundError:
        return {'message': f'Pet {pet_id} does not exist'}, 404


def add_pet():
    data = request.json
    name = data.get('name')
    try:
        return put_pet(name, data.get('animal_type')), 201
    except DuplicatePetError:
        return {'message': f'Pet with name : {name} already Exists'}, 404


def get_pet_after_creation_date(creation_date):
    return [pet.to_dict() for pet in get_pets_by_creation_date(creation_date)], 200
