"""das Modul "datetime" wird importiert, um das datumsformat für Variablen zu verwenden"""
import datetime
from abc import ABC, abstractmethod
import json
import hashlib


class BusinessObject(ABC):
    _id: int
    _creationdate: datetime.date

    def __init__(self):
        self._id = 0
        self._creationdate = datetime.date(1, 1, 1)

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
        pass

    def hash(self):
        encoded = self.json().encode()
        hash = hashlib.sha256(encoded)
        return hash.hexdigest()
