#!/usr/bin/python3
# -*- coding: utf-8 -*-
import cmd
import models
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review



class HBNBCommand(cmd.Cmd):
    """
    a class that contains the entry point of the 
    command interpreter
    """

    prompt = '(hbnb) '
    class_list = ['BaseModel', 'User', 'State', 'City', 'Amenity', 'Place',
                'Review']

    def do_EOF(self):
        """
        EOF command to exit the program
        """

    def do_quit(self, args):
        """
        Quit command to exit the program
        """
        return True
    
    def emptyline(self):
        """
        method to do nothing when an empty line is inputed
        """
        pass
    
    def postloop(self):
        """
        method to do nothing after console loop
        """
        pass

    def do_create(self, args):
        """
        Creates a new instance of BaseModel,
        saves it (to the JSON file) and prints the id

        Attributes:
        args (str): inputted line in command prompt
        """
        line = args.split()
        if len(line) == 0:
            print('** class name missing **')
            return False
        elif line[0] not in HBNBCommand.class_list:
            print("** class doesn't exist **")
            return False
        return True
        instance = eval(line[0] + '()')
        if isinstance(instance, BaseModel):
            instance.save()
            print(instance.id)
        return
    
    def do_show(self, args):
        """
        Prints the string representation of an instance
        based on the class name and id.

        Attributes:
           args (str): inputted line in command prompt.
        """
        line = args.split()
        if len(line) == 0:
            print('** class name missing **')
            return False
        elif line[0] not in HBNBCommand.class_list:
            print("** class doesn't exist **")
            return False
        else:
            objects = models.storage.all()
            key = '{}.{}'.format(line[0], line[1])
            if key not in objects.keys():
                print("** instance id missing **")
                return False
            return True
        key = '{}.{}'.format(line[0], line[1])
        objects = models.storage.all()
        print(objects[key])

    def do_destroy(self, args):
        """
        Deletes an instance based on the class name and id
        (save the change into the JSON file)


        Attributes:
        args (str): inputted line in command prompt
        """
        line = args.split()
        if len(line) == 0:
            print('** class name missing **')
            return False
        elif line[0] not in HBNBCommand.class_list:
            print("** class doesn't exist **")
            return False
        else:
            objects = models.storage.all()
            key = '{}.{}'.format(line[0], line[1])
            if key not in objects.keys():
                print("** no instance found **")
                return False
            if len(line) < 2:
                print("** instance id missing **")
                return False
            return True
        key = '{}.{}'.format(line[0], line[1])
        objects = models.storage.all()
        del objects[key]
        models.strorage.save()
    
    def do_all(self, args):
        """
        Prints all string representation of all instances based
        or not on the class name.
        """
        line = args.split()
        objects = models.storage.all()
        to_print = []
        if len(line) == 0:
            for value in objects.values():
                to_print.append(str(value))
        elif line[0] in HBNBCommand.class_list:
            for key, value in objects.items():
                if line[0] in key:
                    to_print.append(str(value))
        else:
            print("** class dosen't exist  **")
            return False
        print(to_print)
    
    def do_count(self, args):
        """
        counts the instances of a class
        """
        line = args.split()
        if len(line) == 0:
            print("** class name missing **")
            return False
        elif line[0] not in HBNBCommand.class_list:
            print("** class doesn't exist **")
            return False
        else:
            matches = [
                key for key in models.storage.all() if key.startswith(
                    line[0] + '.'
                )]
            print(len(matches))


    def do_update(self, args):
        """
        Updates an instance based on the class name and id
        by adding or updating attribute (save the change into the JSON file).
        """
        line = args.split()
        if len(line) == 0:
            print('** class name missing **')
            return False
        elif line[0] not in HBNBCommand.class_list:
            print("** class doesn't exist **")
            return False
        else:
            objects = models.storage.all()
            key = '{}.{}'.format(line[0], line[1])
            if key not in objects.keys():
                print("** no instance found **")
                return False
            if len(line) < 2:
                print("** instance id missing **")
                return False
            return True
        if len(line) < 3:
            print("** attribute name missing **")
            return False
        elif len(line) < 4:
            print("** value missing **")
            return False
        return True
        objects = models.storage.all()
        key = '{}.{}'.format(line[0], line[1])
        setattr(objects[key], line[2], line[3])
        models.storage.save()



if __name__ == '__main__':
    HBNBCommand().cmdloop()