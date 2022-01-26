from server.bo import NamedBo as Nbo
import json


class StudyCourse (Nbo.NamedBo):
    def __init__(self):
        super().__init__()

    def __str__(self):
        return f"Semester: id: {self.get_id()}, name: {self._name}, title: {self._title}"

    def json(self):
        return json.dumps({
            'id': self.get_id(),
            'name': self.get_name(),
            'title': self.get_title()
            })

    @staticmethod
    def from_dict(dictionary=dict()):
        """Umwandeln eines Python dict() in einen StudyCourse()."""
        obj = StudyCourse()
        obj.set_id(dictionary["id"])
        obj.set_name(dictionary["name"])
        obj.set_title(dictionary["title"])
        return obj

    def __eq__(self, other):
        return super().__eq__(other)

    __hash__ = Nbo.NamedBo.__hash__
