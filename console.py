#!/usr/bin/python3

import cmd
from models.base_model import BaseModel
from models.user import User
from models import storage

class HBNBCommand(cmd.Cmd):

    __classes = ["BaseModel", "User"]
    
    """ console class """
    prompt = '(hbnb) '
 
    def do_EOF(self, arg):
        """ Exit """
        return True

    def emptyline(self):
        """ empty line shouldn't have an output """
        pass

    def do_quit(self, arg):
        """ execute quit command """
        return True

    def do_create(self, arg):
        """ 
        Creates a new instance of BaseModel, 
        saves it (to the JSON file) and prints the id 
        """
        if not arg:
            print("** class name missing **")
            return
        if arg not in HBNBCommand.__classes:
            print("** class doesn't exist **")
            return
        # https://tinyurl.com/9uthf24u
        klass = globals()[arg]
        obj = klass()
        obj.save()
        print(obj.id)

    def do_show(self, arg):
        """
        Prints the string representation of an instance based on the class name and id
        """
        l = arg.split()
        if not l[0]:
            print("** class name missing **")
            return
        if l[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
            return
        if not l[1]:
            print("** instance id is missing **")
            return
        objects_dict = storage.all()
        my_key = l[0] + "." + l[1]
        if my_key in objects_dict:
            print(objects_dict[my_key])
        else:
            print("** no instance found **")

    def do_destroy(self, arg):
        """ Deletes an instance based on the class 
        name and id (save the change into the JSON file)
        """
        l = arg.split()
        if not l[0]:
            print("** class name missing **")
            return
        if l[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
            return
        if not l[1]:
            print("** instance id is missing **")
            return
        my_key = l[0] + "." + l[1]
        objects_dict = storage.all()
        if my_key in objects_dict:
            del objects_dict[my_key]
            storage.save()
            print(storage.all())

    def do_all(self, arg):
        """ 
            Prints all string representation of all instances 
            based or not on the class name 
        """
        l = arg.split()
        class_name = l[0]
        if class_name not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        objects_dict = storage.all()
        print("object dicts = ")
        print(objects_dict)
        print("finish")
        l2 = []
        # if only all is is written
        if not arg:
            for key, val in objects_dict.items():
                l2.append((objects_dict[key].__str__()))
        else:
            # if the class wanted is added
            for key, val in objects_dict.items():
                if class_name in key:
                    l2.append((objects_dict[key].__str__()))
        print(l2)

if __name__ == '__main__':
    HBNBCommand().cmdloop()