from server.bo import NamedBo as nbo
"""das Modul "datetime" wird importiert um das datumsformat für Variablen zu verwenden"""
from server.bo.Semester import Semester
from server.bo.StudyCourse import StudyCourse
import json


class Spo (nbo.NamedBo):
    _start_semester: Semester
    _end_semester: Semester
    _studycourse_id: StudyCourse

    def __init__(self):
        super().__init__()
        self._start_semester = Semester()   # Anfangssemester der SPO Gültigkeit
        self._end_semester = Semester()     # Endsemester der SPO Gültigkeit
        self._studycourse_id = StudyCourse()

    def get_start_semester(self):
        """Auslesen des Anfangsdatums der SPO Gültigkeit """
        return self._start_semester

    def set_start_semester(self, start_semester):
        """Setzen des Anfangsdatums der SPO Gültigkeit """
        self._start_semester = start_semester

    def get_end_semester(self):
        """Auslesen des Enddatums der SPO Gültigkeit """
        return self._end_semester

    def set_end_semester(self, end_semester):
        """Setzen des Enddatums der SPO Gültigkeit """
        self._end_semester = end_semester

    def get_studycourse_id(self):
        """Auslesen des Studienganges"""
        return self._studycourse_id

    def set_studycourse_id(self, studycourseid):
        """Setzen des Studiengangs"""
        self._studycourse_id = studycourseid

    def __str__(self):
        return "Spo: id: {}, name: {}, title: {}, start Semester: {}, end Semester: {}, studycourse: {}".format(
            self.get_id(),
            self._name,
            self._title,
            Semester.get_name(self.get_start_semester()),
            Semester.get_name(self.get_end_semester()),
            StudyCourse.get_name(self.get_studycourse_id())
            )

    def json(self):
        # modulehash = []
        # for modulepart in self.__moduleparts:
        # modulehash.append(modulepart.hash())
        return json.dumps({
            'id': self.get_id(),
            'name': self.get_name(),
            'title': self.get_title(),
            'start_semester': Semester.hash(self.get_start_semester()),
            'end_semester': Semester.hash(self.get_end_semester()),
            'studycourse_id': StudyCourse.hash(self.get_studycourse_id())
            })

    @staticmethod
    def from_dict(dictionary=dict()):
        """Umwandeln eines Python dict() in eine Spo()."""
        obj = Spo()
        obj.set_id(dictionary["id"])  # Teil von BusinessObject!
        obj.set_name(dictionary["name"])    # Teil von NamedBo!
        obj.set_title(dictionary["title"])  # Teil von NamedBo!
        obj.set_start_semester(dictionary["start_semester"])
        obj.set_end_semester(dictionary["end_semester"])
        obj.set_studycourse_id(dictionary["studycourse_id"])
        return obj


"""
    Test Script

    test = Spo()
    print(test)
    print(test.json())
    print(test.hash())
"""