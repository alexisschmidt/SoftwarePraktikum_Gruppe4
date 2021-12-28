"""das Modul "datetime" wird importiert um das datumsformat für Variablen zu verwenden"""
import datetime
from abc import ABC, abstractmethod
import hashlib



class BusinessObject(ABC):
    id: int
    creationdate: datetime.date

    def __init__(self):
        self.id = 0
        self.creationdate = datetime.date(1, 1, 1)

    def set_id(self, value):
        """Setzen der ID."""
        self.id = value

    def get_id(self):
        """Auslesen der ID."""
        return self.id

    def set_creationdate(self, value):
        """Setzen des erstellten Datums"""
        self.creationdate = value

    def get_creationDate(self):
        """Auslesen des erstellten Datum"""
        return self.set_creationDate

    def hash(self):
        encoded= self.json().encode()
        hash= hashlib.sha256(encoded)
        return hash.hexdigest()

    @abstractmethod 
    def json():
       pass
