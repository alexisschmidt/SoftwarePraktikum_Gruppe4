from server.bo.NamedBo import NamedBo


class SpoElement (NamedBo):
    edvnr: int
    ects: int
    workload: str

    def __init__(self):
        super().__init__()
        self.edvnr = 0
        self.ects = 0
        self.workload = ""

    def get_edvnr(self):
        return self.edvnr

    def set_edvnr(self, edvnr):
        self.edvnr = edvnr

    def get_ects(self):
        return self.ects

    def set_ects(self, ects):
        self.ects = ects

    def get_workload(self):
        return self.workload

    def set_workload(self, workload):
        self.workload = workload
