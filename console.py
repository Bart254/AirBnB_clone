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
            print("** class doesn't exist **")

    def do_show(self, arg):
        """ Prints string representation of an instance
        """
        if len(arg) == 0:
            print("** class name missing **")
        else:
            arg_list = arg.split()
            if arg_list[0] in globals():
                obj_class = globals()[arg_list[0]]
                if len(arg_list) < 2:
                    print("** instance id missing **")
                else:
                    obj_id = arg_list[1]
                    dict_key = arg_list[0] + "." + obj_id
                    all_objs = storage.all()
                    if dict_key not in all_objs.keys():
                        print("** no instance found **")
                    else:
                        obj = obj_class(**all_objs[dict_key])
                        print(obj)
            else:
                print("** class doesn't exist **")

    def do_destroy(self, arg):
        """ Deletes an instance based on class name and id
        """
        if len(arg) == 0:
            print("** class name missing **")
        else:
            arg_list = arg.split()
            if arg_list[0] in globals():
                obj_class = globals()[arg_list[0]]
                if len(arg_list) < 2:
                    print("** instance id missing **")
                else:
                    obj_id = arg_list[1]
                    dict_key = arg_list[0] + "." + obj_id
                    all_objs = storage.all()
                    if dict_key not in all_objs.keys():
                        print("** no instance found **")
                    else:
                        obj = obj_class(**all_objs[dict_key])
                        del obj
                        del all_objs[dict_key]
                        storage.__objects = all_objs
                        storage.save()
            else:
                print("** class doesn't exist **")

    def do_all(self, line):
        """ Prints all string representation of all instances
        based or not on the class name
        """
        dict_objs = storage.all()
        list_str_repr = []
        match_class = None
        if len(line) != 0:
            if line in globals():
                match_class = line
            else:
                print("** class doesn't exist **")
                return
        for key in dict_objs.keys():
            a_class = key.split(".")[0]
            if match_class is not None:
                if a_class == match_class:
                    obj_class = globals()[match_class]
                else:
                    continue
            else:
                obj_class = globals()[a_class]
            obj = obj_class(**dict_objs[key])
            list_str_repr.append(obj.__str__())
        print(list_str_repr)

    def do_update(self, args):
        """ Updates an instance based on class name and id by adding or
        updating attribute
        """
        if len(args) == 0:
            print("** class name missing **")
            return
        arg_list = args.split()
        if arg_list[0] in globals():
            obj_class = globals()[arg_list[0]]
        else:
            print("** class doesn't exist **")
            return
        if len(arg_list) < 2:
            print("** instance id missing **")
            return
        all_obj = storage.all()
        key = arg_list[0] + "." + arg_list[1]
        if key not in all_obj.keys():
            print("** no instance found **")
            return
        if len(arg_list) < 3:
            print("** attribute name missing **")
            return
        else:
            attr_name = arg_list[2]
        if len(arg_list) < 4:
            print("** value missing **")
            return
        else:
            attr_value = arg_list[3]
        all_obj[key][attr_name] = attr_value
        obj = obj_class(**all_obj[key])
        obj.save()


if __name__ == "__main__":
    HBNBCommand().cmdloop()
