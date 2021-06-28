#!/usr/bin/python3
""" module to define FileStorage
        -that serializes instances to a JSON
        -that deserializes JSON file to an instances
"""

import json,  os.path
from os import closerange
class FileStorage:
    """ __file_path:
        __objects:
            -dictionary of objects: key=id + value=object
    """
    __file_path = 'file.json'
    __objects = {}

    def all(self):
        """Returns: the dictionary __objects """
        # print(FileStorage.__objects)
        return FileStorage.__objects

    def new(self, obj):
        """ sets in __objects the obj with key <obj class name>.id """
        obj_dict = obj.to_dict()
        key = "{}.{}".format( obj_dict["__class__"], obj_dict["id"])
        FileStorage.__objects[key] = obj



    def save(self):
        """ serializes __objects to the JSON file (path: __file_path)
            -my_dict_elements:
                the final dictionary representation to be converted into a JSON string
            -dict_value:
                the conversion of the python object into a dictionary
        """
        my_dict_elements = {}
        for key, value in FileStorage.__objects.items():
            dict_value = value.to_dict()
            #print(type(dict_value["updated_at"]))
            my_dict_elements.update({key: dict_value})
        with open('{}'.format(FileStorage.__file_path), 'w') as file:
            json.dump(my_dict_elements, file)


    def reload(self):
        """ deserializes the JSON file to __objects:
            -only if the JSON file (__file_path) exists ; otherwise, do nothing.
            -If the file doesn’t exist, no exception should be raised)
        """
        if os.path.exists('{}'.format(FileStorage.__file_path)) == True:
            with open('{}'.format(FileStorage.__file_path), 'r', encoding="UTF-8") as file:
                json_data = json.load(file)
                print(type(json_data))
            for key, value in json_data.items():
                FileStorage.new(self, value)
