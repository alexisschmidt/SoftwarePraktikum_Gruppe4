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
        command = "SELECT id, creationdate, name, title, studycourse_id FROM spo WHERE name LIKE '{}' ORDER BY name".format(name)
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
        command = "SELECT id, creationdate, name, title, studycourse_id FROM spo WHERE id={}".format(key)
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
        command ="SELECT spo.id, spo.creationdate, spo.name, spo.title, spo.studycourse_hash " \
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

    def insert(self, spo: Spo):

        cursor = self._cnx.cursor()
        cursor.execute("SELECT MAX(id) AS maxid FROM spo")
        tuples = cursor.fetchall()

        for (maxid) in tuples:
            if maxid[0] is not None:
                spo.set_id(maxid[0] + 1)
            else:
                spo.set_id(1)

        try:
            cursor.execute(f'SELECT id FROM studycourse WHERE studycourse_hash={spo.get_studycourse()}')
            sc = int(cursor.fetchone()[0])
        except ValueError:
            print('spo needs an studycourse to be created!')


        command = "INSERT INTO spo (id, creationdate, name, title, spo_hash, studycourse_id, studycourse_hash) VALUES (%s,%s,%s,%s,%s,%s,%s)"
        data = (spo.get_id(), spo.get_creationdate(), spo.get_name(), spo.get_title(), hash(spo), sc, spo.get_studycourse())
        cursor.execute(command, data)

        self._cnx.commit()
        cursor.close()

        return spo

    def update(self, spo):

        cursor = self._cnx.cursor()

        command = "UPDATE spo " + "SET name=%s, SET title=%s, SET spo_hash=%s, SET studycourse_id=%s, SET get_studycourse_studycourse_hash=%s WHERE id=%s "
        data = (spo.get_name(), spo.get_title(), spo.get_start_semester(), spo.get_end_semester(), spo.get_studycourse(), spo.get_id())
        cursor.execute(command, data)

        self._cnx.commit()
        cursor.close()

    def delete(self, spo):

        cursor = self._cnx.cursor()

        command = "DELETE FROM spo WHERE spo_hash={}".format(hash(spo))
        cursor.execute(command)

        self._cnx.commit()
        cursor.close()
