from server.bo import Businessobject as bo
import json


class Person (bo.BusinessObject):
    __firstname: str
    __lastname: str
    __email: str

    def __init__(self):
        super().__init__()
        self.__firstname = ""   # Der Vorname der Person
        self.__lastname = ""    # Der Nachname der Person
        self.__email = ""       # email der Person

# Auslesen / des Vor-/nachnamens und Email.

    def get_firstname(self):
        """Auslesen des Vornamens"""
        return self.__firstname

    def set_firstname(self, firstname):
        """Setzen des Vornamens"""
        self.__firstname = firstname

    def get_lastname(self):
        """Auslesen des Nachnamens"""
        return self.__lastname

    def set_lastname(self, lastname):
        """Setzen des Nachnamens"""
        self.__lastname = lastname

    def get_email(self):
        """Auslesen der E-Mail"""
        return self.__email

    def set_email(self, email):
        """Setzen der E-Mail"""
        self.__email = email

    def __str__(self):
        return f"Person: \
               id: {self.get_id()}, \
               firstname: {self.__firstname}, \
               lastname: {self.__lastname}, \
               email: {self.__email}"

    def json(self):
        return json.dumps({
            'id': self.get_id(),
            'name': self.get_name(),
            'title': self.get_title(),
            'firstname': self.get_firstname(),
            'lastname': self.get_lastname(),
            'email': self.get_email()
            })

    @staticmethod
    def from_dict(dictionary=dict()):
        """Umwandeln eines Python dict() in eine Person()."""
        obj = Person()
        obj.set_id(dictionary["id"])                # Teil von BusinessObject!
        obj.set_name(dictionary["name"])            # Teil von NamedBo!
        obj.set_title(dictionary["title"])          # Teil von NamedBo!
        obj.set_firstname(dictionary["firstname"])
        obj.set_lastname(dictionary["lastname"])
        obj.set_email(dictionary["email"])
        return obj

    def __eq__(self, other):
        return super().__eq__(other) and self.get_firstname() == other.get_name() and \
               self.get_lastname() == other.get_lastname() and \
               self.get_email() == other.get_email()

    __hash__ = nbo.NamedBo.__hash__
