from server.bo.NamedBo import NamedBo
from server.bo.SpoElement import SpoElement

class Module (NamedBo):
    def __init__(self):
        super.__init__()

        self.__type = ""
        self.__requirement = ""
        self.__outcome = ""
        self.__examtype = ""
        self.__instructor = ""


# Auslesen

    def get_type(self):
        return self.__type


    def set_type(self, value):
        self.__type = value


    def get_requirement(self):
        return self.__requirement


    def set_requirement(self, value):
        self.__requirement = value


    def get_outcome(self):
        return self.__outcome


    def set_outcome(self, value):
        self.__outcome = value


    def get_examtype(self):
        return self.__examtype

    def set_examtype(self, value):
        self.__examtype = value


    def get_instructor(self):
        return self.__instructor

    def set_instructor(self, value):
        self.__instructor = value





    def __str__(self):
        return "Module: {}, {}, {}, {}, {}".format(

        self.get_id(),
        self.__type,
        self.__requirement,
        self.__outcome,
        self.__examtype,
        self.__instructor)


@staticmethod
def from_dict(dictionary=dict()):
    """Umwandeln eines Python dict() in ein Module()."""
    obj = Module()
    obj.set_id(dictionary["id"])  # eigentlich Teil von BusinessObject !
    obj.set_type(dictionary["type"])
    obj.set_requirement(dictionary["requirement"])
    obj.set_outcome(dictionary["outcome"])
    obj.set_examtype(dictionary["examtype"])
    obj.set_instructor(dictionary["instructor"])
    return obj

