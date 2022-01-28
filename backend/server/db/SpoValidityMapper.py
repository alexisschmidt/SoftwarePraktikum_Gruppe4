from server.bo.Spo import Spo
from server.db.Mapper import Mapper


class SpoValidityMapper(Mapper):

    def __init__(self):
        super().__init__()

    def insert_validity(self, spo: Spo, valtype: bool):

        cursor = self._cnx.cursor()
        # bestimmen der ID der SpoValidity-Zeile
        cursor.execute("SELECT MAX(id) AS maxidv1 FROM spovalidity")
        tuples1 = cursor.fetchall()
        newidv1 = 1
        for (maxidv1) in tuples1:
            if maxidv1[0] is not None:
                newidv1 = maxidv1[0] + 1

        # spovalidity Zeile anlegen. Ist Endsemester nicht bestimmt, so wird nur für das Startsemester angelegt,
        # anderen Falls werden beide Einträge erstellt.
        startsemcommand = "INSERT INTO spovalidity (id, spo_hash, semester_hash, startsem, endsem) " \
                          "VALUES " \
                          f"(id={newidv1}, spo_hash={hash(spo)}, " \
                          f"semester_hash={spo.get_start_semester()}, " \
                          f"startsem=1, endsem=0)"

        cursor.execute("SELECT MAX(id) AS maxidv2 FROM spovalidity")
        tuples2 = cursor.fetchall()
        newidv2 = 1
        for (maxidv2) in tuples2:
            if maxidv2[0] is not None:
                newidv2 = maxidv2[0] + 1

        endsemcommand = "INSERT INTO spovalidity (id, spo_hash, semester_hash, startsem, endsem) " \
                        "VALUES " \
                        f"(id={newidv2}, spo_hash={hash(spo)}, " \
                        f"semester_hash={spo.get_end_semester()}, " \
                        f"startsem=0, endsem=1)"

        if valtype == 0:
            cursor.execute(startsemcommand)
        else:
            cursor.execute(startsemcommand)
            cursor.execute(endsemcommand)

        self._cnx.commit()
        cursor.close()
        return spo

    def copy_validity(self, copy: Spo, valtype: bool):
        cursor = self._cnx.cursor()

        # bestimmen der ID des kopierten SPO-Objekts
        # durch die neue ID ändert sich der hash der Kopie
        newid1 = 1
        newid2 = 1
        cursor.execute("SELECT MAX(id) AS maxid FROM spo")
        tuples = cursor.fetchall()
        for (maxid) in tuples:
            if maxid[0] is not None:
                newid1 = maxid[0] + 1

        cursor.execute("SELECT MAX(id) AS maxid FROM spo")
        tuples = cursor.fetchall()
        for (maxid) in tuples:
            if maxid[0] is not None:
                newid2 = maxid[0] + 1

        startsemcommand = "INSERT INTO spovalidity " \
                          f"VALUES ({newid1}, {hash(copy)}, {copy.get_start_semester()}, 1, 0"
        endsemcommand = "INSERT INTO spovalidity " \
                        f"VALUES ({newid2}, {hash(copy)}, {copy.get_end_semester()}, 0, 1"
        if valtype == 0:
            cursor.execute(startsemcommand)
        else:
            cursor.execute(startsemcommand)
            cursor.execute(endsemcommand)

        self._cnx.commit()
        cursor.close()
        return copy

    def find_validities_by_spo(self, spohash: int):
        cursor = self._cnx.cursor()

        startsemcommand = f"SELECT semester_hash FROM spovalidity WHERE spo_hash={spohash} AND startsem=1"
        endsemcommand = f"SELECT semester_hash FROM spovalidity WHERE spo_hash={spohash} AND endsem=1"

        cursor.execute(startsemcommand)
        startid = cursor.fetchone()

        cursor.execute(endsemcommand)
        endid = cursor.fetchone()
        return [startid, endid]

    def update_validity(self, spo: Spo, ids: list[int]):
        cursor = self._cnx.cursor()

        startsemcommand = f"UPDATE spovalidity " \
                          f"SET id={ids[0]}, " \
                          f"spo_hash={hash(spo)}, semester_hash={spo.get_start_semester()}, " \
                          f"startsem=1, endsem=0 " \
                          f"WHERE spo_hash= {hash(spo)}"

        endsemcommand = f"UPDATE spovalidity " \
                        f"SET id={ids[1]}, " \
                        f"spo_hash={hash(spo)}, semester_hash={spo.get_end_semester()}, " \
                        f"startsem=0, endsem=1 " \
                        f"WHERE spo_hash= {hash(spo)}"
        cursor.execute(startsemcommand)
        cursor.execute(endsemcommand)

        self._cnx.commit()
        cursor.close()
        return spo

    def find_all(self):
        """Lies alle Tupel aus und gib sie als Objekte zurück."""
        pass

    def find_by_hash(self, key):
        """Lies den einen Tupel mit dem gegebenen Hash (vgl. Primärschlüssel) aus."""
        pass

    def insert(self, businessobject):
        """Füge das folgende Objekt als Datensatz in die DB ein."""
        pass

    def update(self, businessobject):
        """Ein Objekt auf einen bereits in der DB enthaltenen Datensatz abbilden."""
        pass

    def delete(self, businessobject):
        """Den Datensatz, der das gegebene Objekt in der DB repräsentiert löschen."""
        pass
