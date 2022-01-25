from server.bo.Spo import Spo
from server.db.Mapper import Mapper


class SpoMapper(Mapper):

    def __init__(self):
        super().__init__()

    def find_all(self):

        result = []
        cursor = self._cnx.cursor()
        cursor.execute("SELECT id, creationdate, name, title, studycourse_hash FROM spo")
        tuples = cursor.fetchall()

        for (id, creationdate, name, title, studycourse_hash) in tuples:
            spo = Spo()
            spo.set_id(id)
            spo.set_name(name)
            spo.set_title(title)
            spo.set_studycourse(studycourse_hash)
            result.append(spo)

        self._cnx.commit()
        cursor.close()

        return result

    def find_by_name(self, name):

        result = []
        cursor = self._cnx.cursor()
        command = f"SELECT id, creationdate, name, title, studycourse_hash " \
                  f"FROM spo WHERE name LIKE '{name}' ORDER BY name"
        cursor.execute(command)
        tuples = cursor.fetchall()

        for (id, creationdate, name, title, studycourse_id) \
                in tuples:
            spo = Spo()
            spo.set_id(id)
            spo.set_name(name)
            spo.set_title(title)
            spo.set_studycourse(studycourse_id)
            result.append(spo)

        self._cnx.commit()
        cursor.close()

        return result

    def find_by_id(self, key):

        result = None

        cursor = self._cnx.cursor()
        command = f"SELECT id, creationdate, name, title, studycourse_id FROM spo WHERE id={key}"
        cursor.execute(command)
        tuples = cursor.fetchall()

        try:
            (id, creationdate, name, title, studycourse_id) = tuples[0]
            spo = Spo()
            spo.set_id(id)
            spo.set_name(name)
            spo.set_title(title)
            spo.set_studycourse(studycourse_id)
            result = spo
        except IndexError:

            result = None

        self._cnx.commit()
        cursor.close()

        return result

    def find_by_hash(self, hashcode):

        result = None
        cursor = self._cnx.cursor()

        # finden der SPO in der DB:
        command = f"SELECT id, creationdate, createdby, name, title, studycourse_hash FROM spo WHERE spo_hash={hashcode}"
        cursor.execute(command)
        tuples = cursor.fetchall()

        # finden der zugehörigen Module in der DB:
        cursor.execute(f"SELECT module_hash FROM spocomposition WHERE spo_hash={hashcode}")
        modules = list(cursor)

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
            spo.set_modules(modules)
            result = spo
        except IndexError:
            result = None

        self._cnx.commit()
        cursor.close()
        return result

    def find_all_by_studycourse(self, studycoursehash):
        result = []
        cursor = self._cnx.cursor()

        # finden der SPOs in der DB:
        command = "SELECT * FROM spo " \
                  f"WHERE studycourse_hash ={studycoursehash}"
        cursor.execute(command)
        tuples = cursor.fetchall()
        # Erstellen einer Liste von Objekten
        for (id, creationdate, createdby, name, title, spo_hash, studycourse_hash) \
                in tuples:
            cursor.execute(f"SELECT module_hash FROM spocomposition WHERE spo_hash={spo_hash}")
            modules = [cursor.fetchall]
            spo = Spo()
            spo.set_id(id)
            spo.set_creationdate(creationdate)
            spo.set_creator(createdby)
            spo.set_name(name)
            spo.set_title(title)
            spo.set_studycourse(studycourse_hash)
            spo.set_modules()
            result.append(spo)

        self._cnx.commit()
        cursor.close()
        return result

    def find_latest_by_studycourse(self, studycourse):
        result = []
        cursor = self._cnx.cursor()
        command = "SELECT id, creationdate, createdby, name, title, studycourse_hash " \
                  f"FROM spo WHERE studycourse_hash = '{studycourse}' " \
                  "ORDER BY creationdate DESC LIMIT 1"
        cursor.execute(command)
        tuples = cursor.fetchall()

        for (id, creationdate, createdby, name, title, studycourse_hash) in tuples:
            spo = Spo()
            spo.set_id(id)
            spo.get_creationdate(creationdate)
            spo.get_creator(createdby)
            spo.set_name(name)
            spo.set_title(title)
            spo.set_studycourse(studycourse_hash)

            result.append(spo)

        self._cnx.commit()
        cursor.close()

        return result

    def find_by_startsemester_and_studycourse(self, semesterhash, studycoursehash):
        result = None
        cursor = self._cnx.cursor()
        command = "SELECT spo.id, spo.creationdate, spo.name, spo.title, spo.studycourse_hash " \
                  "FROM spo " \
                  "LEFT JOIN spovalidity ON spo.spo_hash = spovalidity.spo_hash " \
                  f"WHERE semester_hash = {semesterhash} AND studycourse_hash = {studycoursehash}"
        cursor.execute(command)
        tuples = cursor.fetchall()

        try:
            (id, creationdate, name, title, studycourse_hash) = tuples[0]
            spo = Spo()
            spo.set_id(id)
            spo.set_name(name)
            spo.set_title(title)
            spo.set_studycourse(studycourse_hash)
            result = spo
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
        command = f"SELECT semester_hash FROM spovalidity WHERE spo_hash={hashcode}"
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

    def insert(self, spo: Spo):

        cursor = self._cnx.cursor()
        cursor.execute("SELECT MAX(id) AS maxid FROM spo")
        tuples = cursor.fetchall()

        for (maxid) in tuples:
            if maxid[0] is not None:
                spo.set_id(maxid[0] + 1)
            else:
                spo.set_id(1)

        command = "INSERT INTO spo (id, creationdate, createdby, name, title, spo_hash, studycourse_hash) " \
                  "VALUES (%s,%s,%s,%s,%s,%s,%s)"
        data = (spo.get_id(), spo.get_creationdate(), spo.get_creator(), spo.get_name(), spo.get_title(),
                hash(spo), spo.get_studycourse())
        cursor.execute(command, data)

        cursor.execute("SELECT MAX(id) AS maxidv FROM spovalidity")
        tuples = cursor.fetchall()

        for (maxidv) in tuples:
            if maxidv[0] is not None:
                newid = maxidv[0] + 1
            else:
                newid = 1

        startsemcommand = "INSERT INTO spovalidity (id, spo_hash, semester_hash, startsem, endsem) " \
                          "VALUES " \
                          f"(id={newid}, spo_hash={hash(spo)}, " \
                          f"semester_hash={spo.get_start_semester()}, " \
                          f"startsem=1, endsem=0)"
        endsemcommand = "INSERT INTO spovalidity (id, spo_hash, semester_hash, startsem, endsem) " \
                        "VALUES " \
                        f"(id={newid}, spo_hash={hash(spo)}, " \
                        f"semester_hash={spo.get_end_semester()}, " \
                        f"startsem=0, endsem=1)"

        if spo.get_end_semester() == 0:
            cursor.execute(startsemcommand)
        else:
            cursor.execute(startsemcommand)
            cursor.execute(endsemcommand)

        self._cnx.commit()
        cursor.close()
        return spo

    def update(self, spo):

        cursor = self._cnx.cursor()

        command = "UPDATE spo " + "SET name=%s, SET title=%s, SET spo_hash=%s, " \
                                  "SET studycourse_id=%s, SET get_studycourse_studycourse_hash=%s " \
                                  "WHERE id=%s "
        data = (spo.get_spo(), spo.get_semester(),
                spo.get_start_semester(), spo.get_end_semester(), spo.get_studycourse(), spo.get_id())
        cursor.execute(command, data)

        self._cnx.commit()
        cursor.close()

    def delete(self, spo):

        cursor = self._cnx.cursor()

        command = "DELETE FROM spo WHERE spo_hash={}".format(hash(spo))
        cursor.execute(command)

        self._cnx.commit()
        cursor.close()
