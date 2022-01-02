from server.bo import SpoElement as spe
from server.bo.Person import Person
from server.bo.Modulepart import Modulepart
import json


class Module(spe.SpoElement):
    __type: str
    __requirement: str
    __outcome: str
    __examtype: str
    __instructor: dict
    __moduleparts: dict

    def __init__(self):
        super().__init__()
        self.__type = ""
        self.__requirement = ""
        self.__outcome = ""
        self.__examtype = ""
        self.__instructor = {}
        self.__moduleparts = {}

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
        if isinstance(instructor, Person):
            self.__instructor = {hash(instructor): instructor.get_id()}

    def get_moduleparts(self):
        return self.__moduleparts

    def set_moduleparts(self, moduleparts):
        if isinstance(moduleparts, list):
            for i in moduleparts:
                if isinstance(i, Modulepart):
                    self.__moduleparts.update({hash(i): i.get_id()})

    """ 
    Muss in Administration.py
    
    def append_moduleparts(self, module):
        if isinstance(module, Module):
            self.__moduleparts.append(hash(module))

    def remove_moduleparts(self, modulepart):
        if isinstance(modulepart, Module):
            for i in self.__moduleparts:
                if hash(modulepart) == i:
                    self.__moduleparts.remove(i)
    """

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
                self.__instructor
                )

    def json(self):
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
            'instructor': self.get_instructor()
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

    def __eq__(self, other):
        return super().__eq__(other) and\
               self.get_type() == other.get_type() and\
               self.get_requirement() == other.get_requirement() and\
               self.get_outcome() == other.get_outcome() and\
               self.get_examtype() == other.get_examtype() and \
               self.get_instructor() == other.get_instructor()

    __hash__ = spe.SpoElement.__hash__




test = Module()
person1 = Person()
person1.set_id(69)
test.set_instructor(person1)
print(test)
print(test.json())
print(hash(test))