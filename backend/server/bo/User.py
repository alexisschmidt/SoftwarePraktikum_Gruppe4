from server.bo import Businessobject as bo


"""Realisierung einer exemplarischen Benutzerklasse.

    Aus Gründen der Vereinfachung besitzt der Student in diesem Demonstrator
    lediglich einen einfachen Namen, eine E_Mail-Adresse sowie eine außerhalb
    unseres Systems verwaltete User ID (z.B. die Google ID). """


class User(bo.BusinessObject):
    __firstname: str
    __lastname: str
    __email: str

    def __init__(self):
        super().__init__()
        self.__firstname = ""   # Der Vorname des Nutzers
        self.__lastname = ""    # Der Nachname des Nutzers
        self.__email = ""   # Die E-Mail des Nutzers

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
        return "User: {}, {}, {}, {}".format(self.get_id(), self.__firstname, self.__lastname, self.__email,)
    
    @staticmethod
    def from_dict(dictionary=dict()):
        """Umwandeln eines Python dict() in einen User()."""
        print(dictionary)
        obj = User()
        obj.set_id(dictionary["id"])  # Teil von BusinessObject!
        obj.set_firstname(dictionary["firstname"])
        obj.set_lastname(dictionary["lastname"])
        obj.set_email(dictionary["email"])
        return obj






    
