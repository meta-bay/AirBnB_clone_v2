#!/usr/bin/python3
"""
    DB storage module
"""
from models.base_model import Base, BaseModel
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User
from sqlalchemy.orm import scoped_session, sessionmaker, Session
from sqlalchemy.exc import InvalidRequestError
from sqlalchemy import create_engine
from os import getenv


class DBStorage:
    """
        DB storage class
    """
    __engine = None
    __session = None

    def __init__(self):
        """ initializer """
        user = getenv("HBNB_MYSQL_USER")
        passwd = getenv("HBNB_MYSQL_PWD")
        db = getenv("HBNB_MYSQL_DB")
        host = getenv("HBNB_MYSQL_HOST")
        env = getenv("HBNB_ENV")

        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'
                                      .format(user, passwd, host, db),
                                      pool_pre_ping=True)

        if env == 'test':
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """
        query on the current database session
        """
        obj_dict = {}
        if cls:
            if type(cls) is str:
                cls = eval(cls)
            query = self.__session.query(cls)
            for the_item in query:
                key = "{}.{}".format(type(the_item).__name__, the_item.id)
                obj_dict[key] = the_item
        else:
            cls_list = [State, City, User, Place, Review, Amenity]
            for clase in cls_list:
                query = self.__session.query(clase)
                for the_item in query:
                    key = "{}.{}".format(type(the_item).__name__, the_item.id)
                    obj_dict[key] = the_item
        return (obj_dict)

    def new(self, obj):
        """
        add the object to the current database session
        """
        self.__session.add(obj)

    def save(self):
        """"
        commit all changes of the current database session
        """
        self.__session.commit()

    def delete(self, obj=None):
        """
        delete from the current database session
        """
        if obj:
            self.__session.delete(obj)

    def reload(self):
        """
        Reloads it
        """
        Base.metadata.create_all(self.__engine)
        session = sessionmaker(bind=self.__engine, expire_on_commit=False)
        self.__session = scoped_session(session)

    def close(self):
        """ close the session """
        self.__session.close()
