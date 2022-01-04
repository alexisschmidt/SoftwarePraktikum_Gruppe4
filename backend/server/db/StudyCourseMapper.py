from server.bo.StudyCourse import StudyCourse
from backend.server.db.Mapper import Mapper


class StudyCourseMapper(Mapper):

    def __init__(self):
        super().__init__()

    def find_all(self):
        result = []
        cursor = self._cnx.cursor()
        cursor.execute("SELECT * from studycourse")
        tuples = cursor.fetchall()

        for (id, creationdate, name, title) in tuples:
            studycourse = StudyCourse
            studycourse.set_id(id)
            studycourse.set_pname(name)
            studycourse.set_title(title)

            result.append(studycourse)

        self._cnx.commit()
        cursor.close()

        return result

    def find_by_name(self, name):

        result = []
        cursor = self._cnx.cursor()
        command = "SELECT * FROM studycourse WHERE name LIKE '{}' ORDER BY name".format(name)
        cursor.execute(command)
        tuples = cursor.fetchall()

        for (id, creationdate, name, title) in tuples:
            studycourse = Studycourse()
            studycourse.set_id(id)
            studycourse.set_name(name)
            studycourse.set_title(title)

            result.append(studycourse)

        self._cnx.commit()
        cursor.close()

        return result

    def find_by_key(self, key):

        result = None

        cursor = self._cnx.cursor()
        command = "SELECT * studycourse WHERE id={}".format(key)
        cursor.execute(command)
        tuples = cursor.fetchall()

        try:
            (id, creationdate, name, title) = tuples[0]
            studycourse = Studycourse()
            studycourse.set_id(id)
            studycourse.set_name(name)
            studycourse.set_title(title)

            result = studycourse
        except IndexError:

            result = None

        self._cnx.commit()
        cursor.close()

        return result

    def insert(self, studycourse):

        cursor = self._cnx.cursor()
        cursor.execute("SELECT MAX(id) AS maxid FROM studycourse ")
        tuples = cursor.fetchall()

        for (maxid) in tuples:
            if maxid[0] is not None:

                studycourse.set_id(maxid[0] + 1)
            else:

                studycourse.set_id(1)

        command = "INSERT INTO studycourse (id, creationdate, name, title) VALUES (%s,%s,%s,%s) "
        data = (studycourse.get_id(), studycourse.get_creationdate(), studycourse.get_name(), studycourse.get_title())
        cursor.execute(command, data)

        self._cnx.commit()
        cursor.close()

        return studycourse

    def update(self, studycourse):

        cursor = self._cnx.cursor()

        command = "UPDATE studycourse " + "SET name=%s, SET title=%s WHERE id=%s "
        data = (studycourse.get_name(), studycourse.get_title(), studycourse.get_id())
        cursor.execute(command, data)

        self._cnx.commit()
        cursor.close()

    def delete(self, studycourse):

        cursor = self._cnx.cursor()

        command = "DELETE FROM studycourse WHERE id={}".format(studycourse.get_id())
        cursor.execute(command)

        self._cnx.commit()
        cursor.close()



