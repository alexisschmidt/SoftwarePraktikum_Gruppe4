from server.bo.NamedBo import NamedBo

class Spo (NamedBo):
    def __init__(self):
        super.__init__()
        self.start_date = ""    # Anfangsdatum der SPO Gültigkeit
        self.end_date = ""      # Enddatum der SPO Gültigkeit

    def get_start_date(self):
        """Auslesen des Anfangsdatums der SPO Gültigkeit """
        return self.start_date

    def set_start_date(self, start):
        """Bestimmen des Anfangsdatums der SPO Gültigkeit """
        self.start_date = start


    def get_end_date(self):
        """Auslesen des Enddatums der SPO Gültigkeit """
        return self.end_date

    def set_end_date(self, end):
        """Bestimmen des Enddatums der SPO Gültigkeit """
        self.end_date = end

        