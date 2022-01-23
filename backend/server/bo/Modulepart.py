from server.bo import SpoElement as Spe
import json


class Modulepart(Spe.SpoElement):
    _sws: str
    _language: str
    _description: str
    _connection: str
    _literature: str
    _sources: str
    _semester: int
    _professor: int

    def __init__(self):
        super().__init__()
        self._sws = ""
        self._language = ""
        self._description = ""
        self._connection = ""
        self._literature = ""
        self._sources = ""
        self._semester = 0
        self._professor = 0

    def get_sws(self):
        """Auslesen der Semesterwochenstunden"""
        return self._sws

    def set_sws(self, sws):
        """Setzen der Semesterwochenstunden"""
        self._sws = sws

    def get_language(self):
        """Auslesen der Modulteilsprache"""
        return self._language

    def set_language(self, language):
        """Setzen der Modulteilsprache"""
        self._language = language

    def get_description(self):
        """Auslesen der Modulteilbeschreibung"""
        return self._description

    def set_description(self, description):
        """Setzen der Modulteilbeschreibung"""
        self._description = description

    def get_connection(self):
        return self._connection

    def set_connection(self, connection: str):
        """Setzten der Verbindung"""
        self._connection = connection

    def get_literature(self):
        """Auslesen der Lektüre"""
        return self._literature

    def set_literature(self, literature):
        """Setzen der Lektüre"""
        self._literature = literature

    def get_sources(self):
        """Auslesen der Quelle(n)"""
        return self._sources

    def set_sources(self, sources):
        """Setzen der Quelle(n)"""
        self._sources = sources

    def get_semester(self):
        """Auslesen des Semesters"""
        return self._semester

    def set_semester(self, semester):
        """Setzen des Semesters"""
        self._semester = semester

    def get_professor(self):
        """Auslesen des Professors"""
        return self._professor

    def set_professor(self, professor):
        """Setzen des Modulverantwortlichen"""
        self._professor = professor

    def __str__(self):
        astring = (f"Modulepart:"
                   f"id: {self.get_id()}, "
                   f"name: {self._name}, "
                   f"title: {self._title}, "
                   f"edvnr: {self._edvnr}, "
                   f"ects: {self._ects}, "
                   f"workload: {self.workload}, "
                   f"SWS: {self._sws}, "
                   f"language: {self._language}, "
                   f"description: {self._description}, "
                   f"connection: {self._connection}, "
                   f"literature: {self._literature}, "
                   f"sources: {self._sources}, "
                   f"semester: {self._semester}, "
                   f"professor: {self._professor}"
                   )
        return astring

    def json(self):
        return json.dumps({
            'id': self.get_id(),
            'sws': self.get_sws(),
            'language': self.get_language(),
            'edvnr': self.get_edvnr(),
            'ects': self.get_ects(),
            'workload': self.get_workload(),
            'description': self.get_description(),
            'connection': self.get_connection(),
            'literature': self.get_literature(),
            'sources': self.get_sources(),
            'semester': self.get_semester(),
            'professor': self.get_professor()
        })

    @staticmethod
    def from_dict(dictionary=dict()):
        """Umwandeln eines Python dict() in ein Modulepart()."""
        obj = Modulepart()
        obj.set_id(dictionary["id"])  # Teil von BusinessObject!
        obj.set_sws(dictionary["sws"])  # Teil von NamedBo!
        obj.set_language(dictionary["language"])  # Teil von NamedBo!
        obj.set_edvnr(dictionary["edvnr"])  # Teil von SpoElement!
        obj.set_ects(dictionary["ects"])  # Teil von SpoElement!
        obj.set_workload(dictionary["workload"])  # Teil von SpoElement!
        obj.set_description(dictionary["description"])
        obj.set_connection(dictionary["connection"])
        obj.set_literature(dictionary["literature"])
        obj.set_sources(dictionary["sources"])
        obj.set_semester(dictionary["semester"])
        obj.set_professor(dictionary["professor"])
        return obj

    __hash__ = Spe.__hash__()

"""
# Test Script

test = Modulepart()
person1 = Person()
person1.set_id(69)
test.set_professor(person1)
print(test)
print(test.json())
print(hash(test))
"""
