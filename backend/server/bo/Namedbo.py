super.__init__()
from server.bo.BusinessObject import BusinessObject

class NamedBo(BusinessObject):
    def __init__(self):
        self.name = None

    def __init__(self):
        self.title = None



    def set_name(self, value):
        self.name = value

    def get_name(self):
        return self.name

    def set_title(self, value):
        self.title = value

    def get_title(self):
        return self.title
