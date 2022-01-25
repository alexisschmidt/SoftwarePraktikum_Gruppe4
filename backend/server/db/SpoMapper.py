from server.bo.Spo import Spo
from server.db.Mapper import Mapper


class SpoMapper(Mapper):

    def __init__(self):
        super().__init__()

    def find_all(self):

        result = []
        cursor = self._cnx.cursor()
        cursor.execute("SELECT id, creationdate, name, title, studycourse_id FROM spo")
        tuples = cursor.fetchall()

        for (id, creationdate, name, title, studycourse_id) in tuples:
            spo = Spo()
            spo.set_id(id)
            spo.set_name(name)
            spo.set_title(title)
            spo.set_studycourse(studycourse_id)
            result.append(spo)

        self._cnx.commit()
        cursor.close()

        return result

    def find_by_name(self, name):

        result = []
        cursor = self._cnx.cursor()
        command = f"SELECT id, creationdate, name, title, studycourse_id " \
                  f"FROM spo WHERE name LIKE '{name}' ORDER BY name"
        cursor.execute(command)
        tuples = cursor.fetchall()

        for (id, creationdate, name, title, studycourse_id) in tuples:
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
        command = "SELECT id, creationdate, name, title, studycourse_id FROM spo WHERE spo_hash={}".format(hashcode)
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

    def find_all_by_studycourse(self, studycourse):
        result = []
        cursor = self._cnx.cursor()
        command = "SELECT id, creationdate, name, title, studycourse_id FROM spo " \
                  f"WHERE studycourse_id LIKE '{studycourse}' " \
                  "ORDER BY studycourse_id"
        cursor.execute(command)
        tuples = cursor.fetchall()

        try:
            (id, creationdate, name, title, studycourse) = tuples[0]
            spo = Spo()
            spo.set_id(id)
            spo.set_name(name)
            spo.set_title(title)
            spo.set_studycourse(studycourse)
            result = spo
        except IndexError:

            result = None

        self._cnx.commit()
        cursor.close()

        return result

    def find_latest_by_studycourse(self, studycourse):
        result = []
        cursor = self._cnx.cursor()
        command = "SELECT id, creationdate, name, title, studycourse_hash " \
                  f"FROM spo WHERE studycourse_hash = '{studycourse}' " \
                  "ORDER BY creationdate DESC LIMIT 1"
        cursor.execute(command)
        tuples = cursor.fetchall()

        for (id, creationdate, name, title, studycourse) in tuples:
            spo = Spo()
            spo.set_id(id)
            spo.set_name(name)
            spo.set_title(title)
            spo.set_studycourse(studycourse)

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

    def insert(self, spo: Spo, endsemester=False):

        cursor = self._cnx.cursor()
        cursor.execute("SELECT MAX(id) AS maxid FROM spovalidity")
        maxid = cursor.fetchone()[0]

        if maxid is None:
            newid = 1
        else:
            newid = maxid + 1

        # cursor.execute("SET FOREIGN_KEY_CHECKS=0")
        if endsemester is True:
            cursor.execute(f"SELECT id FROM semester WHERE semester_hash={spo.get_end_semester()}")
            esid = int(cursor.fetchone()[0])
            command = "INSERT INTO spovalidity (id, spo_id, spo_hash, semester_id, semester_hash, startsem, endsem) " \
                      "VALUES " \
                      f"(id={newid}, spo_id={spo.get_id()}, spo_hash={hash(spo)}, " \
                      f"semester_id={esid}, semester_hash={spo.get_end_semester()}, " \
                      f"startsem=0, endsem=1)"
        else:
            cursor.execute(f"SELECT id FROM semester WHERE semester_hash={spo.get_start_semester()}")
            ssid = int(cursor.fetchone()[0])
            command = "INSERT INTO spovalidity (id, spo_id, spo_hash, semester_id, semester_hash, startsem, endsem) " \
                      "VALUES " \
                      f"(id={newid}, spo_id={spo.get_id()}, spo_hash={hash(spo)}, " \
                      f"semester_id={ssid}, semester_hash={spo.get_start_semester()}, " \
                      f"startsem=1, endsem=0)"

        print(command)
        cursor.execute(command)
        # cursor.execute("SET FOREIGN_KEY_CHECKS=1")
        self._cnx.commit()
        cursor.close()
        return spo

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
