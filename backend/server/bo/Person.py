from server.bo import Businessobject as Bo
import json


class Person(Bo.BusinessObject):
    _firstname: str
    _lastname: str
    _email: str

    def __init__(self):
        super().__init__()
        self._firstname = ""  # Der Vorname der Person
        self._lastname = ""  # Der Nachname der Person
        self._email = ""  # email der Person

    # Auslesen / des Vor-/nachnamens und Email.

    def get_firstname(self):
        """Auslesen des Vornamens"""
        return self._firstname

    def set_firstname(self, firstname):
        """Setzen des Vornamens"""
        self._firstname = firstname

    def get_lastname(self):
        """Auslesen des Nachnamens"""
        return self._lastname

    def set_lastname(self, lastname):
        """Setzen des Nachnamens"""
        self._lastname = lastname

    def get_email(self):
        """Auslesen der E-Mail"""
        return self._email

    def set_email(self, email):
        """Setzen der E-Mail"""
        self._email = email

    def __str__(self):
        astring = (f"Person: "
                   f"id: {self.get_id()}, "
                   f"firstname: {self._firstname}, "
                   f"lastname: {self._lastname}, "
                   f"email: {self._email}"
                   )
        return astring

    def json(self):
        return json.dumps({
            'id': self.get_id(),
            'firstname': self.get_firstname(),
            'lastname': self.get_lastname(),
            'email': self.get_email()
        })

    @staticmethod
    def from_dict(dictionary=dict()):
        """Umwandeln eines Python dict() in eine Person()."""
        obj = Person()
        obj.set_id(dictionary["id"])  # Teil von BusinessObject!
        obj.set_firstname(dictionary["firstname"])
        obj.set_lastname(dictionary["lastname"])
        obj.set_email(dictionary["email"])
        return obj

    def __eq__(self, other):
        return super().__eq__(other) and self.get_firstname() == other.get_firstname() and \
               self.get_lastname() == other.get_lastname() and \
               self.get_email() == other.get_email()

    __hash__ = Bo.BusinessObject.__hash__
