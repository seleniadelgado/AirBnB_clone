#!/usr/bin/python3
import cmd
from models.base_model import BaseModel
from models.user    import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review
from models import storage


class HBNBCommand(cmd.Cmd):
    """this class is the beginning of the interpreter"""
    prompt = "(hbnb) "
    list_classes = [
                "BaseModel",
                "User",
                "Place",
                "State",
                "City",
                "Amenity",
                "Review"
                ]
# adding the classes to this list so the methods check throgh here if class
# exists.

    def do_quit(self, arg):
        """Quit command to exit the program\n"""
        return True

    def do_EOF():
        """End of File to exit file."""
        print()

    def emptyline(self):
        """method so it should not execute anything"""
        pass

    def do_create(self, *args):
        """Creates new instance of BaseModel & saves to json file & prints
        id"""
        """ args without commas created a tuple of 1, so I created a list with
        the tuple being split by spaces  """
        args = [ele for ele in args[0].split(' ')]
        if args[0] == '':
            print("** class name missing **")
            return
        if args[0] not in self.list_classes:
            print("** class doesn't exist **")
            return
        newinstance = eval("{}()".format(args[0]))
        newinstance.save()
        print(newinstance.id)

    def do_show(self, *args):
        """prints the str rep. of an instance based on the class and id."""
        args = [ele for ele in args[0].split(' ')]
        if args[0] == '':
            print("** class name missing **")
            return
        if args[0] not in self.list_classes:
            print("** class doesn't exist **")
            return
        if len(args) != 2:
            print("** instance id missing **")
            return

        storage.reload()
        dict_objs = storage.all()
        if dict_objs is None or dict_objs == []:
            print("** no instance found **")
            return

        key = "{}.{}".format(args[0], args[1])
        if key in dict_objs.keys():
            print(dict_objs[key])
        else:
            print("** no instance found **")

    def do_destroy(self, *args):
        """deletes an instance based on the class name and id, must save the
        change in the JSON file)"""
        args = [ele for ele in args[0].split(' ')]
        if args[0] == '':
            print("** class name missing **")
            return
        if args[0] not in self.list_classes:
            print("** class doesn't exist **")
            return
        if len(args) != 2:
            print("** instance id missing **")
            return

        storage.reload()
        dict_objs = storage.all()
        if dict_objs is None or dict_objs == []:
            print("** no instance found **")
            return

        key = "{}.{}".format(args[0], args[1])
        if key in dict_objs.keys():
            del dict_objs[key]
            storage.save()
        else:
            print("** no instance found **")


    def do_all(self, *args):
        """prints all string representation of all instances based or not on the
        class name"""
        args = [ele for ele in args[0].split(' ')]
        print_obj = []
        storage.reload()
        if args[0] == '':
            for key, obj in storage.all().items():
                print_obj.append(obj.__str__())
            print(print_obj)
            return
        if args[0] not in self.list_classes:
            print("** class doesn't exist **")
            return
        else:
            ''' Get a list of specified instances '''
            print(storage.all().items())
            for key, obj in storage.all().items():
                key = key.split('.')
                if key[0] == args[0]:
                    print_obj.append(obj.__str__())
            print(print_obj)



    def do_update(self, *args):
        """update/adds attributes in an instance based on class and id."""
        args = [ele for ele in args[0].split(' ')]
        if args[0] == '':
            print("** class name missing **")
            return
        if args[0] not in self.list_classes:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        elif len(args) < 3:
            print("** attribute name is missing **")
            return
        elif len(args) < 4:
            print("** value missing **")
            return

        storage.reload()
        dict_objs = storage.all()
        if dict_objs is None or dict_objs == []:
            print("** no instance found **")
            return

        key = "{}.{}".format(args[0], args[1])
        if key in dict_objs.keys():
            dict_objs[key][args[2]] = args[3]
            storage.save()
        else:
            print("** no instance found **")

if __name__ == '__main__':
    HBNBCommand().cmdloop()
