from abc import ABC
from server.bo import NamedBo as nbo


class SpoElement (nbo.NamedBo, ABC):
    edvnr: int
    ects: int
    workload: str

    def __init__(self):
        super().__init__()
        self.edvnr = 0      # EDV Nummer des Spo Elements
        self.ects = 0       # ECTS des Spo Elements
        self.workload = ""  # Arbeitsaufwand in Stunden des Spo Elements

    def get_edvnr(self):
        """Auslesen der EDV Nummer"""
        return self.edvnr

    def set_edvnr(self, edvnr):
        """Setzen der EDV Nummer"""
        self.edvnr = edvnr

    def get_ects(self):
        """Auslesen der ECTS"""
        return self.ects

    def set_ects(self, ects):
        """Setzen der ECTS"""
        self.ects = ects

    def get_workload(self):
        """Auslesen des Arbeitsaufwands"""
        return self.workload

    def set_workload(self, workload):
        """Setzen des Arbeitsaufwands"""
        self.workload = workload

    def __eq__(self, other):
        return super().__eq__() and\
               self.get_edvnr() == other.get_name() and\
               self.get_ects() == other.get_title() and\
               self.get_workload() == other.get_workload()

    __hash__ = nbo.NamedBo.__hash__
