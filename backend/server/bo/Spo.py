from server.bo.NamedBo import NamedBo
"""Die "date" Klasse aus dem Modul "datetime" wird importiert um das datumsformat für Variablen zu verwenden"""
from datetime import date

class Spo (NamedBo):
    
    def __init__(self):
        super.__init__()
        self.start_date = datetime.date(1, 1, 1)    # Anfangsdatum der SPO Gültigkeit
        self.end_date = datetime.date(1, 1, 1)  # Enddatum der SPO Gültigkeit

    def get_start_date(self):
        """Auslesen des Anfangsdatums der SPO Gültigkeit """
        return self.start_date

    def set_start_date(self, year, month, day):
        """Bestimmen des Anfangsdatums der SPO Gültigkeit """
        self.start_date = datetime.date(year, month, day)


    def get_end_date(self):
        """Auslesen des Enddatums der SPO Gültigkeit """
        return self.end_date

    def set_end_date(self, year, month, day):
        """Bestimmen des Enddatums der SPO Gültigkeit """
        self.end_date = datetime.date(year, month, day)

        