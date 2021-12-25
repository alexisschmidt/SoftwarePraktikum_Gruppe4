from abc import ABC
"""das Modul "datetime" wird importiert um das datumsformat für Variablen zu verwenden"""
import datetime


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

    def get_creationdate(self):
        """Auslesen des erstellten Datums"""
        return self.set_creationdate
