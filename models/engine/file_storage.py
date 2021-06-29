#!/usr/bin/python3
""" module to define FileStorage
        -that serializes instances to a JSON
        -that deserializes JSON file to an instances
"""

import json,  os.path
from models.base_model import BaseModel
from models.user import User

class FileStorage:
    __file_path = 'file.json'
    __objects = {}

    def all(self):
        """Returns: the dictionary __objects """
        return self.__objects

    def new(self, obj):
        """ sets in __objects the obj with key <obj class name>.id """
        obj_dict = obj.to_dict()
        key = "{}.{}".format(obj_dict["__class__"], obj_dict["id"])
        self.__objects[key] = obj



    def save(self):
        """ serializes __objects to the JSON file (path: __file_path)
            -my_dict_elements:
                the final dictionary representation to be converted into a JSON string
            -dict_value:
                the conversion of the python object into a dictionary
        """
        my_dict_elements = {}
        for key, value in self.__objects.items():
            dict_value = value.to_dict()
            my_dict_elements.update({key: dict_value})

        with open(self.__file_path, 'w') as file:
            json.dump(my_dict_elements, file)


    def reload(self):
        """ deserializes the JSON file to __objects:
            -only if the JSON file (__file_path) exists ; otherwise, do nothing.
            -If the file doesn’t exist, no exception should be raised)
        """
        if os.path.exists('{}'.format(self.__file_path)) == True:
            with open(self.__file_path, 'r') as file:
                my_dict_elements = json.load(file)
                for key, value in my_dict_elements.items():
                    """ we load the content of file.json as dictionnaries object
                        then convert the dictionary object to Base_model class
                        so we can apply to_dict()
                    """
                    clas = value["__class__"]
                    clas = eval(clas)
                    self.new(clas(**value))