"""das Modul "datetime" wird importiert, um das datumsformat für Variablen zu verwenden"""
import datetime
from abc import ABC, abstractmethod
import hashlib


class BusinessObject(ABC):
    _id: int
    _creationdate: datetime.date

    def __init__(self):
        self._id = 0
        self._creationdate = datetime.date.today()  # immer aktuelles Datum

    def set_id(self, value):
        """Setzen der ID."""
        self._id = value

    def get_id(self):
        """Auslesen der ID."""
        return self._id

    def set_creationdate(self, value):
        """Setzen des erstellten Datums"""
        self._creationdate = value

    def get_creationdate(self):
        """Auslesen des erstellten Datums"""
        return self._creationdate

    @abstractmethod
    def json(self):
        """Gibt das Objekt als json aus. Wird von allen BOs überschrieben"""
        pass

    def __eq__(self, other):
        """Vergleicht die einzelnen Attribute auf ihre identität und gibt nur ein Ergebnis, wenn alle übereinstimmen.
        Wird von allen BOs erweitert"""
        return self.get_id() == other.get_id() and self.get_creationdate() == other.get_creationdate()

    def __hash__(self):
        """
        Gibt den Integer aus den Bits des Hash der json vom Objekt aus. Wird von allen BOs geerbt.
        Ermöglicht die referentielle Integrität.
        """

        hashedbo = int.from_bytes(hashlib.sha256(self.json().encode()).digest(), 'big')
        return hashedbo
