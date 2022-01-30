from server.bo.ModuleType import ModuleType
from server.db.Mapper import Mapper


class ModuleTypeMapper(Mapper):

    def __init__(self):
        super().__init__()

    def find_all(self):
        result = []
        cursor = self._cnx.cursor()

        # finden der SPO in der DB:
        command = f"SELECT moduletype_hash " \
                  f"FROM moduletype"
        cursor.execute(command)
        tuples = cursor.fetchall()

        for mthash in tuples:
            result.append(mthash[0])

        self._cnx.commit()
        cursor.close()
        return result

    def find_by_name(self, typename):

        result = []
        cursor = self._cnx.cursor()
        command = f"SELECT moduletype_hash FROM moduletype WHERE name LIKE '{typename}' " \
                  "ORDER BY name"
        cursor.execute(command)
        tuples = cursor.fetchall()

        for (id, creationdate, name, title) in tuples:
            moduletype = ModuleType()
            moduletype.set_id(id)
            moduletype.set_name(name)
            moduletype.set_title(title)

            result.append(moduletype)

        self._cnx.commit()
        cursor.close()

        return result

    def find_hash_by_id(self, id: int):
        result = None
        cursor = self._cnx.cursor()

        # finden der SPO in der DB:
        command = f"SELECT moduletype_hash " \
                  f"FROM moduletype WHERE id={id}"
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
        command = f"SELECT id, creationdate, createdby, name, title FROM moduletype WHERE moduletype_hash={hashcode}"
        cursor.execute(command)
        tuples = cursor.fetchall()

        try:
            (id, creationdate, createdby, name, title) = tuples[0]
            moduletype = ModuleType()
            moduletype.set_id(id)
            moduletype.set_creationdate(creationdate)
            moduletype.set_creator(createdby)
            moduletype.set_name(name)
            moduletype.set_title(title)

            result = moduletype
        except IndexError:

            result = None

        self._cnx.commit()
        cursor.close()

        return result

    def insert(self, moduletype: ModuleType):

        cursor = self._cnx.cursor()
        cursor.execute("SELECT MAX(id) AS maxid FROM moduletype ")
        tuples = cursor.fetchall()

        for (maxid) in tuples:
            if maxid[0] is not None:
                moduletype.set_id(maxid[0] + 1)
            else:
                moduletype.set_id(1)

        command = "INSERT INTO moduletype (id, creationdate, createdby, name, title, moduletype_hash) " \
                  "VALUES (%s,%s,%s,%s,%s,%s)"
        data = (moduletype.get_id(), moduletype.get_creationdate(), moduletype.get_creator(),
                moduletype.get_name(), moduletype.get_title(), hash(moduletype))
        cursor.execute(command, data)

        self._cnx.commit()
        cursor.close()

        return moduletype

    def update(self, moduletype: ModuleType):

        cursor = self._cnx.cursor()

        command = f"UPDATE moduletype " \
                  f"SET name='{moduletype.get_name()}', " \
                  f"title='{moduletype.get_title()}'" \
                  f" WHERE id={moduletype.get_id()} "
        cursor.execute(command)

        self._cnx.commit()
        cursor.close()

    def delete(self, moduletype: ModuleType):

        cursor = self._cnx.cursor()

        command = f"DELETE FROM moduletype WHERE moduletype_hash={hash(moduletype)}"
        cursor.execute(command)

        self._cnx.commit()
        cursor.close()