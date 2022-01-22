from server.bo.Semester import Semester
from .Mapper import Mapper


class SemesterMapper(Mapper):

    def __init__(self):
        super().__init__()

    def find_all(self):
        result = []
        cursor = self._cnx.cursor()
        cursor.execute("SELECT * from semester")
        tuples = cursor.fetchall()

        for (id, creationdate, name, title,) \
                in tuples:
            semester = Semester()
            semester.set_id(id)
            semester.set_name(name)
            semester.set_title(title)

            result.append(semester)

        self._cnx.commit()
        cursor.close()

        return result

    def find_by_name(self, name):
        result = []
        cursor = self._cnx.cursor()
        command = "SELECT * FROM semester WHERE name LIKE '{}' ORDER BY name".format(name)
        cursor.execute(command)
        tuples = cursor.fetchall()

        for (id, creationdate, name, title) in tuples:
            semester = Semester()
            semester.set_id(id)
            semester.set_name(name)
            semester.set_title(title)

            result.append(semester)

        self._cnx.commit()
        cursor.close()

        return result

    def find_by_id(self, key):

        result = None

        cursor = self._cnx.cursor()
        command = "SELECT * semester WHERE id={}".format(key)
        cursor.execute(command)
        tuples = cursor.fetchall()

        try:
            (id, creationdate, name, title) = tuples[0]
            semester = Semester()
            semester.set_id(id)
            semester.set_name(name)
            semester.set_title(title)
            result = semester

        except IndexError:
            result = None

        self._cnx.commit()
        cursor.close()

        return result

    def find_by_hash(self, hashcode):

        result = None

        cursor = self._cnx.cursor()
        command = "SELECT * semester WHERE semester_hash={}".format(hashcode)
        cursor.execute(command)
        tuples = cursor.fetchall()

        try:
            (id, creationdate, name, title) = tuples[0]
            semester = Semester()
            semester.set_id(id)
            semester.set_name(name)
            semester.set_title(title)
            result = semester

        except IndexError:
            result = None

        self._cnx.commit()
        cursor.close()

        return result

    def insert(self, semester):

        cursor = self._cnx.cursor()
        cursor.execute("SELECT MAX(id) AS maxid FROM semester")
        tuples = cursor.fetchall()

        for (maxid) in tuples:
            if maxid[0] is not None:

                semester.set_id(maxid[0] + 1)
            else:

                semester.set_id(1)

        command = "INSERT INTO semester (id, creationdate, name, title, semester_hash) VALUES (%s,%s,%s,%s,%s) "
        data = (semester.get_id(), semester.get_name(), semester.get_title(), hash(semester))
        cursor.execute(command, data)

        self._cnx.commit()
        cursor.close()

        return semester

    def update(self, semester):

        cursor = self._cnx.cursor()

        command = "UPDATE semester " + "SET name=%s, SET title=%s, WHERE id=%s "
        data = (
            semester.get_id(), semester.get_name(), semester.get_title())
        cursor.execute(command, data)

        self._cnx.commit()
        cursor.close()

        return semester

    def delete(self, semester):

        cursor = self._cnx.cursor()

        command = "DELETE FROM semester WHERE id={}".format(semester.get_id())
        cursor.execute(command)

        self._cnx.commit()
        cursor.close()