from server.bo import NamedBo as nbo

class StudyCourse (nbo.NamedBo):
    def __init__(self):
        super().__init__()

    @staticmethod
    def from_dict(dictionary=dict()):
        """Umwandeln eines Python dict() in einen StudyCourse()."""
        obj = StudyCourse()
        obj.set_id(dictionary["id"])  # Teil von BusinessObject!
        obj.set_name(dictionary["name"])
        obj.title(dictionary["title"])
        return obj
