from server.bo.Module import Module
from .Mapper import Mapper


class ModuleMapper(Mapper):

    def __init__(self):
        super().__init__()

    def find_all(self):

        result = []
        command = "SELECT id, creationdate, name, title, requirement, examtype, outcome, type, ects, edvnr, workload, instructor_hash FROM module"
        cursor = self._cnx.cursor()
        cursor.execute(command)
        tuples = cursor.fetchall()

        for (id, creationdate, name, title,
             requirement, examtype, outcome, type,
             ects, edvnr, workload, instructor_hash) in tuples:
            module = Module()
            module.set_id(id)
            module.set_creationdate(creationdate)
            module.set_name(name)
            module.set_title(title)
            module.set_requirement(requirement)
            module.set_examtype(examtype)
            module.set_outcome(outcome)
            module.set_type(type)
            module.set_ects(ects)
            module.set_edvnr(edvnr)
            module.set_workload(workload)
            module.set_instructor(instructor_hash)
            result.append(module)

        self._cnx.commit()
        cursor.close()

        return result

    def find_by_name(self, name):

        result = []
        cursor = self._cnx.cursor()
        command = "SELECT * FROM module WHERE name LIKE '{}' ORDER BY name".format(name)
        cursor.execute(command)
        tuples = cursor.fetchall()

        for (
                id, creationdate, name, title, requirement, examtype, instructor, outcome, type, moduleparts, ects,
                edvnr,
                workload) in tuples:
            module = Module()
            module.set_id(id)
            module.set_name(name)
            module.set_title(title)
            module.set_requirement(requirement)
            module.set_examtype(examtype)
            module.set_instructor(instructor)
            module.set_outcome(outcome)
            module.set_type(type)
            module.set_ects(ects)
            module.set_edvnr(edvnr)
            module.set_workload(workload)

            result.append(module)

        self._cnx.commit()
        cursor.close()

        return result

    def find_by_key(self, key):

        result = None
        cursor = self._cnx.cursor()
        command = "SELECT id, creationdate, name, title, requirement, examtype, outcome, type, ects, edvnr, workload, instructor_hash FROM module WHERE id={}".format(key)
        cursor.execute(command)
        tuples = cursor.fetchall()

        try:
            (id, creationdate, name, title,
             requirement, examtype, outcome, type,
             ects, edvnr, workload,
             instructor_hash) = tuples[0]
            module = Module()
            module.set_id(id)
            module.set_creationdate(creationdate)
            module.set_name(name)
            module.set_title(title)
            module.set_requirement(requirement)
            module.set_examtype(examtype)
            module.set_outcome(outcome)
            module.set_type(type)
            module.set_ects(ects)
            module.set_edvnr(edvnr)
            module.set_workload(workload)
            module.set_instructor(instructor_hash)
            result = module
        except IndexError:
            result = None

        self._cnx.commit()
        cursor.close()

        return result

    def find_by_hash(self, hashcode: int):
        result = None

        command = "SELECT * module WHERE module_hash={}".format(hashcode)
        cursor = self._cnx.cursor()
        cursor.execute(command)
        tuples = cursor.fetchall()

        try:
            (id, creationdate, name, title,
             requirement, examtype, instructor, outcome, type, moduleparts,
             ects, edvnr, workload) = tuples[0]
            module = Module()
            module.set_id(id)
            module.set_name(name)
            module.set_title(title)
            module.set_requirement(requirement)
            module.set_examtype(examtype)
            module.set_instructor(instructor)
            module.set_outcome(outcome)
            module.set_type(type)
            module.set_ects(ects)
            module.set_edvnr(edvnr)
            module.set_workload(workload)
            result = module
        except IndexError:

            result = None

        self._cnx.commit()
        cursor.close()

        return result

    def insert(self, module: Module):
        print(module)
        cursor = self._cnx.cursor()
        cursor.execute("SELECT MAX(id) AS maxid FROM module ")
        tuples = cursor.fetchall()

        for (maxid) in tuples:
            if maxid[0] is not None:
                module.set_id(maxid[0] + 1)
            else:
                module.set_id(1)
        command = "INSERT INTO module (id, creationdate, name, title, requirement, examtype, outcome, type, ects, edvnr, workload, instructor, module_hash) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s) "
        data = (
        module.get_id(), module.get_creationdate(), module.get_name(), module.get_title(), module.get_requirement(),
        module.get_examtype(), module.get_outcome(), module.get_type(),
        0, module.get_edvnr(), module.get_workload(), module.get_instructor(), hash(module))
        cursor.execute(command, data)

        self._cnx.commit()
        cursor.close()

        return module

    def update(self, module: Module):

        cursor = self._cnx.cursor()

        command = "UPDATE module " + "SET name=%s, SET title=%s, SET requirement=%s, SET examtype=%s, " \
                                     "SET instructor=%s, SET outcome=%s, SET type=%s, SET moduleparts=%s, " \
                                     "SET ects=%s, SET edvnr=%s, SET workload=%s WHERE id=%s "
        data = (
            module.get_name(), module.get_title(), module.get_requirement(), module.get_examtype(),
            module.get_instructor(), module.get_outcome(), module.get_type(),
            module.get_ects(),
            module.get_edvnr(), module.get_workload(), module.get_id())
        cursor.execute(command, data)

        self._cnx.commit()
        cursor.close()

    def delete(self, module):

        cursor = self._cnx.cursor()

        command = "DELETE FROM module WHERE id={}".format(module.get_id())
        cursor.execute(command)

        self._cnx.commit()
        cursor.close()
