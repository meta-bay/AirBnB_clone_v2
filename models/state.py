#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
import models
from models.city import City
import shlex


class State(BaseModel, Base):
    """ State class """
    __tablename__ = "states"
    name = Column(String(128), nullable=False)
    cities = relationship("City", cascade='all, delete, delete-orphan',
                          backref="state")

    @property
    def cities(self):
        all_models = models.storage.all()
        cont = []
        cities = []
        for key in all_models:
            city = key.replace('.', ' ')
            city = shlex.split(city)
            if (city[0] == 'City'):
                cont.append(all_models[key])
        for i in cont:
            if (i.state_id == self.id):
                cities.append(i)
        return (cities)
