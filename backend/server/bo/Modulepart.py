from server.bo.NamedBo import SpoElement
from server.bo.Person import Person


class Modulepart (SpoElement):
    __SWS: str
    __language: str
    __description: str
    __connection: str
    __literature: str
    __sources: str
    __semester: str
    _professor: Person

    def __init__(self):
        super().__init__()
        self.__SWS = ""
        self.__language = ""
        self.__description = ""
        self.__connection = ""
        self.__literature = ""
        self.__sources = ""
        self.__semester = ""
        self._professor = Person()

        # Auslesen

    def get_sws(self):
        """Auslesen der Semesterwochenstunden"""
        return self.__SWS

    def set_sws(self, sws):
        """Setzen der Semesterwochenstunden"""
        self.__SWS = sws

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
        """Auslesen der Modulverknüpfung(en)"""
        return self.__connection

    def set_connection(self, value):
        """Setzen der Modulverknüpfung(en)"""
        self.__connection = value

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

    def __str__(self):
        return "Modulepart: {}, {}, {}, {}, {}, {}, {}, {}".format(
            self.get_id(),
            self.__SWS,
            self.__language,
            self.__description,
            self.__connection,
            self.__literature,
            self.__sources,
            self.__semester)

    @staticmethod
    def from_dict(dictionary=dict()):
        """Umwandeln eines Python dict() in ein Modulepart()."""
        obj = Modulepart()
        obj.set_id(dictionary["id"])                    # Teil von BusinessObject!
        obj.set_sws(dictionary["SWS"])                  # Teil von NamedBo!
        obj.set_language(dictionary["language"])        # Teil von NamedBo!
        obj.set_edvnr(dictionary["edvnr"])              # Teil von SPOElement
        obj.set_ects(dictionary["ects"])                # Teil von SPOElement
        obj.set_workload(dictionary["workload"])        # Teil von SPOElement
        obj.set_description(dictionary["description"])
        obj.set_connection(dictionary["connection"])
        obj.set_literature(dictionary["literature"])
        obj.set_sources(dictionary["sources"])
        obj.set_semester(dictionary["semester"])
        return obj
