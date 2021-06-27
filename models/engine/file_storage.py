#!/usr/bin/python3
""" module to define FileStorage
        -that serializes instances to a JSON
        -that deserializes JSON file to an instances
"""

import json,  os.path
class FileStorage:
    __file_path = 'file.json'
    __objects = {}

    def all(self):
        """Returns: the dictionary __objects """
        return FileStorage.__objects

    def new(self, obj):
        """ sets in __objects the obj with key <obj class name>.id """
        obj_dict = obj.to_dict()
        key = "{}.{}".format( obj_dict[__class__], obj_dict[id])
        FileStorage.__objects[key] = obj



    def save(self):
        """ serializes __objects to the JSON file (path: __file_path)
            -my_dict_elements:
                the final dictionary representation to convert into JSON string
            -dict_value:
                the conversion of the python object into a dictionary

        """
        my_dict_elemenets = {}
        for key, value in FileStorage.__objects.items():
            dict_value = value.to_dict()
            my_dict_elemenets.update({key: dict_value})

        with open('{}'.format(FileStorage.__file_path), 'w') as file:
            file.write(json.dump(my_dict_elemenets))


    def reload(self):
        """ deserializes the JSON file to __objects:
            -only if the JSON file (__file_path) exists ; otherwise, do nothing.
            -If the file doesn’t exist, no exception should be raised)
        """
        if os.path.exists('{}'.format(FileStorage.__file_path)) == True:
            FileStorage.__objects = json.load('{}'.format(FileStorage.__file_path))