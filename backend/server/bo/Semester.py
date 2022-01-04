from server.bo import NamedBo as nbo
import json


class Semester(nbo.NamedBo):
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
        """Umwandeln eines Python dict() in ein Semester()."""
        obj = Semester()
        obj.set_id(dictionary["id"])
        obj.set_name(dictionary["name"])
        obj.set_title(dictionary["title"])
        return obj

    __eq__ = nbo.NamedBo.__eq__

    __hash__ = nbo.NamedBo.__hash__
