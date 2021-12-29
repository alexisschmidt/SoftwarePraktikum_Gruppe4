from server.bo.User import User
from backend.server.db.Mapper import Mapper


class UserMapper(Mapper):

    def __init__(self):
        super().__init__()

    def find_all(self):
        result = []
        cursor = self._cnx.cursor()
        cursor.execute("SELECT * from user")
        tuples = cursor.fetchall()

        for (id, creationdate, firstname, lastname, email) in tuples:
            user = User()
            user.set_id(id)
            user.set_firstname(firstname)
            user.set_lastname(lastname)
            user.set_email(email)

            result.append(user)

        self._cnx.commit()
        cursor.close()

        return result

    def find_by_name(self, name):

        result = []
        cursor = self._cnx.cursor()
        command = "SELECT * FROM user WHERE name LIKE '{}' ORDER BY name".format(name)
        cursor.execute(command)
        tuples = cursor.fetchall()

        for (id, creationdate, firstname, lastname, email) in tuples:
            user = User()
            user.set_id(id)
            user.set_firstname(firstname)
            user.set_lastname(lastname)
            user.set_email(email)

            result.append(user)

        self._cnx.commit()
        cursor.close()

        return result

    def find_by_key(self, key):

        result = None

        cursor = self._cnx.cursor()
        command = "SELECT * user WHERE id={}".format(key)
        cursor.execute(command)
        tuples = cursor.fetchall()

        try:
            (id, creationdate, firstname, lastname, email) = tuples[0]
            user = User()
            user.set_id(id)
            user.set_firstname(firstname)
            user.set_lastname(lastname)
            user.set_email(email)
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

        command = "INSERT INTO user (id, creationdate, firstname, lastname, email) VALUES (%s,%s,%s,%s,%s) "
        data = (user.get_id(), user.get_creationdate(), user.get_firstname(), user.get_lastname(), user.get_email())
        cursor.execute(command, data)

        self._cnx.commit()
        cursor.close()

        return user

    def update(self, user):

        cursor = self._cnx.cursor()

        command = "UPDATE user " + "SET firstname=%s, SET lastname=%s, SET email=%s WHERE id=%s "
        data = (user.get_firstname(), user.get.lastname(), user.getemail(), user.get_id())
        cursor.execute(command, data)

        self._cnx.commit()
        cursor.close()

    def delete(self, user):

        cursor = self._cnx.cursor()

        command = "DELETE FROM user WHERE id={}".format(user.get_id())
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
        command = "SELECT id, creationdate, title, firstname, lastname, email, google_user_id FROM user WHERE google_user_id='{}'".format(google_user_id)
        cursor.execute(command)
        tuples = cursor.fetchall()

        try:
            (id, creationdate, firstname, lastname, email, google_user_id) = tuples[0]
            u = User()
            u.set_id(id)
            u.set_creationdate(creationdate)
            u.set_firstname(firstname)
            u.set_lastname(lastname)
            u.set_email(email)
            u.set_user_id(google_user_id)
            result = u
        except IndexError:
            """Der IndexError wird oben beim Zugriff auf tuples[0] auftreten, wenn der vorherige SELECT-Aufruf
            keine Tupel liefert, sondern tuples = cursor.fetchall() eine leere Sequenz zurück gibt."""
            result = None

        self._cnx.commit()
        cursor.close()

        return result


