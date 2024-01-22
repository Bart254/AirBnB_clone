#!/usr/bin/python3
""" This module starts up the console of our project

    The console will be used to create and modify models and manipulate storage
"""
import cmd
from models.base_model import BaseModel
from models.user import User
from models import storage
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class HBNBCommand(cmd.Cmd):
    """ Console class that inherits from cmd module
    """
    prompt = "(hbnb) "
    classes = {'BaseModel': BaseModel, 'User': User, 'State': State,
               'City': City, 'Amenity': Amenity, 'Place': Place,
               'Review': Review}

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
        """ Creates a new instance of the class passed in the arg then
        prints out its id"""
        if len(class_name) == 0:
            print('** class name missing **')
        elif class_name not in self.classes.keys():
            print("** class doesn't exist **")
        else:
            obj = self.classes[class_name]()
            obj.save()
            print(obj.id)

    def do_show(self, arg):
        """ Prints string representation of an instance
        """
        if len(arg) == 0:
            print("** class name missing **")
        else:
            list_args = arg.split()
            class_name = list_args[0]
            if class_name not in self.classes.keys():
                print("** class doesn't exist **")
            elif len(list_args) < 2:
                print("** instance id missing **")
            else:
                key = class_name + '.' + list_args[1]
                if key not in storage.all().keys():
                    print("** no instance found **")
                else:
                    obj = storage.all()[key]
                    print(obj)

    def do_destroy(self, arg):
        """ Deletes an instance based on class name and id
        """
        if len(arg) == 0:
            print("** class name missing **")
        else:
            list_args = arg.split()
            class_name = list_args[0]
            if class_name not in self.classes.keys():
                print("** class doesn't exist **")
            elif len(list_args) < 2:
                print("** instance id missing **")
            else:
                key = class_name + '.' + list_args[1]
                if key not in storage.all().keys():
                    print("** no instance found **")
                else:
                    del storage.all()[key]
                    storage.save()

    def do_all(self, args):
        """ Prints all string representation of all instances
        based or not on the class name
        """
        strings = []
        to_print = True
        if len(args) != 0:
            class_name = args
            if class_name not in self.classes.keys():
                print("** class doesn't exist **")
                to_print = False
            else:
                for key, obj in storage.all().items():
                    obj_class = key.split('.')[0]
                    if class_name == obj_class:
                        strings.append(obj.__str__())
        else:
            for obj in storage.all().values():
                strings.append(obj.__str__())
        if to_print:
            print(strings)

    def do_update(self, args):
        """ Updates an instance based on class name and id by adding or
        updating attribute
        """
        if len(args) == 0:
            print("** class name missing **")
        else:
            list_args = args.split()
            class_name = list_args[0]
            if class_name not in self.classes.keys():
                print("** class doesn't exist **")
            elif len(list_args) < 2:
                print("** instance id missing **")
            else:
                key = class_name + '.' + list_args[1]
                if key not in storage.all().keys():
                    print("** no instance found **")
                elif len(list_args) < 3:
                    print("** attribute name missing **")
                elif len(list_args) < 4:
                    print("** value missing **")
                else:
                    attr = list_args[2]
                    if list_args[3][0] == '"' and list_args[3][-1] == '"':
                        value = list_args[3][1:-1]
                    elif '.' in list_args[3]:
                        value = float(list_args[3])
                    else:
                        value = int(list_args[3])
                    obj = storage.all()[key]
                    obj.__dict__.update({attr: value})
                    obj.save()


if __name__ == "__main__":
    HBNBCommand().cmdloop()
