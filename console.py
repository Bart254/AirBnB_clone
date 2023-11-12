#!/usr/bin/python3
""" A console Module
"""
import cmd
from models.base_model import BaseModel


class HBNBCommand(cmd.Cmd):
    """ console class
    """
    prompt = "(hbnb) "

    def do_quit(self, line):
        """Quit command to exit the program
        """
        exit()

    def do_EOF(self, line):
        """EOF command to exit the program
        """
        exit()

    def emptyline(self):
        """ Does not execute anything
        """
        pass

    def do_create(self, class_name):
        """ Create command creates a new instance of BaseModel,
        saves it (to the JSON file) and prints the id"""
        if len(class_name) == 0:
            print('** class name missing **')
        elif class_name in globals():
            my_class = globals()[class_name]
            obj = my_class()
            obj.save()
            print(obj.id)
        else:
            print("** class doesnt exist **")

if __name__ ==  "__main__":
    HBNBCommand().cmdloop()
