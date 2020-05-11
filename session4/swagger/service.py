from swagger.exceptions import DuplicatePetError, PetNotFoundError
from swagger.model import Pet
from swagger.pets_database import db_session


def put_pet(name, animal_type, created=None):
    if get_pet_by_name(name):
        raise DuplicatePetError()
    pet = Pet(name, animal_type, created)
    db_session.add(pet)
    db_session.commit()
    return pet.to_dict()


def get_all_pets(limit=None):
    if limit:
        pets = Pet.query.limit(limit).all()
    else:
        pets = Pet.query.all()
    return [pet.to_dict() for pet in pets]


def get_pet_by_name(name):
    pet = Pet.query.filter(Pet.name == name).first()
    return pet.to_dict() if pet else None


def get_pets_by_type(animal_type):
    pets = Pet.query.filter(Pet.animal_type == animal_type).all()
    return [pet.to_dict() for pet in pets]


def get_pets_created_after(timestamp):
    pets = Pet.query.filter(Pet.created > timestamp).all()
    return [pet.to_dict() for pet in pets]


def get_pet_by_id(id):
    pet = Pet.query.filter(Pet.id == id).first()
    return pet if pet else None


def delete_pet_by_id(id):
    pet = get_pet_by_id(id)
    if not pet:
        raise PetNotFoundError()
    db_session.delete(pet)
    db_session.commit()


def get_pets_by_creation_date(date):
    return Pet.query.filter(Pet.created >= date).all()
