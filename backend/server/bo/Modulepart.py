from server.bo.NamedBo import NamedBo
from server.bo.SpoElement import SpoElement

class Modulepart (NamedBo):
    def __init__(self):
        super.__init__()

        self.__SWS = ""
        self.__language = ""
        self.__description = ""
        self.__connection = ""
        self.__literature = ""
        self.__sources = ""
        self.__semester = ""

        # Auslesen

    def get_SWS(self):
        return self.__SWS

    def set_SWS(self, value):
        self.__SWS = value

    def get_language(self):
        return self.__language

    def set_language(self, value):
        self.__language = value

    def get_description(self):
        return self.__description

    def set_description(self, value):
        self.__description = value

    def get_connection(self):
        return self.__connection

    def set_connection(self, value):
        self.__connection = value

    def get_literature(self):
        return self.__literature

    def set_literature(self, value):
        self.__literature = value

    def get_sources(self):
        return self.__sources

    def set_sources(self, value):
        self.__sources = value


    def get_semester(self):
        return self.__semester

    def set_semester(self, value):
        self.__semester = value

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
        obj.set_id(dictionary["id"])
        obj.set_SWS(dictionary["SWS"])
        obj.set_language(dictionary["language"])
        obj.set_description(dictionary["description"])
        obj.set_connection(dictionary["connection"])
        obj.set_literature(dictionary["literature"])
        obj.set_sources(dictionary["sources"])
        obj.set_semester(dictionary["semester"])
        return obj