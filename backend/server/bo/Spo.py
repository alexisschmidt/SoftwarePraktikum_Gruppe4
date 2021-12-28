from server.bo import NamedBo as nbo
"""das Modul "datetime" wird importiert um das datumsformat für Variablen zu verwenden"""
import datetime
import json


class Spo (nbo.NamedBo):
    start_date: datetime.date
    end_date: datetime.date

    def __init__(self):
        super().__init__()
        self._start_date = datetime.date(1, 1, 1)    # Anfangsdatum der SPO Gültigkeit
        self._end_date = datetime.date(1, 1, 1)  # Enddatum der SPO Gültigkeit

    def get_start_date(self):
        """Auslesen des Anfangsdatums der SPO Gültigkeit """
        return self.start_date

    def set_start_date(self, year, month, day):
        """Setzen des Anfangsdatums der SPO Gültigkeit """
        self.start_date = datetime.date(year, month, day)

    def get_end_date(self):
        """Auslesen des Enddatums der SPO Gültigkeit """
        return self.end_date

    def set_end_date(self, year, month, day):
        """Setzen des Enddatums der SPO Gültigkeit """
        self.end_date = datetime.date(year, month, day)


    def json(self):
            modulehash=[]
            for modulepart in self.__moduleparts:
                modulehash.append(modulepart.hash())

            return json.dumps({
                'id': self.get_id(),
                'name': self.get_name(),
                'title': self.get_title(),
                'start_date': self.get_start_date(),
                'end_date': self.get_end_date(),
                })


    @staticmethod
    def from_dict(dictionary=dict()):
        """Umwandeln eines Python dict() in eine Spo()."""
        obj = Spo()
        obj.set_id(dictionary["id"])  # Teil von BusinessObject!
        obj.set_name(dictionary["name"])    # Teil von NamedBo!
        obj.set_title(dictionary["title"])  # Teil von NamedBo!
        obj.set_start_date(dictionary["year, month, day"], dictionary["month"], dictionary["day"])
        obj.set_end_date(dictionary["year, month, day"], dictionary["month"], dictionary["day"])
        return obj
