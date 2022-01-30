from server.bo.User import User
from server.db.Mapper import Mapper


class UserMapper(Mapper):

    def __init__(self):
        super().__init__()

    def find_all(self):
        result = []
        cursor = self._cnx.cursor()
        cursor.execute("SELECT id, creationdate, "
                       "firstname, lastname, email, "
                       "google_user_id, isadmin, spo_hash FROM user")
        tuples = cursor.fetchall()

        for (id, creationdate, firstname, lastname, email, google_user_id, isadmin, spo_hash) in tuples:
            user = User()
            user.set_id(id)
            user.set_firstname(firstname)
            user.set_lastname(lastname)
            user.set_email(email)
            user.set_google_user_id(google_user_id)
            user.set_isadmin(isadmin)
            user.set_spo(spo_hash)
            result.append(user)

        self._cnx.commit()
        cursor.close()

        return result

    def find_by_name(self, name):

        result = []
        cursor = self._cnx.cursor()
        command = f"SELECT * FROM user WHERE lastname LIKE '{name}' ORDER BY lastname"
        cursor.execute(command)
        tuples = cursor.fetchall()

        for (id, creationdate, firstname, lastname, email, google_user_id, isadmin) in tuples:
            user = User()
            user.set_id(id)
            user.set_creationdate(creationdate)
            user.set_firstname(firstname)
            user.set_lastname(lastname)
            user.set_email(email)
            user.set_google_user_id(google_user_id)
            user.set_isadmin(isadmin)

            result.append(user)

        self._cnx.commit()
        cursor.close()

        return result

    def find_by_hash(self, hashcode):
	
        result = None

        cursor = self._cnx.cursor()
        command = f"SELECT * FROM user WHERE user_hash={hashcode}"
        cursor.execute(command)
        tuples = cursor.fetchall()

        try:
            (id, creationdate, createdby, firstname, lastname, email, google_user_id, isadmin, user_hash, spo_hash) = tuples[0]
            user = User()
            user.set_id(id)
            user.set_creationdate(creationdate)
            user.set_creator(createdby)
            user.set_firstname(firstname)
            user.set_lastname(lastname)
            user.set_email(email)
            user.set_google_user_id(google_user_id)
            user.set_isadmin(isadmin)
            result = user
        except IndexError:

            result = None

        self._cnx.commit()
        cursor.close()

        return result

    def insert(self, user):

        cursor = self._cnx.cursor()
        cursor.execute("SELECT MAX(id) AS maxid FROM user ")
        tuples = cursor.fetchall()

        for (maxid) in tuples:
            if maxid[0] is not None:

                user.set_id(maxid[0] + 1)
            else:

                user.set_id(1)

        command = "INSERT INTO user (id, creationdate, createdby, " \
                  "firstname, lastname, email, google_user_id, isadmin, user_hash, spo_hash) "\
                  "VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
        data = (user.get_id(), user.get_creationdate(), user.get_creator(),
                user.get_firstname(), user.get_lastname(), user.get_email(),
                user.get_google_user_id(), user.get_isadmin(), hash(user), user.get_spo())
        cursor.execute(command, data)

        self._cnx.commit()
        cursor.close()

        return user

    def update(self, user):

        cursor = self._cnx.cursor()

        command = "UPDATE user SET firstname=%s, lastname=%s, email=%s, google_user_id=%s, isadmin=%s WHERE id=%s AND" \
                  " user_hash=%s "
        data = (user.get_firstname(), user.get_lastname(), user.get_email(), user.get_google_user_id(),
                user.get_isadmin(), user.get_id(), hash(user))
        command = "UPDATE user SET firstname=%s, lastname=%s, email=%s, google_user_id=%s, isadmin=%s WHERE id=%s "
        data = (
            user.get_firstname(), user.get_lastname(), user.get_email(), user.get_google_user_id(), user.get_isadmin(),
            user.get_id())
        cursor.execute(command, data)

        self._cnx.commit()
        cursor.close()

    def delete(self, user):

        cursor = self._cnx.cursor()

        command = f"DELETE FROM user WHERE user_hash={hash(user)}"
        cursor.execute(command)

        self._cnx.commit()
        cursor.close()

    def find_by_google_user_id(self, google_user_id):
        """Suchen eines Benutzers mit vorgegebener Google ID. Da diese eindeutig ist,
        wird genau ein Objekt zurückgegeben.

        :param google_user_id die Google ID des gesuchten Users.
        :return User-Objekt, das die übergebene Google ID besitzt,
            None bei nicht vorhandenem DB-Tupel.
        """
        result = None

        cursor = self._cnx.cursor()
        command = "SELECT id, creationdate, createdby, firstname, lastname, email, google_user_id, user_hash, spo_hash " \
                  "FROM user " \
                  f"WHERE google_user_id='{google_user_id}'"
        cursor.execute(command)
        tuples = cursor.fetchall()


        try:
            (id, creationdate, createdby, firstname, lastname, email, google_user_id, isadmin, user_hash, spo_hash) = tuples[0]
            user = User()
            user.set_id(id)
            user.set_creator(createdby)
            user.set_creationdate(creationdate)
            user.set_firstname(firstname)
            user.set_lastname(lastname)
            user.set_email(email)
            user.set_google_user_id(google_user_id)
            user.set_isadmin(isadmin)
            user.set_spo(spo_hash)
            result = user
        except IndexError:
            # Der IndexError wird oben beim Zugriff auf tuples[0] auftreten, wenn der vorherige SELECT-Aufruf
            # keine Tupel liefert, sondern tuples = cursor.fetchall() eine leere Sequenz zurückgibt.
            result = None

        self._cnx.commit()
        cursor.close()

        return result
