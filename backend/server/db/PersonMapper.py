from server.bo.Person import Person
from .Mapper import Mapper


class PersonMapper(Mapper):

    def __init__(self):
        super().__init__()

    def find_all(self):

        result = []
        cursor = self._cnx.cursor()
        cursor.execute("SELECT * from person")
        tuples = cursor.fetchall()

        for (id, creationdate, firstname, lastname, email) in tuples:
            person = Person()
            person.set_id(id)
            person.set_firstname(firstname)
            person.set_lastname(lastname)
            person.set_email(email)

            result.append(person)

        self._cnx.commit()
        cursor.close()

        return result

    def find_by_name(self, name):

        result = []
        cursor = self._cnx.cursor()
        command = "SELECT * FROM person WHERE name LIKE '{}' ORDER BY name".format(name)
        cursor.execute(command)
        tuples = cursor.fetchall()

        for (id, creationdate, firstname, lastname, email) in tuples:
            person = Person()
            person.set_id(id)
            person.set_firstname(firstname)
            person.set_lastname(lastname)
            person.set_email(email)

            result.append(person)

        self._cnx.commit()
        cursor.close()

        return result

    def find_by_id(self, key):

        result = None

        cursor = self._cnx.cursor()
        command = "SELECT * person WHERE id={}".format(key)
        cursor.execute(command)
        tuples = cursor.fetchall()

        try:
            (id, creationdate, name, firstname, lastname, email) = tuples[0]
            person = Person()
            person.set_id(id)
            person.set_firstname(firstname)
            person.set_lastname(lastname)
            person.set_email(email)
            result = person
        except IndexError:

            result = None

        self._cnx.commit()
        cursor.close()

        return result

    def find_by_hash(self, hashcode):

        result = None

        cursor = self._cnx.cursor()
        command = "SELECT * person WHERE person_hash={}".format(hashcode)
        cursor.execute(command)
        tuples = cursor.fetchall()

        try:
            (id, creationdate, firstname, lastname, email) = tuples[0]
            person = Person()
            person.set_id(id)
            person.set_firstname(firstname)
            person.set_lastname(lastname)
            person.set_email(email)
            result = person
        except IndexError:

            result = None

        self._cnx.commit()
        cursor.close()

        return result

    def insert(self, person):

        cursor = self._cnx.cursor()
        cursor.execute("SELECT MAX(id) AS maxid FROM person")
        tuples = cursor.fetchall()

        for (maxid) in tuples:
            if maxid[0] is not None:
                person.set_id(maxid[0] + 1)
            else:
                person.set_id(1)

        command = "INSERT INTO person (id, creationdate, firstname, lastname, email, person_hash) VALUES (%s,%s,%s,%s,%s,%s)"
        data = (person.get_id(), person.get_creationdate(), person.get_firstname(), person.get_lastname(), person.get_email(), hash(person))
        cursor.execute(command, data)

        self._cnx.commit()
        cursor.close()

        return person

    def update(self, person):

        cursor = self._cnx.cursor()

        command = "UPDATE person " \
                  "SET firstname=%s, lastname=%s, email=%s " \
                  "WHERE id=%s "
        data = (person.get_firstname(), person.get_lastname(), person.get_email(), person.get_id())
        cursor.execute(command, data)

        self._cnx.commit()
        cursor.close()

    def delete(self, person):

        cursor = self._cnx.cursor()

        command = "DELETE FROM person WHERE id={}".format(person.get_id())
        cursor.execute(command)

        self._cnx.commit()
        cursor.close()
