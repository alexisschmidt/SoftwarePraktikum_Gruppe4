from abc import ABC, abstractmethod
import datetime

class BusinessObject(ABC):

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
        """setzung der erstellten Datum"""
        self.creationdate = value

    def get_creationdate(self):
        """Auslesen des erstellten Datum"""
        return self.set_creationdate
