from abc import ABC
from server.bo import Businessobject as bo


class NamedBo(bo.BusinessObject, ABC):
    _name: str
    _title: str

    def __init__(self):
        super().__init__()
        self._name = ""
        self._title = ""

    def get_name(self):
        """Auslesen des Namens"""
        return self._name

    def set_name(self, name):
        """Setzen des Namens"""
        self._name = name

    def get_title(self):
        """Auslesen des Namens"""
        return self._title

    def set_title(self, title):
        """Setzen des Titels"""
        self._title = title

    def __eq__(self, other):
        return super().__eq__() and \
               self.get_name() == other.get_name() and \
               self.get_title() == other.get_title()

    __hash__ = bo.BusinessObject.__hash__
