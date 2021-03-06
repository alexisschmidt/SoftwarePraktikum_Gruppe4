from abc import ABC
from server.bo import NamedBo as Nbo


class SpoElement(Nbo.NamedBo, ABC):
    _edvnr: int
    _ects: int
    _workload: str

    def __init__(self):
        super().__init__()
        self._edvnr = 0     # EDV Nummer des Spo Elements
        self._ects = 0      # ECTS des Spo Elements
        self._workload = ""  # Arbeitsaufwand in Stunden des Spo Elements

    def get_edvnr(self):
        """Auslesen der EDV Nummer"""
        return self._edvnr

    def set_edvnr(self, edvnr):
        """Setzen der EDV Nummer"""
        self._edvnr = edvnr

    def get_ects(self):
        """Auslesen der ECTS"""
        return self._ects

    def set_ects(self, ects):
        """Setzen der ECTS"""
        self._ects = ects

    def get_workload(self):
        """Auslesen des Arbeitsaufwands"""
        return self._workload

    def set_workload(self, workload):
        """Setzen des Arbeitsaufwands"""
        self._workload = workload

    def __eq__(self, other):
        return super().__eq__() and \
               self.get_edvnr() == other.get_edvnr() and \
               self.get_ects() == other.get_ects() and \
               self.get_workload() == other.get_workload()

    __hash__ = Nbo.NamedBo.__hash__
