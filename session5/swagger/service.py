from swagger.model import Pet


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
