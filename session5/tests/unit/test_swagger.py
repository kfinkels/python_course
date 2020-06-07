from datetime import datetime
from mock import patch

from swagger.model import Pet
from swagger.pet_store import get_pet


@patch('swagger.pet_store.get_pet_by_id')
def test_get_pet(mock_get_pet_by_id):
    pet = {
        'animal_type': 'Cat',
        'name': 'name',
        'created': datetime.now(),
        'id': 1
    }
    pet_obj = Pet(name=pet['name'], animal_type=pet['animal_type'], created=pet['created'])
    pet_obj.id = 1
    mock_get_pet_by_id.return_value = pet_obj
    assert get_pet(1) == (pet, 200)
