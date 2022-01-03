from server.bo import NamedBo as nbo
"""das Modul "datetime" wird importiert um das datumsformat für Variablen zu verwenden"""
from server.bo.Semester import Semester
from server.bo.Module import Module
from server.bo.StudyCourse import StudyCourse
import json


class Spo (nbo.NamedBo):
    _start_semester: dict
    _end_semester: dict
    _modules: dict
    _studycourse: dict

    def __init__(self):
        super().__init__()
        self._start_semester = {}   # Anfangssemester der SPO Gültigkeit
        self._end_semester = {}     # Endsemester der SPO Gültigkeit
        self._modules = {}          # Module, die die SPO bilden
        self._studycourse = {}      # Studiengang der SPO

    def get_start_semester(self):
        """Auslesen des Anfangsdatums der SPO Gültigkeit """
        return self._start_semester

    def set_start_semester(self, start_semester):
        """Setzen des Anfangsdatums der SPO Gültigkeit """
        if isinstance(start_semester, Semester):
            self._start_semester = {hash(start_semester): start_semester.get_id()}

    def get_end_semester(self):
        """Auslesen des Enddatums der SPO Gültigkeit """
        return self._end_semester

    def set_end_semester(self, end_semester):
        """Setzen des Enddatums der SPO Gültigkeit """
        if isinstance(end_semester, Semester):
            self._end_semester = {hash(end_semester): end_semester.get_id()}

    def get_modules(self):
        return self._modules

    def set_modules(self, modulelist):
        if isinstance(modulelist, list):
            for i in modulelist:
                if isinstance(i, Module):
                    self._modules.update({hash(i): i.get_id()})

    def append_modules(self, module):
        if isinstance(module, Module):
            self._modules.update({hash(module): module.get_id()})

    def remove_modules(self, module):
        if isinstance(module, Module):
            for i in self._modules:
                if hash(module) == i:
                    self._modules.pop(i)
                else:
                    pass

    def get_studycourse(self):
        """Auslesen des Studienganges"""
        return self._studycourse

    def set_studycourse(self, studycourse):
        """Setzen des Studiengangs"""
        if isinstance(studycourse, StudyCourse):
            self._studycourse = {hash(studycourse): studycourse.get_id()}

    def __str__(self):
        return "Spo: id: {}, name: {}, title: {}, start Semester: {}, end Semester: {}, studycourse: {}".format(
            self.get_id(),
            self._name,
            self._title,
            self.get_start_semester(),
            self.get_end_semester(),
            self.get_studycourse()
            )

    def json(self):
        return json.dumps({
            'id': self.get_id(),
            'name': self.get_name(),
            'title': self.get_title(),
            'start_semester': self.get_start_semester(),
            'end_semester': self.get_end_semester(),
            'studycourse_id': self.get_studycourse()
            })

    @staticmethod
    def from_dict(dictionary=dict()):
        """Umwandeln eines Python dict() in eine Spo()."""
        obj = Spo()
        obj.set_id(dictionary["id"])                        # Teil von BusinessObject!
        obj.set_name(dictionary["name"])                    # Teil von NamedBo!
        obj.set_title(dictionary["title"])                  # Teil von NamedBo!
        obj.set_start_semester(dictionary["start_semester"])
        obj.set_end_semester(dictionary["end_semester"])
        obj.set_studycourse(dictionary["studycourse_id"])
        return obj

    def __eq__(self, other):
        return super().__eq__(other) and self.get_start_semester() == other.get_start_semester() and \
               self.get_end_semester() == other.get_endsemester() and \
               self.get_studycourse() == other.get_studycourse()

    __hash__ = nbo.NamedBo.__hash__


"""
# Test Script

test = Spo()
print(test)
print(test.json())
print(hash(test))
"""