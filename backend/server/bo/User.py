from server.bo import Businessobject as Bo
import json

"""
Realisierung einer exemplarischen Benutzerklasse.

Aus Gründen der Vereinfachung besitzt der Student in diesem Demonstrator
lediglich einen einfachen Namen, eine E_Mail-Adresse sowie eine außerhalb
unseres Systems verwaltete User ID (z.B. die Google ID).
"""


class User(Bo.BusinessObject):
    _firstname: str
    _lastname: str
    _email: str
    _google_user_id: str
    _isadmin: int
    _spo: int

    def __init__(self):
        super().__init__()
        self._firstname = ""       # Der Vorname des Nutzers
        self._lastname = ""        # Der Nachname des Nutzers
        self._email = ""           # Die E-Mail des Nutzers
        self._google_user_id = ""  # Die Google ID des Nutzers
        self._isadmin = 0          # Adminstatus des Users
        self._spo = 0              # Die SPO, falls der User ein Student ist

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

    def get_google_user_id(self):
        """Auslesen der Google User ID"""
        return self._google_user_id

    def set_google_user_id(self, google_user_id):
        """Setzen der Google User ID"""
        self._google_user_id = google_user_id

    def get_isadmin(self):
        return self._isadmin

    def set_isadmin(self, isadmin):
        self._isadmin = isadmin

    def get_spo(self):
        return self._spo

    def set_spo(self, spohash):
        self._spo = spohash

    def _str_(self):
        return f"User: \
               id: {self.get_id()}, \
               firstname: {self._firstname}, \
               lastname: {self._lastname}, \
               email: {self._email}, \
               google_user_id: {self._google_user_id}, \
               isadmin: {self._isadmin}"

    def json(self):
        return json.dumps({
            'firstname':        self.get_firstname(),
            'lastname':         self.get_lastname(),
            'email':            self.get_email(),
            'google_user_id':   self.get_google_user_id(),
            'isadmin':          self.get_isadmin(),
            'spo':              self.get_spo()
            })
    
    @staticmethod
    def from_dict(dictionary=dict()):
        """Umwandeln eines Python dict() in einen User()."""
        obj = User()
        obj.set_id(dictionary["id"])  # Teil von BusinessObject!
        obj.set_firstname(dictionary["firstname"])
        obj.set_lastname(dictionary["lastname"])
        obj.set_email(dictionary["email"])
        obj.set_google_user_id(dictionary["google_user_id"])
        obj.set_isadmin(dictionary["isadmin"])
        obj.set_spo(dictionary["spo"])
        

        return obj

    def __eq__(self, other):
        return super().__eq__(other) and \
               self.get_firstname() == other.get_firstname() and \
               self.get_lastname() == other.get_lastname() and \
               self.get_email() == other.get_email() and \
               self.get_google_user_id() == other.get_google_user_id() and \
               self.get_isadmin() == other.get_isadmin() and \
               self.get_spo() == other.get_spo()

    __hash__ = Bo.BusinessObject.__hash__


"""
test = User()
print(test)
print(test.json())
print(test.hash())
"""




    
