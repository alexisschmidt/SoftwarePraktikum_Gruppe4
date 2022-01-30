from server.bo.ExamType import ExamType
from server.db.Mapper import Mapper


class ExamTypeMapper(Mapper):

    def __init__(self):
        super().__init__()

    def find_all(self):
        result = []
        cursor = self._cnx.cursor()

        # finden der SPO in der DB:
        command = f"SELECT examtype_hash " \
                  f"FROM examtype"
        cursor.execute(command)
        tuples = cursor.fetchall()

        for schash in tuples:
            result.append(schash[0])

        self._cnx.commit()
        cursor.close()
        return result

    def find_by_name(self, examtypename):

        result = []
        cursor = self._cnx.cursor()
        command = f"SELECT id, creationdate, createdby, name, title " \
                  f"FROM examtype WHERE name LIKE '{examtypename}' " \
                  f"ORDER BY name"
        cursor.execute(command)
        tuples = cursor.fetchall()

        for (id, creationdate, name, title) in tuples:
            examtype = ExamType()
            examtype.set_id(id)
            examtype.set_name(name)
            examtype.set_title(title)

            result.append(examtype)

        self._cnx.commit()
        cursor.close()

        return result

    def find_hash_by_id(self, id: int):
        result = None
        cursor = self._cnx.cursor()

        # finden der SPO in der DB:
        command = f"SELECT examtype_hash " \
                  f"FROM examtype WHERE id={id}"
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
        command = f"SELECT id, creationdate, createdby, name, title " \
                  f"FROM examtype " \
                  f"WHERE examtype_hash={hashcode}"
        cursor.execute(command)
        tuples = cursor.fetchall()

        try:
            (id, creationdate, createdby, name, title) = tuples[0]
            examtype = ExamType()
            examtype.set_id(id)
            examtype.set_creationdate(creationdate)
            examtype.set_creator(createdby)
            examtype.set_name(name)
            examtype.set_title(title)

            result = examtype
        except IndexError:

            result = None

        self._cnx.commit()
        cursor.close()

        return result

    def insert(self, examtype: ExamType):

        cursor = self._cnx.cursor()
        cursor.execute("SELECT MAX(id) AS maxid FROM examtype ")
        tuples = cursor.fetchall()

        for (maxid) in tuples:
            if maxid[0] is not None:
                examtype.set_id(maxid[0] + 1)
            else:
                examtype.set_id(1)

        command = "INSERT INTO examtype (id, creationdate, createdby, name, title, examtype_hash) " \
                  "VALUES (%s,%s,%s,%s,%s,%s)"
        data = (examtype.get_id(), examtype.get_creationdate(), examtype.get_creator(),
                examtype.get_name(), examtype.get_title(), hash(examtype))
        cursor.execute(command, data)

        self._cnx.commit()
        cursor.close()

        return examtype

    def update(self, examtype: ExamType):

        cursor = self._cnx.cursor()

        command = f"UPDATE examtype SET name='{examtype.get_name()}', " \
                  f"title='{examtype.get_title()}' " \
                  f"WHERE id={examtype.get_id()} "
        cursor.execute(command)

        self._cnx.commit()
        cursor.close()

    def delete(self, examtype: ExamType):

        cursor = self._cnx.cursor()

        command = f"DELETE FROM examtype WHERE examtype_hash={hash(examtype)}"
        cursor.execute(command)

        self._cnx.commit()
        cursor.close()