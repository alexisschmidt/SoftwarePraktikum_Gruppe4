from server.bo.StudyCourse import StudyCourse
from server.db.Mapper import Mapper


class StudyCourseMapper(Mapper):

    def __init__(self):
        super().__init__()

    def find_all(self):
        result = []
        cursor = self._cnx.cursor()

        # finden der SPO in der DB:
        command = f"SELECT studycourse_hash " \
                  f"FROM studycourse"
        cursor.execute(command)
        tuples = cursor.fetchall()

        for schash in tuples:
            result.append(schash[0])

        self._cnx.commit()
        cursor.close()
        return result

    def find_by_name(self, name):

        result = []
        cursor = self._cnx.cursor()
        command = "SELECT * FROM studycourse WHERE name LIKE '{}' " \
                  "ORDER BY name".format(name)
        cursor.execute(command)
        tuples = cursor.fetchall()

        for (id, creationdate, name, title) in tuples:
            studycourse = StudyCourse()
            studycourse.set_id(id)
            studycourse.set_name(name)
            studycourse.set_title(title)

            result.append(studycourse)

        self._cnx.commit()
        cursor.close()

        return result

    def find_hash_by_id(self, id: int):
        result = None
        cursor = self._cnx.cursor()

        # finden der SPO in der DB:
        command = f"SELECT studycourse_hash " \
                  f"FROM studycourse WHERE id={id}"
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
        command = f"SELECT id, creationdate, createdby, name, title FROM studycourse WHERE studycourse_hash={hashcode}"
        cursor.execute(command)
        tuples = cursor.fetchall()

        try:
            (id, creationdate, createdby, name, title) = tuples[0]
            studycourse = StudyCourse()
            studycourse.set_id(id)
            studycourse.set_creationdate(creationdate)
            studycourse.set_creator(createdby)
            studycourse.set_name(name)
            studycourse.set_title(title)

            result = studycourse
        except IndexError:

            result = None

        self._cnx.commit()
        cursor.close()

        return result

    def insert(self, studycourse: StudyCourse):

        cursor = self._cnx.cursor()
        cursor.execute("SELECT MAX(id) AS maxid FROM studycourse ")
        tuples = cursor.fetchall()

        for (maxid) in tuples:
            if maxid[0] is not None:
                studycourse.set_id(maxid[0] + 1)
            else:
                studycourse.set_id(1)

        command = "INSERT INTO studycourse (id, creationdate, createdby, name, title, studycourse_hash) " \
                  "VALUES (%s,%s,%s,%s,%s,%s)"
        data = (studycourse.get_id(), studycourse.get_creationdate(), studycourse.get_creator(),
                studycourse.get_name(), studycourse.get_title(), hash(studycourse))
        cursor.execute(command, data)

        self._cnx.commit()
        cursor.close()

        return studycourse

    def update(self, studycourse: StudyCourse):

        cursor = self._cnx.cursor()

        command = f"UPDATE studycourse " + f"SET name='{studycourse.get_name()}', " \
                                           f"title='{studycourse.get_title()}'" \
                                           f" WHERE id={studycourse.get_id()} "
        cursor.execute(command)

        self._cnx.commit()
        cursor.close()

    def delete(self, studycourse: StudyCourse):

        cursor = self._cnx.cursor()

        command = "DELETE FROM studycourse WHERE id={}".format(studycourse.get_id())
        cursor.execute(command)

        self._cnx.commit()
        cursor.close()

