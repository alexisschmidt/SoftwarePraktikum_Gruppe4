from server.bo.ModuleList import ModuleList
from server.db.Mapper import Mapper


class ModuleListMapper (Mapper):

    def __init__(self):
        super().__init__()

    def find_all(self):
        result = []
        cursor = self._cnx.cursor()

        cursor.execute("SELECT + from modulelist")
        tuples = cursor.fetchall()

        for (id, creationdate, modulepart, module) in tuples:
            modulelist = ModuleList()
            modulelist.set_id(id)
            modulelist.set_creationdate(creationdate)
            modulelist.set_modulepart(modulepart)
            modulelist.set_module(module)
            result.append(modulelist)


        self._cnx.commit()
        cursor.close()

        return result

    def find_by_module(self, module):
        result = []
        cursor = self._cnx.cursor()
        command = "SELECT * FROM modulelist WHERE module={} ORDER BY id".format(module)
        cursor.execute(command)
        tuples = cursor.fetchall()

        for (id, creationdate, modulepart, module) in tuples:
            modulelist = ModuleList()
            modulelist.set_id(id)
            modulelist.set_creationdate(creationdate)
            modulelist.set_modulepart(modulepart)
            modulelist.set_module(module)
            result.append(modulelist)

        self._cnx.commit()
        cursor.close()

        return result

    def find_by_modulepart(self, modulepart):
        result = []
        cursor = self._cnx.cursor()
        command = "SELECT * FROM modulelist WHERE modulepart={} ORDER BY id".format(modulepart)
        cursor.execute(command)
        tuples = cursor.fetchall()

        for (id, creationdate, modulepart, module) in tuples:
            modulelist = ModuleList()
            modulelist.set_id(id)
            modulelist.set_creationdate(creationdate)
            modulelist.set_modulepart(modulepart)
            modulelist.set_module(module)
            result.append(modulelist)

        self._cnx.commit()
        cursor.close()

        return result

    def find_by_key(self, key):

        result = None

        cursor = self._cnx.cursor()
        command = "SELECT * modulelist WHERE id={}".format(key)
        cursor.execute(command)
        tuples = cursor.fetchall()

        try:
            (
                id, creationdate, modulepart, module) = tuples[0]
            modulelist = ModuleList()
            modulelist.set_id(id)
            modulelist.set_creationdate(creationdate)
            modulelist.set_modulepart(modulepart)
            modulelist.set_module(module)
            result.append(modulelist)

        except IndexError:
            result = None

        self._cnx.commit()
        cursor.close()

        return result

    def insert(self, modulelist):

        cursor = self._cnx.cursor()
        cursor.execute("SELECT MAX(id) AS maxid FROM modulelist ")
        tuples = cursor.fetchall()

        for (maxid) in tuples:
            if maxid[0] is not None:

                modulelist.set_id(maxid[0] + 1)
            else:

                modulelist.set_id(1)

        command = "INSERT INTO modulelist (id, creationdate, modulepart, module) VALUES (%s,%s,%s,%s) "
        data = (modulelist.get_id(), modulelist.get_creationdate(), modulelist.get_modulepart(), modulelist.get_module())
        cursor.execute(command, data)

        self._cnx.commit()
        cursor.close()

        return modulelist


    def update(self, modulelist):
        cursor = self._cnx.cursor()

        command = "UPDATE modulelist " + "SET module=%s, modulepart=%s WHERE id=%s"
        data = (modulelist.get_module(module),
                modulelist.get_modulepart(modulepart),
                modulelist.get__id())
        cursor.execute(command, data)

        self._cnx.commit()
        cursor.close()

    def delete(self, modulelist):
        cursor = self._cnx.cursor()

        command = "DELETE FROM modulelist WHERE id={}".format(modulelist.get_id())
        cursor.execute(command)

        self._cnx.commit()
        cursor.close()