from server.bo import SpoElement as spe
from server.bo.Person import Person
import json


class Modulepart (spe.SpoElement):
    __sws: str
    __language: str
    __description: str
    __connection: dict
    __literature: str
    __sources: str
    __semester: int
    _professor: dict

    def __init__(self):
        super().__init__()
        self.__sws = ""
        self.__language = ""
        self.__description = ""
        self.__connection = {}
        self.__literature = ""
        self.__sources = ""
        self.__semester = 1
        self._professor = {}

        # Auslesen

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

    def set_connection(self, connection):
        if isinstance(connection, list):
            for i in connection:
                if isinstance(i, Modulepart):
                    self.__connection.update({hash(i): i.get_id()})

    def append_connection(self, other):
        if isinstance(other, Modulepart):
            self.__connection.update({hash(other): other.get_id()})

    def remove_connection(self, other):
        if isinstance(other, Modulepart):
            self.__connection.pop(hash(other))

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
        return self._professor

    def set_professor(self, professor):
        """Setzen des Modulverantwortlichen"""
        if isinstance(professor, Person):
            self._professor = {hash(professor): professor.get_id()}

    def __str__(self):
        return "Modulepart: id: {}, name: {}, title: {}, edvnr: {}, ects: {}, workload: {}, SWS: {}, language: {}," \
               "description: {}, connection: {}, literature: {}, sources: {}, semester: {}, professor: {}".format(
                self.get_id(),
                self._name,
                self._title,
                self._edvnr,
                self.ects,
                self.workload,
                self.__sws,
                self.__language,
                self.__description,
                self.__connection,
                self.__literature,
                self.__sources,
                self.__semester,
                self._professor
                )

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
        obj.set_id(dictionary["id"])                    # Teil von BusinessObject!
        obj.set_sws(dictionary["sws"])                  # Teil von NamedBo!
        obj.set_language(dictionary["language"])        # Teil von NamedBo!
        obj.set_edvnr(dictionary["edvnr"])              # Teil von SpoElement!
        obj.set_ects(dictionary["ects"])                # Teil von SpoElement!
        obj.set_workload(dictionary["workload"])        # Teil von SpoElement!
        obj.set_description(dictionary["description"])
        obj.set_connection(dictionary["connection"])
        obj.set_literature(dictionary["literature"])
        obj.set_sources(dictionary["sources"])
        obj.set_semester(dictionary["semester"])
        obj.set_professor(dictionary["professor"])
        return obj


"""
#Test Script

test = Modulepart()
person1 = Person()
person1.set_lastname("testname")
test.set_professor(person1)
print(test)
print(test.json())
print(hash(test))
"""
