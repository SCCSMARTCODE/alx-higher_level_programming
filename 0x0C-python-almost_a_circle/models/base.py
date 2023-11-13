#!/usr/bin/python3
"""this is a module that contains the mother class of my project
        Write the first class Base:
"""
import json


class Base:
    """The Base class:
            private class attribute __nb_objects = 0
            class constructor: def __init__(self, id=None):
            """
    __nb_objects = 0

    def __init__(self, id=None):
        """My initializer
                Arg:
                    id=None(default value)
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        
        :param list_dictionaries: 
        :return: 
                    []
                    json.dumps(list_dictionaries)
        """
        if list_dictionaries is None or list_dictionaries == []:
            return []

        if (type(list_dictionaries) != list or
           not all(type(x) == dict for x in list_dictionaries)):
            raise TypeError("list_dictionaries must be a list of dictionaries")
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """Writes the JSON string representation of
        list_objs to a file.

        """
        if list_objs is None or list_objs == []:
            jstr = "[]"
        else:
            jstr = cls.to_json_string([o.to_dictionary() for o in list_objs])
        filename = cls.__name__ + ".json"
        with open(filename, 'w') as f:
            f.write(jstr)

    @staticmethod
    def from_json_string(json_string):
        """Returns the list of the JSON string representation json_string.
        :param:
            json_string
        """
        let = []
        if json_string is not None and json_string != '':
            if type(json_string) != str:
                raise TypeError("json_string must be a string")
            let = json.loads(json_string)
        return let

    @classmethod
    def create(cls, **dictionary):
        """Returns an instance with all attributes already set.

        Args:
            - dictionary: used as **kwargs

        Returns: instance created
        """
        if dictionary and dictionary != {}:
            if cls.__name__ == 'Rectangle':
                new = cls(1, 1)

            elif cls.__name__ == 'Square':
                new = cls(1)

            new.update(**dictionary)
            return new

    @classmethod
    def load_from_file(cls):
        """
        :return:
            return json.load(f)
                    or
            []
        """
        filename = str(cls.__name__) + ".json"
        try:
            with open(filename, "r") as jsonfile:
                list_dicts = Base.from_json_string(jsonfile.read())
                return [cls.create(**d) for d in list_dicts]
        except IOError:
            return []
