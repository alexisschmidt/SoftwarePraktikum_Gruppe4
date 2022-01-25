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
                       "ects, edvnr, workload FROM modulepart")
        tuples = cursor.fetchall()

        for (id, creationdate, name, title,
             language, literature, semester, sources, connection, description,
             sws, ects, edvnr, workload) \
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

            result.append(modulepart)

        self._cnx.commit()
        cursor.close()
        return result

    def find_by_name(self, name: str):

        result = []
        cursor = self._cnx.cursor()
        command = "SELECT id, creationdate, name, title, "\
                  "language, literature, semester, sources, connection, description, sws, "\
                  f"ects, edvnr, workload FROM modulepart WHERE name LIKE '{name}' ORDER BY name"
        cursor.execute(command)
        tuples = cursor.fetchall()

        for (id, creationdate, name, title,
             language, literature, semester, sources, connection, description, sws,
             ects, edvnr, workload) in tuples:
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
            result.append(modulepart)

        self._cnx.commit()
        cursor.close()
        return result

    def find_by_id(self, key: int):

        result = None

        cursor = self._cnx.cursor()
        command = "SELECT id, creationdate, createdby, name, title, "\
                  "language, literature, semester, sources, connection, description, sws, "\
                  f"ects, edvnr, workload FROM modulepart WHERE id={key}"
        cursor.execute(command)
        tuples = cursor.fetchall()

        try:
            (id, creationdate, createdby, name, title,
             language, literature, semester, sources, connection, description, sws,
             ects, edvnr, workload) = tuples[0]
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
            obj = modulepart
        except IndexError:
            result = None

        self._cnx.commit()
        cursor.close()
        return result

    def find_by_hash(self, hashcode: int):

        result = None

        cursor = self._cnx.cursor()
        command = "SELECT id, creationdate, name, title, "\
                  "language, literature, semester, sources, connection, description, sws, "\
                  f"ects, edvnr, workload FROM modulepart WHERE modulepart_hash={hashcode}"
        cursor.execute(command)
        tuples = cursor.fetchall()

        try:
            (id, creationdate, name, title,
             language, literature, semester, sources, connection, description, sws,
             ects, edvnr, workload) = tuples[0]
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

        try:
            cursor.execute(f'SELECT id FROM person WHERE person_hash={modulepart.get_professor()}')
            profid = int(cursor.fetchone()[0])
        except ValueError:
            print('modulepart needs a professor to be created!')

        try:
            cursor.execute(f'SELECT id FROM module WHERE module_hash={modulepart.get_module()}')
            modid = int(cursor.fetchone()[0])
        except ValueError:
            print('modulepart needs a professor to be created!')

        command = "INSERT INTO modulepart (id, creationdate, name, title, " \
                  "language, literature, semester, sources, connection, description, sws, " \
                  "ects, edvnr, workload, " \
                  "modulepart_hash, professor_id, professor_hash, module_id, module_hash) " \
                  "VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"

        data = (modulepart.get_id(), modulepart.get_creationdate(), modulepart.get_name(), modulepart.get_title(),
                modulepart.get_language(), modulepart.get_literature(), modulepart.get_semester(),
                modulepart.get_sources(), modulepart.get_connection(), modulepart.get_description(),
                modulepart.get_sws(), modulepart.get_ects(), modulepart.get_edvnr(), modulepart.get_workload(),
                hash(modulepart), profid, modulepart.get_professor(), modid, modulepart.get_module())

        cursor.execute(command, data)
        self._cnx.commit()
        cursor.close()
        return modulepart

    def update(self, modulepart: Modulepart):

        cursor = self._cnx.cursor()

        command = "UPDATE modulepart " + "SET name=%s, SET title=%s, SET language=%s, SET literature=%s, " \
                                         "SET semester_id=%s, SET sources=%s, SET connection=%s, SET description=%s, " \
                                         "SET sws=%s, SET ects=%s,SET edvnr=%s,SET workload=%s WHERE id=%s "
        data = (
            modulepart.get_name(), modulepart.get_title(), modulepart.get_language(),
            modulepart.get_literature(), modulepart.get_semester(), modulepart.get_sources(),
            modulepart.get_connection(), modulepart.get_description(), modulepart.get_sws(), modulepart.get_ects(),
            modulepart.get_edvnr(), modulepart.get_workload(), modulepart.get_id())
        cursor.execute(command, data)

        self._cnx.commit()
        cursor.close()

    def delete(self, modulepart: Modulepart):

        cursor = self._cnx.cursor()
        command = f"DELETE FROM modulepart WHERE id={modulepart.get_id()}"
        cursor.execute(command)
        self._cnx.commit()
        cursor.close()
