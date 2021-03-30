#!/usr/bin/python3
"""This module defines a base class for all models in our hbnb clone"""
import uuid
from datetime import datetime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, DateTime
import models


if models.typestorage == "db":
    Base = declarative_base()
else:
    Base = object


class BaseModel:
    """A base class for all hbnb models"""

    def __init__(self, *args, **kwargs):
        """Instatntiates a new model"""
        if kwargs:  # Key-Value pairs given at creation.
            for key, value in kwargs.items():
                if key != '__class__':
                    if key == "created_at" or key == "updated_at":
                        setattr(self, key, datetime.
                                strptime(value, "%Y-%m-%dT%H:%M:%S.%f"))
                    else:
                        setattr(self, key, value)
        elif args:  # A dictionary given at creation will be in a tuple.
            for dictionary in args:
                for key, value in dictionary.items():
                    if key != '__class__':
                        if key == "created_at" or key == "updated_at":
                            setattr(self, key, datetime.
                                    strptime(value, "%Y-%m-%dT%H:%M:%S.%f"))
                        else:
                            setattr(self, key, value)
        else:  # No arguments at the time of creation.
            self.id = str(uuid.uuid4())  # quedó funcionando eso? yesss jaja
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)
        """
        if not kwargs:
            from models import storage
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
        else:
            kwargs['updated_at'] = datetime.strptime(kwargs['updated_at'],
                                                     '%Y-%m-%dT%H:%M:%S.%f')
            kwargs['created_at'] = datetime.strptime(kwargs['created_at'],
                                                     '%Y-%m-%dT%H:%M:%S.%f')
            del kwargs['__class__']
            self.__dict__.update(kwargs)
            """

    def __str__(self):
        """Returns a string representation of the instance"""
        cls = (str(type(self)).split('.')[-1]).split('\'')[0]
        return '[{}] ({}) {}'.format(cls, self.id, self.__dict__)

    def save(self):
        """Updates updated_at with current time when instance is changed"""
        from models import storage
        self.updated_at = datetime.now()
        storage.new(self)
        storage.save()

    def to_dict(self):
        """Convert instance into dict format"""
        dictionary = {}
        dictionary.update(self.__dict__)
        dictionary.update({'__class__':
                          (str(type(self)).split('.')[-1]).split('\'')[0]})
        dictionary['created_at'] = self.created_at.isoformat()
        dictionary['updated_at'] = self.updated_at.isoformat()
        # agregar lo mismo que delete
        to_delete = "_sa_instance_state"
        for key, value in dictionary.items():
            if to_delete == key:
                del dictionary[key]
        # if to_delete in dictonary:
            # del dictonary[to_delete]
        return dictionary

    def delete(self):
        """delete the current instance from the storage"""
        storage.delete(self)
