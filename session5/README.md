# **Getting started**

create virtualenv: `virtualenv -p python3 session5`

activate the virtualenv: `source session5/bin/activate`

install requirements: <br>
`pip install -r requirements.txt`
`pip install -r dev.txt`

run application: `python app-swagger.py`

run tests: `pytest`

# **Exercises**

* API test - add failed test to post pet
* Parameterize: 
> * Write a method that compare 2 dictionaries and return a dictionary with all the matching items (key and value) 
> * Add the the following tests:
>> * There are no matched items
>> * All items match
>> * One item match
>> * dict1\dict2 is None
>> * dict1\dict2 is not a dict
* Mock: 
> * Write a unittest for swagger/pet_store.py::get_pet(pet_id)
> * Validate that the function returns a tuple `(<pet_dict>, 200)`
> * Validate that the result pet dict values are as expected
> * HINT: You should patch get_pet_by_id

