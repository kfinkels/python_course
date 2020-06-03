from swagger.service import get_pets_by_type, get_all_pets


def get_pets(limit, animal_type=None):
    if animal_type:
        return get_pets_by_type(animal_type), 200
    return get_all_pets(limit), 200


def get_pet(pet_id):
    return {'message': f'TBD'}, 501


def delete_pet(pet_id):
    return {'message': f'TBD'}, 501


def add_pet():
    return {'message': f'TBD'}, 501


def get_pet_after_creation_date(creation_date):
    return {'message': f'TBD'}, 501
