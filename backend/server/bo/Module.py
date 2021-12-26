from server.bo.SpoElement import SpoElement
import json
from server.bo.Person import Person



class Module (SpoElement): # diese infos sind nicht relevant, nicht in den anforderungen 
    __type: str
    __requirement: str
    __outcome: str
    __examtype: str
    __instructor: Person
       


    def __init__(self):
        super().__init__()
        self.__type = ""
        self.__requirement = ""
        self.__outcome = ""
        self.__examtype = ""
        self.__instructor = Person()

    # Auslesen
    def get_type(self):
        """Auslesen des Modultyps"""
        return self.__type

    def set_type(self, value):
        """Setzen des Modultyps"""
        self.__type = value

    def get_requirement(self):
        """Auslesen der Voraussetzung(en)"""
        return self.__requirement

    def set_requirement(self, requirement):
        """Setzen der Voraussetzung(en)"""
        self.__requirement = requirement

    def get_outcome(self):
        """Auslesen des Outcomes"""
        return self.__outcome

    def set_outcome(self, outcome):
        """Setzen des Outcomes"""
        self.__outcome = outcome

    def get_examtype(self):
        """Auslesen des Prüfungstyps"""
        return self.__examtype

    def set_examtype(self, examtype):
        """Setzen des Prüfungstyps"""
        self.__examtype = examtype

    def get_instructor(self):
        """Auslesen des Modulverantwortlichen"""
        return self.__instructor

    def set_instructor(self, instructor):
        """Setzen des Modulverantwortlichen"""
        self.__instructor = instructor
    


    def json(self):
        return json.dumps({'a': self.a, 'b': self.b, 'c': self.c})



    def __str__(self):
        return "Module: {}, {}, {}, {}, {}, {}".format(

            self.get_id(),
            self.__type,
            self.__requirement,
            self.__outcome,
            self.__examtype,
            self.__instructor)

    @staticmethod
    def from_dict(dictionary=dict()):
        """Umwandeln eines Python dict() in ein Module()."""
        obj = Module()
        obj.set_id(dictionary["id"])                    # Teil von BusinessObject!
        obj.set_name(dictionary["name"])                # Teil von NamedBo!
        obj.set_title(dictionary["title"])              # Teil von NamedBo!
        obj.set_type(dictionary["type"])
        obj.set_requirement(dictionary["requirement"])
        obj.set_outcome(dictionary["outcome"])
        obj.set_examtype(dictionary["examtype"])
        obj.set_instructor(dictionary["instructor"])
        return obj
