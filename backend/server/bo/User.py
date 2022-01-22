from server.bo import Businessobject as Bo
import json

"""
Realisierung einer exemplarischen Benutzerklasse.

Aus Gründen der Vereinfachung besitzt der Student in diesem Demonstrator
lediglich einen einfachen Namen, eine E_Mail-Adresse sowie eine außerhalb
unseres Systems verwaltete User ID (z.B. die Google ID).
"""


class User(Bo.BusinessObject):
    __firstname: str
    __lastname: str
    __email: str
    __google_user_id: str
    __isadmin: int

    def __init__(self):
        super().__init__()
        self.__firstname = ""       # Der Vorname des Nutzers
        self.__lastname = ""        # Der Nachname des Nutzers
        self.__email = ""           # Die E-Mail des Nutzers
        self.__google_user_id = ""  # Die Google ID des Nutzers
        self.__isadmin = 0

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

    def get_google_user_id(self):
        """Auslesen der Google User ID"""
        return self.__google_user_id

    def set_google_user_id(self, google_user_id):
        """Setzen der Google User ID"""
        self.__google_user_id = google_user_id

    def get_isadmin(self):
        return self.__isadmin

    def set_isadmin(self, isadmin):
        self.__isadmin = isadmin

    def __str__(self):
        return f"User: \
               id: {self.get_id()}, \
               firstname: {self.__firstname}, \
               lastname: {self.__lastname}, \
               email: {self.__email}, \
               google_user_id: {self.__google_user_id}, \
               isadmin: {self.__isadmin}"

    def json(self):
        return json.dumps({
            'id': self.get_id(),
            'firstname': self.get_firstname(),
            'lastname': self.get_lastname(),
            'email': self.get_email(),
            'google_user_id': self.get_google_user_id(),
            'isadmin': self.get_isadmin()
            })
    
    @staticmethod
    def from_dict(dictionary=dict()):
        """Umwandeln eines Python dict() in einen User()."""
        print(dictionary)
        obj = User()
        obj.set_id(dictionary["id"])  # Teil von BusinessObject!
        obj.set_firstname(dictionary["firstname"])
        obj.set_lastname(dictionary["lastname"])
        obj.set_email(dictionary["email"])
        obj.set_google_user_id(dictionary["google_user_id"])
        obj.set_isadmin(["isadmin"])
        return obj

    def __eq__(self, other):
        return super().__eq__(other) and self.get_firstname() == other.get_name() and\
               self.get_lastname() == other.get_lastname() and\
               self.get_email() == other.get_email()

    __hash__ = Bo.BusinessObject.__hash__


"""
test = User()
print(test)
print(test.json())
print(test.hash())
"""




    
