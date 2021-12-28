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
        data = (user.get_firstname(), user_get.lastname(), user_getemail(), userget_id())
        cursor.execute(command, data)

        self._cnx.commit()
        cursor.close()

    def delete(self, user):

        cursor = self._cnx.cursor()

        command = "DELETE FROM user WHERE id={}".format(user.get_id())
        cursor.execute(command)

        self._cnx.commit()
        cursor.close()


