from db import PetStoreDB


def get_pets(limit, animal_type=None):
    return PetStoreDB.get_pets(limit, animal_type)
