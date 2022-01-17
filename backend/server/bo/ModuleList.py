from server.bo import Businessobject as bo
import json


class ModuleList(bo.BusinessObject):
    _module: int
    _modulepart: int

    def __init__(self):
        super().__init__()
        self._module = 0
        self._modulepart = 0

    def get_module(self):
        return self._module

    def set_module(self, module):
        self._module = module

    def get_modulepart(self):
        return self._modulepart

    def set_modulepart(self, modulepart):
        self._modulepart = modulepart

    def __str__(self):
        return f"ModuleList: id: {self.get_id()}, module: {self._module}, modulepart: {self._modulepart}"

    def json(self):
        return json.dumps({
            'id': self.get_id(),
            'module': self.get_module(),
            'modulepart': self.get_modulepart()
        })

    @staticmethod
    def from_dict(dictionary=dict()):
        """Umwandeln eines Python dict() in ein Semester()."""
        obj = Semester()
        obj.set_id(dictionary["id"])
        obj.set_module(dictionary["module"])
        obj.set_modulepart(dictionary["modulepart"])
        return obj

