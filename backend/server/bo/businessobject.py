from abc import ABC, abstractmethod


class BusinessObject(ABC):

    def __init__(self):
        self.id = 0

    def set_id(self, value):
        """Setzen der ID."""
        self.id = value

    def get_id(self):
        """Auslesen der ID."""
        return self.id

    def set_creationDate(self, value):
        """setzung der erstellten Datum"""
        self.creationdate = value

    def get_creationDate(self):
        """Auslesen des erstellten Datum"""
        return self.set_creationDate