from server.bo import NamedBo as Nbo
import json


class Spo (Nbo.NamedBo):
    _start_semester: int    # Anfangssemester der SPO Gültigkeit
    _end_semester: int      # Endsemester der SPO Gültigkeit
    _studycourse: int       # Studiengang der SPO
    _modules: list[int]     # Module der SPO

    def __init__(self):
        super().__init__()
        self._start_semester = 0
        self._end_semester = 0
        self._studycourse = 0
        self._modules = []

    def get_start_semester(self):
        """Auslesen des Anfangsdatums der SPO Gültigkeit """
        return self._start_semester

    def set_start_semester(self, start_semester: int):
        """Setzen des Anfangsdatums der SPO Gültigkeit """
        self._start_semester = start_semester

    def get_end_semester(self):
        """Auslesen des Enddatums der SPO Gültigkeit """
        return self._end_semester

    def set_end_semester(self, end_semester: int):
        """Setzen des Enddatums der SPO Gültigkeit """
        self._end_semester = end_semester

    def get_studycourse(self):
        """Auslesen des Studienganges"""
        return self._studycourse

    def set_studycourse(self, studycourse: int):
        """Setzen des Studiengangs"""
        self._studycourse = studycourse

    def get_modules(self):
        return self._modules

    def set_modules(self, modules: list[int]):
        self._modules = modules

    def append_module(self, module: int):
        self._modules.append(module)

    def remove_module(self, module: int):
        self._modules.remove(module)

    def __str__(self):
        astring = (f'Spo: id: {self.get_id()}, '
                   f'name: {self._name}, title: {self._title}, '
                   f'start Semester: {self.get_start_semester()}, '
                   f'end Semester: {self.get_end_semester()}, '
                   f'studycourse: {self.get_studycourse()}'
                   )
        return astring

    def json(self):
        return json.dumps({
            'name': self.get_name(),
            'title': self.get_title(),
            'start_semester': self.get_start_semester(),
            'end_semester': self.get_end_semester(),
            'studycourse': self.get_studycourse(),
            'modules': self.get_modules()
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
        obj.set_studycourse(dictionary["studycourse"])
        obj.set_modules(dictionary["modules"])
        return obj

    def __eq__(self, other):
        return super().__eq__(other) and self.get_start_semester() == other.get_start_semester() and \
               self.get_end_semester() == other.get_endsemester() and \
               self.get_studycourse() == other.get_studycourse()

    __hash__ = Nbo.NamedBo.__hash__


"""
# Test Script
test = Spo()
print(test.json())
print(hash(test))
"""