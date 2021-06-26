#!/usr/bin/python3
""" module to define BaseModel """
import uuid
from datetime import datetime

class BaseModel:
    """ class BaseModel that defines all common attributes/methods for other classe """
    
    def __init__(self, *args, **kwargs):
        """ initialiaze id, created_at, updated_at public instance attributes 
            if kwargs is not empty they will be setted from kwargs """
        if (len(kwargs) == 0):
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
        else:
            kwargs["created_at"] = datetime.strptime(kwargs["created_at"],
                                                     "%Y-%m-%dT%H:%M:%S.%f")
            kwargs["updated_at"] = datetime.strptime(kwargs["updated_at"],
                                                     "%Y-%m-%dT%H:%M:%S.%f")
            for key in kwargs:
                if key != "__class__":
                    setattr(self, key, kwargs[key])
    
    def __str__(self):
        """ print: [<class name>] (<self.id>) <self.__dict__> """
        return "[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__)

    def save(self):
        """  updates the public instance attribute updated_at with the current datetime """
        self.updated_at = datetime.now()

    def to_dict(self):
        """ returns a dictionary containing all keys/values of __dict__ of the instance """
        d = self.__dict__
        d["__class__"] = self.__class__.__name__
        d["created_at"] = self.created_at.strftime("%Y-%m-%dT%H:%M:%S.%f")
        d["updated_at"] = self.updated_at.strftime("%Y-%m-%dT%H:%M:%S.%f")
        return d
