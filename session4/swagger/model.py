from datetime import datetime

from sqlalchemy import Column, String, DateTime, Integer, inspect

from swagger.pets_database import Base


class Pet(Base):

    __tablename__ = 'pets'

    id = Column(Integer(), primary_key=True)
    name = Column(String(50), unique=True)
    animal_type = Column(String(50))
    created = Column(DateTime())

    def __init__(self, name, animal_type, created=None):
        self.name = name
        self.animal_type = animal_type
        self.created = created if created is not None else datetime.now()

    def __repr__(self):
        return f'<Pets {self.name}>'

    def to_dict(self):
        return {c.key: getattr(self, c.key) for c in inspect(self).mapper.column_attrs}

