#!/usr/bin/python3

import cmd

class HBNBCommand(cmd.Cmd):
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

if __name__ == '__main__':
    HBNBCommand().cmdloop()