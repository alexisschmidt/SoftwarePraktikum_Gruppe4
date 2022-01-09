from server.bo import NamedBo as nbo
"""das Modul "datetime" wird importiert um das datumsformat für Variablen zu verwenden"""
from server.bo.Semester import Semester
from server.bo.Module import Module
from server.bo.StudyCourse import StudyCourse
import json


class Spo (nbo.NamedBo):
    _start_semester: Semester
    _end_semester: Semester
    _modules: list[Module]
    _studycourse: StudyCourse

    def __init__(self):
        super().__init__()
        self._start_semester = Semester()   # Anfangssemester der SPO Gültigkeit
        self._end_semester = Semester()     # Endsemester der SPO Gültigkeit
        self._modules = []                  # Module, die die SPO bilden
        self._studycourse = StudyCourse()   # Studiengang der SPO

    def get_start_semester(self):
        """Auslesen des Anfangsdatums der SPO Gültigkeit """
        return self._start_semester

    def set_start_semester(self, start_semester):
        """Setzen des Anfangsdatums der SPO Gültigkeit """
        if isinstance(start_semester, Semester):
            self._start_semester = start_semester

    def get_end_semester(self):
        """Auslesen des Enddatums der SPO Gültigkeit """
        return self._end_semester

    def set_end_semester(self, end_semester):
        """Setzen des Enddatums der SPO Gültigkeit """
        if isinstance(end_semester, Semester):
            self._end_semester = end_semester

    def get_modules(self):
        return self._modules

    def set_modules(self, modulelist):
        if isinstance(modulelist, list):
            self._modules = modulelist

    def append_modules(self, module):
        if isinstance(module, Module):
            self._modules.append(module)

    def remove_modules(self, module):
        if isinstance(module, Module) and module in self._modules:
            self._modules.remove(module)

    def get_studycourse(self):
        """Auslesen des Studienganges"""
        return self._studycourse

    def set_studycourse(self, studycourse):
        """Setzen des Studiengangs"""
        if isinstance(studycourse, StudyCourse):
            self._studycourse = studycourse

    def __str__(self):
        return f"Spo: id: {self.get_id()}, \
               name: {self._name}, title: {self._title}, \
               start Semester: {self.get_start_semester()}, \
               end Semester: {self.get_end_semester()}, \
               studycourse: {self.get_studycourse()}"

    def json(self):
        ss = hash(self.get_start_semester())
        es = hash(self.get_end_semester())
        sc = hash(self.get_studycourse())
        mlist = ""
        for module in self.get_modules():
            mlist += str(hash(module))+", "

        return json.dumps({
            'id': self.get_id(),
            'name': self.get_name(),
            'title': self.get_title(),
            'start_semester': ss,
            'end_semester': es,
            'modules': mlist,
            'studycourse_id': sc
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
print(test.json())
print(hash(test))
"""