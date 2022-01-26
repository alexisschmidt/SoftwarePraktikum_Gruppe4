from server.bo.Module import Module
from .Mapper import Mapper


class ModuleMapper(Mapper):

    def __init__(self):
        super().__init__()

    def find_all(self):

        result = []

        command = "SELECT id, creationdate, name, title, " \
                  "requirement, examtype, outcome, type, " \
                  "ects, edvnr, workload, " \
                  "instructor_hash " \
                  "FROM module"

        cursor = self._cnx.cursor()
        cursor.execute(command)
        tuples = cursor.fetchall()

        for (id, creationdate, name, title,
             requirement, examtype, outcome, type,
             ects, edvnr, workload,
             instructor_hash) in tuples:
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

    def find_by_name(self, m_name: str):

        result = None
        command = "SELECT id, creationdate, name, title, " \
                  "requirement, examtype, outcome, type, " \
                  "ects, edvnr, workload, " \
                  "instructor_hash " \
                  "FROM module " \
                  f"WHERE name LIKE '{m_name}' ORDER BY name"

        cursor = self._cnx.cursor()
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

        except IndexError:
            result = None

        result = module
        self._cnx.commit()
        cursor.close()
        return result

    def find_by_id(self, key: int):

        result = None
        command = f"SELECT id, creationdate, createdby, name, title, " \
                  f"requirement, examtype, outcome, type, " \
                  f"ects, edvnr, workload, module_hash instructor_hash " \
                  f"FROM module WHERE id={key}"
        cursor = self._cnx.cursor()
        cursor.execute(command)
        tuples = cursor.fetchall()

        try:
            (id, creationdate, createdby, name, title,
             requirement, examtype, outcome, type,
             ects, edvnr, workload, module_hash,
             instructor_hash) = tuples[0]
            module = Module()
            module.set_id(id)
            module.set_creationdate(creationdate)
            module.set_creator(createdby)
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
            cursor.execute(f"SELECT modulepart_hash FROM modulepart WHERE module_hash={module_hash}")
            parts = list(cursor.fetchall())
            module.set_parts(parts)
            result = module
        except IndexError:
            result = None

        self._cnx.commit()
        cursor.close()

        return result

    def find_by_hash(self, hashcode: int):

        result = None
        cursor = self._cnx.cursor()

        # finden des Moduls in der DB:
        command = f"SELECT * FROM module WHERE module_hash={hashcode}"
        cursor.execute(command)
        tuples = cursor.fetchall()

        # finden der Moduleparts des Moduls in der DB:
        cursor.execute(f"SELECT modulepart_hash FROM modulepart WHERE module_hash={hashcode}")
        parts = list(cursor.fetchall())

        # Erstellen des Objekts
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
            module.set_parts(parts)
            result = module
        except IndexError:
            result = None

        self._cnx.commit()
        cursor.close()

        return result

    def insert(self, module: Module):

        cursor = self._cnx.cursor()
        cursor.execute("SELECT MAX(id) AS maxid FROM module ")
        tuples = cursor.fetchall()

        for (maxid) in tuples:
            if maxid[0] is not None:
                module.set_id(maxid[0] + 1)
            else:
                module.set_id(1)

        command = "INSERT INTO module (id, creationdate, createdby, name, title, " \
                  "requirement, examtype, outcome, type, " \
                  "ects, edvnr, workload, " \
                  "module_hash, instructor_hash)" \
                  "VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
        data = (module.get_id(), module.get_creationdate(), module.get_creator(), module.get_name(), module.get_title(),
                module.get_requirement(), module.get_examtype(), module.get_outcome(), module.get_type(),
                module.get_ects(), module.get_edvnr(), module.get_workload(),
                hash(module), module.get_instructor())
        cursor.execute(command, data)

        self._cnx.commit()
        cursor.close()

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

    def delete(self, module: Module):

        cursor = self._cnx.cursor()
        command = f"DELETE FROM module WHERE module_hash={hash(module)}"
        cursor.execute(command)
        self._cnx.commit()
        cursor.close()
