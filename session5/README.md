# **Getting started**

`virtualenv -p python3 env`

`source env/bin/activate`

`pip install -r requirements.txt`

`curl -X GET --header 'Accept: application/json' 'http://localhost:8080/pets/1/dog'`


# **Flask**

`https://palletsprojects.com/p/flask/`

# **Connexion with Swagger**

`http://localhost:8080/swagger.yaml`

`http://localhost:8080/ui/#!/default`

# **SQLAlchemy**

`https://www.sqlalchemy.org/`

`https://flask.palletsprojects.com/en/1.1.x/patterns/sqlalchemy/`


# **Gunicorn**

`https://gunicorn.org/`

`http://docs.gunicorn.org/en/latest/design.html`

# **Exercises**

1. Implement add pet
2. Implement get pet by ID
3. Implement delete pet by ID
4. Implement get all pets created after DATE
5. Change animal_type to one of (enum)

# **PyCharm configuration**

Flask Example:
https://github.com/kfinkels/python_course/tree/master/session4/images/flask.png

Gunicorn Example: 
https://github.com/kfinkels/python_course/tree/master/session4/images/gunicorn.png

Swagger Example:
https://github.com/kfinkels/python_course/tree/master/session4/images/swagger.png
