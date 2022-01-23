from server.db.Mapper import Mapper
from server.bo.Spo import Spo
from server.bo.Semester import Semester


class SpoValidityMapper(Mapper):

    def __init__(self):
        super().__init__()

    """
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
    """
    def find_all(self):
        """Lies alle Tupel aus und gib sie als Objekte zurück."""
        pass

    def find_by_id(self, key):
        """Lies den einen Tupel mit der gegebenen ID (vgl. Primärschlüssel) aus."""
        pass

    def find_spo_by_semester_hash(self, hashcode: int):

        result = []

        cursor = self._cnx.cursor()
        command = f"SELECT spo_hash FROM spovalidity " \
                  f"WHERE semester_hash={hashcode} AND WHERE startsem=1"
        cursor.execute(command)
        tuples = cursor.fetchall()

        spos = []
        for (spo_hash) in tuples:
            cursor.execute(
                f"SELECT id, creationdate, name, title, studycourse_id FROM spo "
                f"WHERE spo_hash ={spo_hash}")
            spos.append(cursor.fetchall())
        for i in spos:
            for (id, creationdate, name, title, studycourse_id) in i:
                spo = Spo()
                spo.set_id(id)
                spo.set_name(name)
                spo.set_title(title)
                spo.set_studycourse(studycourse_id)
                result.append(spo)

        self._cnx.commit()
        cursor.close()

        return result

    def find_semester_by_spo_hash(self, hashcode: int):

        result = []

        cursor = self._cnx.cursor()
        command = f"SELECT semester_hash FROM spo WHERE id={hashcode}"
        cursor.execute(command)
        tuples = cursor.fetchall()

        scs = []
        for (semester_hash) in tuples:
            cursor.execute(
                f"SELECT id, creationdate, name, title FROM semester "
                f"WHERE semester_hash ={semester_hash}")
            scs.append(cursor.fetchall())
        for i in scs:
            for (id, creationdate, name, title) in i:
                semester = Semester()
                semester.set_id(id)
                semester.set_creationdate(creationdate)
                semester.set_name(name)
                semester.set_title(title)
                result.append(semester)

        self._cnx.commit()
        cursor.close()
        return result

    def insert(self, spo: Spo, endsemester=False):

        cursor = self._cnx.cursor()
        cursor.execute("SELECT MAX(id) AS maxid FROM spovalidity")
        newid = 1
        if cursor.fetchone()[0] is not None:
            newid += 1
        cursor.execute("SET FOREIGN_KEY_CHECKS=0")

        if not endsemester:
            cursor.execute(f"SELECT id FROM semester WHERE semester_hash={spo.get_start_semester()}")
            ssid = int(cursor.fetchone()[0])
            command = "INSERT INTO spovalidity VALUES " \
                      f"(id={newid}, spo_id={spo.get_id()}, spo_hash={hash(spo)}, " \
                      f"semester_id={ssid}, semester_hash={spo.get_start_semester()}, " \
                      f"startsem={1}, endsem={0}) "

        else:
            cursor.execute(f"SELECT id FROM semester WHERE semester_hash={spo.get_end_semester()}")
            esid = int(cursor.fetchone())
            command = "INSERT INTO spovalidity VALUES " \
                      f"(id={newid}, spo_id={spo.get_id()}, spo_hash={hash(spo)}, " \
                      f"semester_id={esid}, semester_hash={spo.get_end_semester()}, " \
                      f"startsem={0}, endsem={1}) "
        cursor.execute(command)
        cursor.execute("SET FOREIGN_KEY_CHECKS=1")
        self._cnx.commit()
        cursor.close()
        return spo

    def update(self, object):
        """Ein Objekt auf einen bereits in der DB enthaltenen Datensatz abbilden."""
        pass

    def delete(self, object):
        """Den Datensatz, der das gegebene Objekt in der DB repräsentiert löschen."""
        pass
