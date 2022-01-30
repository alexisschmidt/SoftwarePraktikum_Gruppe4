from server.bo.Modulepart import Modulepart
from .Mapper import Mapper


class ModulePartMapper(Mapper):

    def __init__(self):
        super().__init__()

    def find_all(self):
        result = []
        cursor = self._cnx.cursor()
        cursor.execute("SELECT id, creationdate, name, title, "
                       "language, literature, semester, sources, connection, description, sws, "
                       "ects, edvnr, workload, module_hash, professor_hash FROM modulepart")
        tuples = cursor.fetchall()

        for (id, creationdate, name, title,
             language, literature, semester, sources, connection, description,
             sws, ects, edvnr, workload, modulehash, professor) \
                in tuples:
            modulepart = Modulepart()
            modulepart.set_id(id)
            modulepart.set_name(name)
            modulepart.set_title(title)
            modulepart.set_language(language)
            modulepart.set_literature(literature)
            modulepart.set_semester(semester)
            modulepart.set_sources(sources)
            modulepart.set_connection(connection)
            modulepart.set_description(description)
            modulepart.set_sws(sws)
            modulepart.set_ects(ects)
            modulepart.set_edvnr(edvnr)
            modulepart.set_workload(workload)
            modulepart.set_professor(professor)

            result.append(modulepart)

        self._cnx.commit()
        cursor.close()
        return result

    def find_by_name(self, name: str):

        result = []
        cursor = self._cnx.cursor()
        command = "SELECT id, creationdate, name, title, " \
                  "language, literature, semester, sources, connection, description, sws, " \
                  f"ects, edvnr, workload, module_hash, professor_hash FROM modulepart WHERE name LIKE '{name}' ORDER BY name"
        cursor.execute(command)
        tuples = cursor.fetchall()

        for (id, creationdate, name, title,
             language, literature, semester, sources, connection, description, sws,
             ects, edvnr, workload, modulehash, professor) in tuples:
            modulepart = Modulepart()
            modulepart.set_id(id)
            modulepart.set_name(name)
            modulepart.set_title(title)
            modulepart.set_language(language)
            modulepart.set_literature(literature)
            modulepart.set_semester(semester)
            modulepart.set_sources(sources)
            modulepart.set_connection(connection)
            modulepart.set_description(description)
            modulepart.set_sws(sws)
            modulepart.set_ects(ects)
            modulepart.set_edvnr(edvnr)
            modulepart.set_workload(workload)
            modulepart.set_professor(professor)
            result.append(modulepart)

        self._cnx.commit()
        cursor.close()
        return result

    def find_hash_by_module(self, modulehash: int):
        result = []

        cursor = self._cnx.cursor()
        command = f"SELECT modulepart_hash FROM modulepart WHERE module_hash={modulehash}"
        cursor.execute(command)
        tuples = cursor.fetchall()

        for modulepart_hash in tuples:
            result.append(modulepart_hash[0])

        self._cnx.commit()
        cursor.close()
        return result

    def find_by_hash(self, hashcode: int):

        result = None

        cursor = self._cnx.cursor()
        command = "SELECT id, creationdate, createdby, name, title, " \
                  "language, literature, semester, sources, connection, description, sws, " \
                  f"ects, edvnr, workload, professor_hash FROM modulepart WHERE modulepart_hash={hashcode}"
        cursor.execute(command)
        tuples = cursor.fetchall()

        try:
            (id, creationdate, createdby, name, title,
             language, literature, semester, sources, connection, description, sws,
             ects, edvnr, workload, professor_hash) = tuples[0]
            modulepart = Modulepart()
            modulepart.set_id(id)
            modulepart.set_creationdate(creationdate)
            modulepart.set_creator(createdby)
            modulepart.set_name(name)
            modulepart.set_title(title)
            modulepart.set_language(language)
            modulepart.set_literature(literature)
            modulepart.set_semester(semester)
            modulepart.set_sources(sources)
            modulepart.set_connection(connection)
            modulepart.set_description(description)
            modulepart.set_sws(sws)
            modulepart.set_ects(ects)
            modulepart.set_edvnr(edvnr)
            modulepart.set_workload(workload)
            modulepart.set_professor(professor_hash)

            result = modulepart
        except IndexError:
            result = None

        self._cnx.commit()
        cursor.close()
        return result

    def insert(self, modulepart: Modulepart):

        cursor = self._cnx.cursor()
        cursor.execute("SELECT MAX(id) AS maxid FROM modulepart ")
        tuples = cursor.fetchall()

        for (maxid) in tuples:
            if maxid[0] is not None:
                modulepart.set_id(maxid[0] + 1)
            else:
                modulepart.set_id(1)

        command = "INSERT INTO modulepart " \
                  "(id, creationdate, createdby, name, title, " \
                  "language, literature, semester, sources, connection, description, sws, " \
                  "ects, edvnr, workload, " \
                  "modulepart_hash, professor_hash, module_hash) " \
                  "VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"

        data = (modulepart.get_id(), modulepart.get_creationdate(), modulepart.get_creator(),
                modulepart.get_name(), modulepart.get_title(),
                modulepart.get_language(), modulepart.get_literature(), modulepart.get_semester(),
                modulepart.get_sources(), modulepart.get_connection(), modulepart.get_description(),
                modulepart.get_sws(), modulepart.get_ects(), modulepart.get_edvnr(), modulepart.get_workload(),
                hash(modulepart), modulepart.get_professor(), modulepart.get_module())

        cursor.execute(command, data)
        self._cnx.commit()
        cursor.close()
        return modulepart

    def update(self, modulepart: Modulepart):

        cursor = self._cnx.cursor()

        command = "UPDATE modulepart SET name=%s, title=%s, language=%s, literature=%s, " \
                  "semester_id=%s, sources=%s, connection=%s, description=%s, " \
                  "sws=%s, ects=%s, edvnr=%s, workload=%s, module_hash=%s, professor_hash=%s WHERE id=%s AND modulepart_hash=%s "
        data = (
            modulepart.get_name(), modulepart.get_title(), modulepart.get_language(),
            modulepart.get_literature(), modulepart.get_semester(), modulepart.get_sources(),
            modulepart.get_connection(), modulepart.get_description(), modulepart.get_sws(), modulepart.get_ects(),
            modulepart.get_edvnr(), modulepart.get_workload(), modulepart.get_id(), modulepart.get_module(), modulepart.get_professor(), hash(modulepart))
        cursor.execute(command, data)

        self._cnx.commit()
        cursor.close()

    def delete(self, modulepart: Modulepart):

        cursor = self._cnx.cursor()
        command = f"DELETE FROM modulepart WHERE id={modulepart.get_id()}"
        cursor.execute(command)
        self._cnx.commit()
        cursor.close()
