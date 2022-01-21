from server.bo import SpoElement as Spe
import json


class Modulepart(Spe.SpoElement):
    __sws: str
    __language: str
    __description: str
    __connection: str
    __literature: str
    __sources: str
    __semester: int
    __professor: int

    def __init__(self):
        super().__init__()
        self.__sws = ""
        self.__language = ""
        self.__description = ""
        self.__connection = ""
        self.__literature = ""
        self.__sources = ""
        self.__semester = 0
        self.__professor = 0

    def get_sws(self):
        """Auslesen der Semesterwochenstunden"""
        return self.__sws

    def set_sws(self, sws):
        """Setzen der Semesterwochenstunden"""
        self.__sws = sws

    def get_language(self):
        """Auslesen der Modulteilsprache"""
        return self.__language

    def set_language(self, language):
        """Setzen der Modulteilsprache"""
        self.__language = language

    def get_description(self):
        """Auslesen der Modulteilbeschreibung"""
        return self.__description

    def set_description(self, description):
        """Setzen der Modulteilbeschreibung"""
        self.__description = description

    def get_connection(self):
        return self.__connection

    def set_connection(self, connection: str):
        """Setzten der Verbindung"""
        self.__connection = connection

    def get_literature(self):
        """Auslesen der Lektüre"""
        return self.__literature

    def set_literature(self, literature):
        """Setzen der Lektüre"""
        self.__literature = literature

    def get_sources(self):
        """Auslesen der Quelle(n)"""
        return self.__sources

    def set_sources(self, sources):
        """Setzen der Quelle(n)"""
        self.__sources = sources

    def get_semester(self):
        """Auslesen des Semesters"""
        return self.__semester

    def set_semester(self, semester):
        """Setzen des Semesters"""
        self.__semester = semester

    def get_professor(self):
        """Auslesen des Professors"""
        return self.__professor

    def set_professor(self, professor):
        """Setzen des Modulverantwortlichen"""
        self.__professor = professor

    def __str__(self):
        astring = (f"Modulepart:"
                   f"id: {self.get_id()}, "
                   f"name: {self._name}, "
                   f"title: {self._title}, "
                   f"edvnr: {self._edvnr}, "
                   f"ects: {self._ects}, "
                   f"workload: {self.workload}, "
                   f"SWS: {self.__sws}, "
                   f"language: {self.__language}, "
                   f"description: {self.__description}, "
                   f"connection: {self.__connection}, "
                   f"literature: {self.__literature}, "
                   f"sources: {self.__sources}, "
                   f"semester: {self.__semester}, "
                   f"professor: {self.__professor}"
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
