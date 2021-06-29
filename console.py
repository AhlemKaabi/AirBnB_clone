#!/usr/bin/python3

import cmd, sys
from models.base_model import BaseModel
from models import storage

class HBNBCommand(cmd.Cmd):
    """ console class """
    __classes = ["BaseModel"]

    if sys.stdin.isatty():
        print("isatty")
        prompt = '(hbnb) '
    else:
        prompt = '(hbnb) \n'

    def do_EOF(self, args):
        """ \n Exit"""
        return True

    def emptyline(self):
        """ empty line shouldn't have an output """
        pass

    def do_quit(self, args):
        """Quit command to exit the program \n"""
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
        try:
            l[0]
        except Exception:
            print("** class name missing **")
            return
        if l[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
            return
        try:
            l[1]
        except Exception:
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

    def do_update(self, cmd_line):
        """ Updates an instance based on the class name and id
        by adding or updating attribute
        (save the change into the JSON file)
        Usage: update <class name> <id> <attribute name> "<attribute value>"
        """
        args = cmd_line.split()
        if not args:
             print("** class name missing **")
             return
        if args[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
            return
        try:
            args[1]
        except Exception:
            print("** instance id missing **")
            return
        objects_dict = storage.all()
        my_key = args[0] + "." + args[1]
        if my_key not in objects_dict:
            print("** no instance found **")
            return
        try:
            args[2]
        except Exception:
            print("** attribute name missing **")
            return
        try:
            args[3]
        except Exception:
            print("** value missing **")
            return
        if args[3]:
            setattr(objects_dict[my_key],args[2], args[3])
            #BaseModel.save()

if __name__ == '__main__':
    HBNBCommand().cmdloop()