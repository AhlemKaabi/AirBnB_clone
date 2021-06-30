#!/usr/bin/python3
""" HBnB console Module """
import cmd
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class HBNBCommand(cmd.Cmd):
    """
    Defines the HBnB command interpreter.
    Attributes:
        prompt: The command prompt.
    """
    
    __classes = [
        "BaseModel", "User", "State",
        "Place", "City", "Amenity",
        "Review"
        ]

    
    prompt = '(hbnb) '

    @classmethod
    def count(self, class_name, objects_dict):
        """ count the class """
        ct = 0
        for key in objects_dict.keys():
            if class_name in key:
                ct += 1
        print(ct)

    @classmethod
    def all(self, class_name, objects_dict):
        """ print all objects of class_name """
        l2 = []
        for key, val in objects_dict.items():
            if class_name in key:
                l2.append((objects_dict[key].__str__()))
        print(l2)

    @classmethod
    def show(self, class_name, objects_dict, idd):
        """ show instance by id """
        cs = class_name + "." + idd
        if cs in objects_dict:
            print(objects_dict[cs])
        else:
            print("** no instance found **")

    @classmethod
    def update(self, class_name, objects_dict, info_list):
        my_key = class_name + "." + info_list[0]
        my_obj = objects_dict[my_key]
        if my_obj:
            setattr(my_obj, info_list[1], info_list[2])
            my_obj.updated_at = datetime.now()
            storage.save()

    @classmethod
    def destroy(self, class_name, objects_dict, idd):
        """ destroy instance by id """
        my_obj = class_name + "." + idd
        if my_obj in objects_dict:
            del objects_dict[my_obj]
            storage.save()
        else:
            print("** no instance found **")

    def default(self, arg):
        """ default command is not recognized """
        # split the command into 2 elements [class,methode]
        objects_dict = storage.all()
        l = arg.split(".")
        if len(l) != 2:
            return
        class_name = l[0]
        method_name = l[1]
        if class_name not in HBNBCommand.__classes:
            print("** class not available **")
            return
        if method_name == "count()":
            HBNBCommand.count(class_name, objects_dict)
        elif method_name == "all()":
            HBNBCommand.all(class_name, objects_dict)
        elif "show" in method_name:
            """ first parse what is inside id """
            pos1 = method_name.find('(')
            pos2 = method_name.find(')')
            idd = method_name[pos1+2:pos2-1]
            HBNBCommand.show(class_name, objects_dict, idd)
        elif "destroy" in method_name:
            pos1 = method_name.find('(')
            pos2 = method_name.find(')')
            idd = method_name[pos1+2:pos2-1]
            HBNBCommand.destroy(class_name, objects_dict, idd)
        elif "update" in method_name:
            pos1 = method_name.find('(')
            pos2 = method_name.find(')')
            info = method_name[pos1+2:pos2-1]
            new_info = info.replace("\"", "")
            new_info = new_info.replace(" ", "")
            info_list = new_info.split(",")
            HBNBCommand.update(class_name, objects_dict, info_list)

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
        Prints the string representation of an
        instance based on the class name and id
        """
        l = arg.split()
        if not arg:
            print("** class name missing **")
            return
        if l[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
            return
        if len(l) == 1:
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
        if not arg:
            print("** class name missing **")
            return
        if l[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
            return
        if len(l) == 1:
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
        objects_dict = storage.all()
        l2 = []
        # list is not empty so a class was given as argument
        if len(l):
            class_name = l[0]
            if class_name not in HBNBCommand.__classes:
                print("** class doesn't exist **")
                return
            for key, val in objects_dict.items():
                if class_name in key:
                    l2.append((objects_dict[key].__str__()))
        else:
            # if the class wanted is added
            for key, val in objects_dict.items():
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
            setattr(objects_dict[my_key], args[2], args[3])
            my_obj.updated_at = datetime.now()
            storage.save()


if __name__ == '__main__':
    HBNBCommand().cmdloop()
