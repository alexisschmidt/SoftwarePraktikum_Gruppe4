from server.bo.Semester import Semester
from .Mapper import Mapper


class SemesterMapper(Mapper):

    def __init__(self):
        super().__init__()

    def find_all(self):
        result = []
        cursor = self._cnx.cursor()
        cursor.execute("SELECT id, creationdate, createdby, name, title, semester_hash from semester")
        tuples = cursor.fetchall()

        for (id, creationdate, createdby, name, title, semester_hash) \
                in tuples:
            semester = Semester()
            semester.set_creationdate(creationdate)
            semester.set_creator(createdby)
            semester.set_id(id)
            semester.set_name(name)
            semester.set_title(title)

            result.append(semester)

        self._cnx.commit()
        cursor.close()

        return result

    def find_by_name(self, name):
        result = None
        cursor = self._cnx.cursor()
        command = "SELECT id, creationdate, createdby, name, title, semester_hash FROM semester WHERE name={}".format(name)
        cursor.execute(command)
        tuples = cursor.fetchall()

        try:
            (id, creationdate, createdby, name, title, semester_hash) = tuples[0]
            semester = Semester()
            semester.set_creationdate(creationdate)
            semester.set_creator(createdby)
            semester.set_id(id)
            semester.set_name(name)
            semester.set_title(title)
            result = semester
        except IndexError:
            result = None

        self._cnx.commit()
        cursor.close()
        return result

    def find_hash_by_id(self, id: int):
        result = None
        cursor = self._cnx.cursor()

        # finden der SPO in der DB:
        command = f"SELECT semester_hash " \
                  f"FROM semester WHERE id={id}"
        cursor.execute(command)
        tuples = cursor.fetchall()
        try:
            result = tuples[0][0]
        except IndexError:
            result = None

        self._cnx.commit()
        cursor.close()
        return result

    def find_by_hash(self, hashcode):

        result = None
        cursor = self._cnx.cursor()
        command = f"SELECT id, creationdate, createdby, name, title, semester_hash FROM semester WHERE semester_hash={hashcode}"
        cursor.execute(command)
        tuples = cursor.fetchall()

        try:
            (id, creationdate, createdby, name, title, semester_hash) = tuples[0]
            semester = Semester()
            semester.set_creationdate(creationdate)
            semester.set_creator(createdby)
            semester.set_id(id)
            semester.set_name(name)
            semester.set_title(title)
            result = semester

        except IndexError:
            result = None

        self._cnx.commit()
        cursor.close()
        return result

    def find_semester_by_spo_hash(self, hashcode: int):

        result = []

        cursor = self._cnx.cursor()
        command = f"SELECT semester_hash FROM spovalidity WHERE spo_hash={hashcode}"
        cursor.execute(command)
        tuples = cursor.fetchall()

        scs = []
        for (semester_hash) in tuples:
            cursor.execute(
                f"SELECT id, creationdate, createdby, name, title, semester_hash FROM semester "
                f"WHERE semester_hash ={semester_hash}")
            scs.append(cursor.fetchall())
        for i in scs:
            for (id, creationdate, createdby, name, title, semester_hash) in i:
                semester = Semester()
                semester.set_id(id)
                semester.set_creationdate(creationdate)
                semester.set_name(name)
                semester.set_title(title)
                result.append(semester)

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

        command = "INSERT INTO semester (id, creationdate, createdby, name, title, semester_hash) " \
                  "VALUES (%s,%s,%s,%s,%s,%s) "
        data = (semester.get_id(), semester.get_creationdate(), semester.get_creator(),
                semester.get_name(), semester.get_title(),
                hash(semester))
        cursor.execute(command, data)

        self._cnx.commit()
        cursor.close()

        return semester

    def update(self, semester):

        cursor = self._cnx.cursor()

        command = "UPDATE semester SET creationdate=%s, createdby=%s, name=%s, title=%s " \
                  f"WHERE id={semester.get_id()} AND semester_hash={hash(semester)}"
        data = (
            semester.set_creationdate(), semester.get_creator(),
            semester.get_name(), semester.get_title())
        cursor.execute(command, data)

        self._cnx.commit()
        cursor.close()

        return semester

    def delete(self, semester):

        cursor = self._cnx.cursor()

        command = f"DELETE FROM semester WHERE semester_hash={hash(semester)}"
        cursor.execute(command)
        self._cnx.commit()
        cursor.close()
