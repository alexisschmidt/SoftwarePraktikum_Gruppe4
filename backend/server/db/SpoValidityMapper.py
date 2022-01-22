from server.bo.SpoValidity import SpoValidity
from server.db.Mapper import Mapper

class SpoValidityMapper(Mapper):

    def __init__(self):
        super().__init__()

    def find_all(self):

        result = []
        cursor = self._cnx.cursor()
        cursor.execute("SELECT spo_id, semester_id, startsem, endsem FROM spovalidity")
        tuples = cursor.fetchall()

        for (spo_id, semester_id, startsem, endsem) in tuples:
            spov = SpoValidity()
            spov.set_spo_id(spo_id)
            spov.set_semester_id(semester_id)
            spov.set_startsem(startsem)
            spov.set_endsem(endsem)
            result.append(spo)

        self._cnx.commit()
        cursor.close()

        return result

    def find_by_id(self, key):

        result = None

        cursor = self._cnx.cursor()
        command = "SELECT spo_id, semester_id, startsem, endsem FROM spo WHERE spo_id={}".format(key)
        cursor.execute(command)
        tuples = cursor.fetchall()

        try:
            (spo_id, semester_id, startsem, endsem) = tuples[0]
            spov = SpoValidity()
            spov.set_spo_id(spo_id)
            spov.set_semester_id(semester_id)
            spov.set_startsem(startsem)
            spov.set_endsem(endsem)
            result = spov
        except IndexError:

            result = None

        self._cnx.commit()
        cursor.close()

        return result

    def find_by_spo_id(self, spo_id):

        result = None

        cursor = self._cnx.cursor()
        command = "spo_id, spo_hash, semester_id, semester_semester_hash, startsem, endsem FROM spo WHERE spo_id={}".format(spo_id)
        cursor.execute(command)
        tuples = cursor.fetchall()

        try:
            (spo_id, spo_hash, semester_id, semester_semester_hash, startsem, endsem) = tuples[0]
            spov = SpoValidity()
            spov.set_spo_id(spo_id)
            spov.set_spo_hash(spo_hash)
            spov.set_semester_id(semester_id)
            spov.set_semester_semester_hash(semester_semester_hash)
            spov.set_startsem(startsem)
            spov.set_endsem(endsem)
            result = spov
        except IndexError:

            result = None

        self._cnx.commit()
        cursor.close()

        return result

    def insert(self, spov):

        cursor = self._cnx.cursor()
        cursor.execute("SELECT MAX(id) AS maxid FROM spovalidity")
        tuples = cursor.fetchall()

        for (maxid) in tuples:
            if maxid[0] is not None:

                spov.set_id(maxid[0] + 1)
            else:

                spov.set_id(1)


        command = "INSERT INTO spovalidity (spo_id, spo_hash, semester_id, semester_semester_hash, startsem, endsem) VALUES (%s,%s,%s,%s,%s,%s)"
        data = (spo.get_spo_id(), spo.get_spo_hash(), spo.get_semester_id(), spo.get_semester_semester_hash(), spo.get_startsem(), spo.get_endsem())
        print(data)
        cursor.execute(command, data)

        self._cnx.commit()
        cursor.close()

        return spov