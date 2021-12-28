from server.bo.NamedBo import NamedBo
import json


class StudyCourse (NamedBo):
    def __init__(self):
        super().__init__()

    def json(self):
        modulehash=[]
        for modulepart in self.__moduleparts:
            modulehash.append(modulepart.hash())

        return json.dumps({
            'id': self.get_id(), 
            'name': self.get_name(), 
            'title': self.get_title()
            })


    @staticmethod
    def from_dict(dictionary=dict()):
        """Umwandeln eines Python dict() in einen StudyCourse()."""
        obj = StudyCourse()
        obj.set_id(dictionary["id"])  # Teil von BusinessObject!
        obj.set_name(dictionary["name"])
        obj.title(dictionary["title"])
        return obj
