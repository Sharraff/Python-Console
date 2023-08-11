#!/usr/bin/python3
# -*- coding: utf-8 -*-

import uuid
from datetime import datetime
import models

class BaseModel:
    """
    this class defines all common attributes/methods
    for other classes 
    """
    def __init__(self, *args, **kwargs):
        """
        init method for BaseModel class

        Attributes:
            args (list): inputted arguments as a list.
            kwargs (dict): inputted arguments as a dict.
            id (str): assign with an uuid when an instance is created
            created_at (time):  datetime - assign with the current datetime when
                an instance is created.
            updated_at (time): datetime - assign with the current datetime when
                n instance is created and it will be updated every time you
                change your object.
        """
        if len(kwargs) > 0:
            for key, value in kwargs.items():
                if key in ["created_at", "updated_at"]:
                    self.__dict__[key] = datetime\
                                        .strptime(value, '%Y-%m-%dT%H:%M:%S.%f')
                elif key == 'id':
                    self.id = value
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)
    
    def __str__(self):
        """
        this method returns a string representation for the BaseModel
        class
        """
        return "[{}] ({}) {}".format(self.__class__.__name__, self.id,
                                     self.__dict__)
    
    def save(self):
        """
        updates the public instance attribute updated_at with the
        current datetime
        """
        update_at = datetime.now()
        models.storage.save()
    
    def to_dict(self):
        """returns a dictionary containing all keys/values of __dict__
        of the instance

        Return:
            dictionary (dict): Dictionary object that contains __dict__
        """
        dictionary = self.__dict__.copy()
        dictionary["created_at"] = self.created_at.isoformat()
        dictionary["updated_at"] = self.updated_at.isoformat()
        dictionary["__class__"] = self.__class__.__name__
        return dictionary