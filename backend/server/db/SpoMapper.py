from operator import mod
from server.bo.Spo import Spo
from server.db.Mapper import Mapper


class SpoMapper(Mapper):

    def __init__(self):
        super().__init__()

    def find_all(self):

        result = []
        cursor = self._cnx.cursor()
        cursor.execute("SELECT spo_hash FROM spo")
        tuples = cursor.fetchall()

        for spo_hash in tuples:
            result.append(spo_hash[0])

        self._cnx.commit()
        cursor.close()

        return result

    def find_by_name(self, name: str):
        result = []
        cursor = self._cnx.cursor()
        command = f"SELECT spo_hash " \
                  f"FROM spo WHERE name LIKE '{name}' ORDER BY name"
        cursor.execute(command)
        tuples = cursor.fetchall()

        for spo_hash in tuples:
            result.append(spo_hash[0])

        self._cnx.commit()
        cursor.close()
        return result

    def find_by_hash(self, hashcode: int):
	
        result = None
        cursor = self._cnx.cursor()

        # finden der SPO in der DB:
        command = f"SELECT id, creationdate, createdby, name, title, studycourse_hash " \
                  f"FROM spo WHERE spo_hash={hashcode}"
        cursor.execute(command)
        tuples = cursor.fetchall()

        # finden der zugehörigen Module in der DB:
        cursor.execute(f"SELECT module_hash FROM spocomposition WHERE spo_hash={hashcode}")
        modules = list(cursor)
        
        if (modules is not None and len(modules)):
            modules = modules[0]
            if (modules is not None):
                modules = list(modules)
        
        # erstellen des Objekts
        try:
            (id, creationdate, createdby, name, title, studycourse_hash) = tuples[0]
            spo = Spo()
            spo.set_id(id)
            spo.set_creationdate(creationdate)
            spo.set_creator(createdby)
            spo.set_name(name)
            spo.set_title(title)
            spo.set_studycourse(studycourse_hash)
            result = spo
        except IndexError:
            result = None

        self._cnx.commit()
        cursor.close()
        return result

    def find_hash_by_id(self, id: int):
        result = None
        cursor = self._cnx.cursor()

        # finden der SPO in der DB:
        command = f"SELECT spo_hash " \
                  f"FROM spo WHERE id={id}"
        cursor.execute(command)
        tuples = cursor.fetchall()
        try:
            result = tuples[0][0]
        except IndexError:
            result = None

        self._cnx.commit()
        cursor.close()
        return result

    def find_all_by_studycourse(self, studycoursehash: int):
        result = []
        cursor = self._cnx.cursor()
        cursor.execute(f"SELECT spo_hash FROM spo "
                       f"WHERE studycourse_hash={studycoursehash}")
        tuples = cursor.fetchall()

        for spo_hash in tuples:
            result.append(spo_hash[0])

        self._cnx.commit()
        cursor.close()

        return result

    def find_latest_by_studycourse(self, studycoursehash: int):
        result = None
        cursor = self._cnx.cursor()
        command = "SELECT spo_hash " \
                  f"FROM spo WHERE studycourse_hash = '{studycoursehash}' " \
                  "ORDER BY creationdate DESC LIMIT 1"
        cursor.execute(command)
        tuples = cursor.fetchall()

        try:
            result = tuples[0][0]
        except IndexError:
            result = None

        self._cnx.commit()
        cursor.close()

        return result

    def find_by_startsemester_and_studycourse(self, semesterhash: int, studycoursehash: int):
        result = None
        cursor = self._cnx.cursor()
        command = "SELECT spo.spo_hash " \
                  "FROM spo " \
                  "LEFT JOIN spovalidity ON spo.spo_hash = spovalidity.spo_hash " \
                  f"WHERE semester_hash = {semesterhash} AND studycourse_hash = {studycoursehash}"
        cursor.execute(command)
        tuples = cursor.fetchall()

        try:
            result = tuples[0][0]
        except IndexError:
            result = None

        self._cnx.commit()
        cursor.close()

        return result

    def find_spos_by_semester_hash(self, hashcode: int):

        result = []

        cursor = self._cnx.cursor()
        command = f"SELECT spo_hash FROM spovalidity " \
                  f"WHERE semester_hash={hashcode} AND WHERE startsem=1"
        cursor.execute(command)
        tuples = cursor.fetchall()

        spos = []
        for (spo_hash) in tuples:
            cursor.execute(
                f"SELECT id, creationdate, name, title, studycourse_hash FROM spo "
                f"WHERE spo_hash ={spo_hash}")
            spos.append(cursor.fetchall())
        for i in spos:
            for (id, creationdate, name, title, studycourse_hash) in i:
                spo = Spo()
                spo.set_id(id)
                spo.set_name(name)
                spo.set_title(title)
                spo.set_studycourse(studycourse_hash)
                result.append(spo)

        self._cnx.commit()
        cursor.close()

        return result

    def insert(self, spo: Spo):

        cursor = self._cnx.cursor()
        # bestimmen der ID des SPO-Objeks
        cursor.execute("SELECT MAX(id) AS maxid FROM spo")
        tuples = cursor.fetchall()
        for (maxid) in tuples:
            if maxid[0] is not None:
                spo.set_id(maxid[0] + 1)
            else:
                spo.set_id(1)

        # anlegen des SPO-Objekts in der Datenbank.
        command = "INSERT INTO spo (id, creationdate, createdby, name, title, spo_hash, studycourse_hash) " \
                  "VALUES (%s,%s,%s,%s,%s,%s,%s)"
        data = (spo.get_id(), spo.get_creationdate(), spo.get_creator(), spo.get_name(), spo.get_title(),
                hash(spo), spo.get_studycourse())

        cursor.execute(command, data)
        self._cnx.commit()
        cursor.close()
        return spo

    def copy_spo(self, base: Spo, copy: Spo):

        cursor = self._cnx.cursor()
        # bestimmen der ID des kopierten SPO-Objeks
        # durch die neue ID ändert sich der hash der Kopie
        cursor.execute("SELECT MAX(id) AS maxid FROM spo")
        tuples = cursor.fetchall()
        for (maxid) in tuples:
            if maxid[0] is not None:
                copy.set_id(maxid[0] + 1)
            else:
                copy.set_id(1)

        command = "INSERT INTO spo " \
                  f"SELECT {copy.get_id()}, {copy.get_creationdate()}, {copy.get_creator()}, " \
                  f"name, title, {hash(copy)}, studycourse_hash " \
                  f"FROM spo " \
                  f"WHERE spo_hash ={hash(base)}"

        cursor.execute(command)
        self._cnx.commit()
        cursor.close()
        return copy

    def update(self, businessobject):
        pass

    def update_spo(self, base: Spo, new: Spo):

        cursor = self._cnx.cursor()

        command = f"UPDATE spo SET " \
                  f"id={new.get_id()}, creationdate={new.get_creationdate()}, createdby={new.get_creator()}, " \
                  f"name='{new.get_name()}', title='{new.get_title()}', " \
                  f"spo_hash={hash(new)}, studycourse_hash={new.get_studycourse()} " \
                  f"WHERE spo_hash={hash(base)}) "
        cursor.execute(command)

        self._cnx.commit()
        cursor.close()

    def delete(self, spo):

        cursor = self._cnx.cursor()
        cursor.execute("DELETE FROM spo "
                       f"WHERE spo_hash={hash(spo)}")
        self._cnx.commit()
        cursor.close()
