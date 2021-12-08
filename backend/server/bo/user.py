from server.bo.BusinessObject import BusinessObject


"""Realisierung einer exemplarischen Benutzerklasse.

    Aus Gründen der Vereinfachung besitzt der Student in diesem Demonstrator
    lediglich einen einfachen Namen, eine E_Mail-Adresse sowie eine außerhalb
    unseres Systems verwaltete User ID (z.B. die Google ID). """
class User(BusinessObject):
    def __init__(self):
        super.__init__()
    
        self.__firstname = "" # Der Name des Nutzers
        self.__lastname = ""
        self.__email = "" # email des Nutzers

#Auslesen / des Vor/nachnamens und Email.

    def get_firstname(self):
        return self.__firstname

    def set_firstname(self, value):
        self.__firstname


    def get_lastname(self):
        return self.__lastname

    def set_lastname(self, value):
        self.__lastname

    def get_email(self):
        return self.__email

    def set_email(self, value):
        self.__email


    def __str__(self):
        return "User: {}, {}, {}, {}".format(self.get_id(), self.__firstname, self.__lastname, self.__email,)   

    
    @staticmethod
    def from_dict(dictionary=dict()):
        """Umwandeln eines Python dict() in einen User()."""
        obj = User()
        obj.set_id(dictionary["id"])  # eigentlich Teil von BusinessObject !
        obj.set_firstname(dictionary["firstname"])
        obj.set_lastname(dictionary["lastname"])
        obj.set_email(dictionary["email"])
        return obj




    
