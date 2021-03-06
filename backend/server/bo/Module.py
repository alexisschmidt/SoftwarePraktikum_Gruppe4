from server.bo import SpoElement as Spe
import json


class Module(Spe.SpoElement):
    _type: int          # Typ des Moduls
    _requirement: str   # Anforderungen des Moduls
    _outcome: str       # Lernergebnisse des Moduls
    _examtype: int      # Prüfungsart des Moduls
    _instructor: int    # Modulverantwortliche Person
    _parts: list[int]   # zugehörige Modulteile

    def __init__(self):
        super().__init__()
        self._type = 0
        self._requirement = ""
        self._outcome = ""
        self._examtype = 0
        self._instructor = 0
        self._parts = []

    # Auslesen
    def get_type(self):
        """Auslesen des Modultyps"""
        return self._type

    def set_type(self, mtype: int):
        """Setzen des Modultyps"""
        self._type = mtype

    def get_requirement(self):
        """Auslesen der Voraussetzung(en)"""
        return self._requirement

    def set_requirement(self, requirement: str):
        """Setzen der Voraussetzung(en)"""
        self._requirement = requirement

    def get_outcome(self):
        """Auslesen des Lernergebnisses"""
        return self._outcome

    def set_outcome(self, outcome: str):
        """Setzen des Lernergebnisses"""
        self._outcome = outcome

    def get_examtype(self):
        """Auslesen des Prüfungstyps"""
        return self._examtype

    def set_examtype(self, examtype: int):
        """Setzen des Prüfungstyps"""
        self._examtype = examtype

    def get_instructor(self):
        """Auslesen des Modulverantwortlichen"""
        return self._instructor

    def set_instructor(self, instructor: int):
        """Setzen des Modulverantwortlichen"""
        self._instructor = instructor

    def get_parts(self):
        return self._modules

    def set_parts(self, parts: list[int]):
        self._modules = parts

    def append_part(self, part: int):
        self._modules.append(part)

    def remove_part(self, part: int):
        self._modules.remove(part)

    def __str__(self):
        astring = (
            f"Module: "
            f"id: {self.get_id()}, "
            f"name: {self._name}, "
            f"title: {self._title}, "
            f"edvnr: {self._edvnr}, "
            f"ects: {self._ects}, "
            f"workload: {self._workload}, "
            f"type: {self._type}, "
            f"requirement: {self._requirement}, "
            f"outcome: {self._outcome}, "
            f"examtype: {self._examtype}, "
            f"instructor: {self._instructor}"
        )
        return astring

    def json(self):
        return json.dumps({
            'name': self.get_name(),
            'title': self.get_title(),
            'edvnr': self.get_edvnr(),
            'ects': self.get_ects(),
            'workload': self.get_workload(),
            'type': self.get_type(),
            'requirement': self.get_requirement(),
            'outcome': self.get_outcome(),
            'examtype': self.get_examtype(),
            'instructor': self.get_instructor(),
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
        obj.set_instructor(dictionary["instructor"])    # könnte geändert werden müssen
        return obj

    def __eq__(self, other):
        return super().__eq__(other) and\
               self.get_type() == other.get_type() and\
               self.get_requirement() == other.get_requirement() and\
               self.get_outcome() == other.get_outcome() and\
               self.get_examtype() == other.get_examtype() and \
               self.get_instructor() == other.get_instructor()

    __hash__ = Spe.SpoElement.__hash__

