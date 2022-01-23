from server.bo.SpoComposotion import SpoComposition
from server.db.Mapper import Mapper


class SpoCompositionMapper(Mapper):

    def __init__(self):
        super().__init__()

    def find_all(self):
        result = []
        cursor = self._cnx.cursor()

        cursor.execute("SELECT id, module_id, spo_id from spocomposition")
        tuples = cursor.fetchall()

        for (id, module_id, module_hash, spo_id, spo_hash) in tuples:
            spoc = SpoComposition()
            spoc.set_id(id)
            spoc.set_module_id(module_id)
            spoc.set_spo_id(spo_id)
            result.append(spoc)

        self._cnx.commit()
        cursor.close()

        return result

    def find_by_module(self, module_id):
        result = []
        cursor = self._cnx.cursor()
        command = "SELECT id, module_id, spo_id,  FROM spocomposition WHERE module_id={} ORDER BY module_id".format(module_id)
        cursor.execute(command)
        tuples = cursor.fetchall()

        for (id, module_id, spo_id) in tuples:
            spoc = SpoComposition()
            spoc.set_id(id)
            spoc.set_module_id(module_id)
            spoc.set_spo_id(spo_id)
            result.append(spoc)

        self._cnx.commit()
        cursor.close()

        return result


    def find_by_spo_id(self, spo_id):
        result = []
        cursor = self._cnx.cursor()
        command = "SELECT id, module_id, spo_id, FROM spocomposition WHERE spo_id={} ORDER BY spo_id".format(spo_id)
        cursor.execute(command)
        tuples = cursor.fetchall()

        for (id, module_id, module_hash, spo_id, spo_hash) in tuples:
            spoc = SpoComposition()
            spoc.set_id(id)
            spoc.set_module_id(module_id)
            spoc.set_spo_id(spo_id)
            result.append(spoc)

        self._cnx.commit()
        cursor.close()

        return result

    def find_by_id(self, key):

        result = None

        cursor = self._cnx.cursor()
        command = "SELECT id, module_id, spo_id, FROM spocomposition WHERE id={}".format(key)
        cursor.execute(command)
        tuples = cursor.fetchall()

        try:
            (id, module_id, spo_id) = tuples[0]
            spoc = SpoComposition()
            spoc.set_id(id)
            spoc.set_module_id(module_id)
            spoc.set_spo_id(spo_id)
            result.append(spoc)

        except IndexError:
            result = None

        self._cnx.commit()
        cursor.close()

        return result

    def insert(self, spoc):

        cursor = self._cnx.cursor()
        cursor.execute("SELECT MAX(id) AS maxid FROM spocomposition ")
        tuples = cursor.fetchall()

        for (maxid) in tuples:
            if maxid[0] is not None:

                spoc.set_id(maxid[0] + 1)
            else:

                spoc.set_id(1)

        command = "INSERT INTO spocomposition (id, module_id, module_hash, spo_id, spo_hash) VALUES (%s,%s,%s,%s,%s) "
        data = (
        spoc.get_id(), spoc.get_module_id(), spoc.get_module_hash(), spoc.get_spo_id(), spoc.get_spo_hash())
        cursor.execute(command, data)

        self._cnx.commit()
        cursor.close()

        return spoc

    def update(self, spoc):
        cursor = self._cnx.cursor()

        command = "UPDATE spocomposition " + "SET module_id=%s, spo_id=%s WHERE id=%s"
        data = (
        spoc.get_id(), spoc.get_module_id(), spoc.get_spo_id())
        cursor.execute(command, data)

        self._cnx.commit()
        cursor.close()

    def delete(self, spoc):
        cursor = self._cnx.cursor()

        command = "DELETE FROM spocomposition WHERE id={}".format(spoc.get_id())
        cursor.execute(command)

        self._cnx.commit()
        cursor.close()
