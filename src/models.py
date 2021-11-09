import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relation, relationship
from sqlalchemy import create_engine
from sqlalchemy.sql.schema import MetaData
from eralchemy import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    username = Column(String(250), nullable=False, unique=True)
    first_name = Column(String(250), nullable=False)
    last_name = Column(String(250), nullable=False)
    email =  Column(String(250), nullable=False, unique=True)
    password = Column(String(120), nullable=False, unique=True)

class Favorites(Base):
    __tablename__ = 'favorites'
    id_fav = Column(Integer, primary_key=True)
    character_fav = Column(String(250), nullable=False)
    planet_fav = Column(String(250), nullable=False)
    vehicles_fav = Column(String(250), nullable=False)
    id_user = Column(Integer, ForeignKey('user.id'))
    userfavorites =  relationship(User)

class Characters(Base):
    __tablename__ = 'characters'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    homeplanet = Column(Integer, ForeignKey('planet.id'))
    favorites =  Column(Integer, ForeignKey('favorites.character_fav'))
    user = relationship(User)

class Planets(Base):
    __tablename__ = 'planets'
    id =  Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    character = Column(String(250), ForeignKey('characters.id'))
    climate = Column(String(250), nullable=False)
    terrain = Column(String(250), nullable=False)
    population = Column(Integer)
    favorites =  Column(Integer, ForeignKey('favorites.planet_fav'))
    user = relationship(User)

class Vehicles(Base):
    __tablename__ = 'vehicles'
    id =  Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    model = Column(String(250), nullable=False)
    manufacturer = Column(String(250), nullable=False)
    pilots = Column(String(250), ForeignKey('characters.id'))
    favorites =  Column(Integer, ForeignKey('favorites.vehicles_fav'))
    user = relationship(User)




class Person(Base):
    __tablename__ = 'person'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)

class Address(Base):
    __tablename__ = 'address'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    street_name = Column(String(250))
    street_number = Column(String(250))
    post_code = Column(String(250), nullable=False)
    person_id = Column(Integer, ForeignKey('person.id'))
    person = relationship(Person)

    def to_dict(self):
        return {
            "id": self.id,
            "username": self.username
        }

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')








