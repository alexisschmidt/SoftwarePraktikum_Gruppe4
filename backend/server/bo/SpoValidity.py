import json

from server.bo import Businessobject as Bo


class SpoValidity(Bo.BusinessObject):
    _spo: int
    _semester: int
    _startsem: bool
    _endsem: bool

    def __init__(self, spo=0, semester=0, startsem=False, endsem=False):
        super().__init__()
        self._spo = spo
        self._semester = semester
        self._startsem = startsem
        self._endsem = endsem

    def get_spo(self):
        return self._spo

    def set_spo(self, spohash):
        self._spo = spohash

    def get_semester(self):
        return self._semester

    def set_semester(self, semesterhash):
        self._semester = semesterhash

    def get_startsem(self):
        return self._startsem

    def set_startsem(self, startsem):
        self._startsem = startsem

    def get_endsem(self):
        return self._endsem

    def set_endsem(self, endsem):
        self._endsem = endsem

    def json(self):
        return json.dumps({
            'id': self.get_id(),
            'spo': self.get_spo(),
            'semester': self.get_semester(),
            'startsem': self.get_startsem(),
            'endsem': self.get_endsem()
        })

    @staticmethod
    def from_dict(dictionary=dict()):
        """Umwandeln eines Python dict() in eine Validity()."""
        obj = SpoValidity()
        obj.set_id(dictionary["id"])
        obj.set_spo(dictionary["spo"])
        obj.set_semester(dictionary["semester"])
        obj.set_startsem(dictionary["startsem"])
        obj.set_endsem(dictionary["endsem"])
        return obj

    def __eq__(self, other):
        return super().__eq__(other) and \
               self.get_spo() == other.get_spo() and \
               self.get_semester() == other.get_semester()

    __hash__ = Bo.BusinessObject.__hash__
