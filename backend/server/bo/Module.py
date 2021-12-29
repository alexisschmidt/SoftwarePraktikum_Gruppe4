from server.bo import SpoElement as spe
from server.bo.Person import Person
from server.bo.Modulepart import Modulepart
import json


class Module(spe.SpoElement):
    __type: str
    __requirement: str
    __outcome: str
    __examtype: str
    __instructor: Person
    __moduleparts: list[Modulepart]

    def __init__(self):
        super().__init__()
        self.__type = ""
        self.__requirement = ""
        self.__outcome = ""
        self.__examtype = ""
        self.__instructor = Person()
        self.__moduleparts = []

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
        """Auslesen des Lernergebnisses"""
        return self.__outcome

    def set_outcome(self, outcome):
        """Setzen des Lernergebnisses"""
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

    def get_moduleparts(self):
        """Auslesen der Modulteilliste"""
        return self.__moduleparts

    def set_moduleparts(self, modulepartlist):
        self.__moduleparts = modulepartlist

    def append_moduleparts(self, modulpart):
        self.__moduleparts.append(modulpart)

    def remove_moduleparts(self, index):
        self.__moduleparts.remove(index)

    def __str__(self):
        return "Module: id: {}, name: {}, title: {}, edvnr: {}, ects: {}, workload: {}, type: {}, " \
               "requirement: {}, outcome: {}, examtype: {}, instructor: {}".format(
                self.get_id(),
                self._name,
                self._title,
                self.edvnr,
                self.ects,
                self.workload,
                self.__type,
                self.__requirement,
                self.__outcome,
                self.__examtype,
                Person.get_lastname(self.__instructor)
                )

    def json(self):
        # modulehash = []
        # for modulepart in self.__moduleparts:
        # modulehash.append(modulepart.hash())
        return json.dumps({
            'id': self.get_id(),
            'name': self.get_name(),
            'title': self.get_title(),
            'edvnr': self.get_edvnr(),
            'ects': self.get_ects(),
            'workload': self.get_workload(),
            'type': self.get_type(),
            'requirement': self.get_requirement(),
            'outcome': self.get_outcome(),
            'examtype': self.get_examtype(),
            'instructor': Person.hash(self.get_instructor())
            })

    @staticmethod
    def from_dict(dictionary=dict()):
        """Umwandeln eines Python dict() in ein Module()."""
        obj = Module()
        obj.set_id(dictionary["id"])                    # Teil von BusinessObject!
        obj.set_name(dictionary["name"])                # Teil von NamedBo!
        obj.set_title(dictionary["title"])              # Teil von NamedBo!
        obj.set_edvnr(dictionary["edvnr"])              # Teil von SpoElement!
        obj.set_ects(dictionary["ects"])                # Teil von SpoElement!
        obj.set_workload(dictionary["workload"])        # Teil von SpoElement!
        obj.set_type(dictionary["type"])
        obj.set_requirement(dictionary["requirement"])
        obj.set_outcome(dictionary["outcome"])
        obj.set_examtype(dictionary["examtype"])
        obj.set_instructor(dictionary["instructor"])
        return obj


"""
    Test Script

    test = Module() 
    print(test)
    print(test.json())
    print(test.hash())
"""