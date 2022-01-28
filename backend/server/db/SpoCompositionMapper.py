from server.bo.Spo import Spo
from server.db.Mapper import Mapper


class SpoCompositionMapper(Mapper):

    def __init__(self):
        super().__init__()

    def insert_compositions(self, spo: Spo):

        cursor = self._cnx.cursor()
        for module_hash in spo.get_modules():

            # bestimmen der ID der SpoComposition-Zeile
            newid = 1
            cursor.execute("SELECT MAX(id) AS maxid FROM spocomposition")
            tuples = cursor.fetchall()
            for (maxid) in tuples:
                if maxid[0] is not None:
                    newid = maxid[0] + 1

            # Erstellen der Zeile
            cursor.execute("INSERT INTO spocomposition (id, module_hash, spo_hash) "
                           "VALUES "
                           f"(id={newid}, module_hash={module_hash}, spo_hash={hash(spo)})")

        self._cnx.commit()
        cursor.close()
        return spo

    def copy_composition(self, copy: Spo):

        cursor = self._cnx.cursor()
        for module_hash in copy.get_modules():
            # bestimmen der ID der SpoComposotion-Zeile
            newidc = 1
            cursor.execute("SELECT MAX(id) AS maxidc FROM spocomposition")
            tuples = cursor.fetchall()
            for (maxidc) in tuples:
                if maxidc[0] is not None:
                    newidc = maxidc[0] + 1
                    # Erstellen der Zeile
            cursor.execute("INSERT INTO spocomposition (id, module_hash, spo_hash) "
                           "VALUES "
                           f"(id={newidc}, module_hash={module_hash}, spo_hash={hash(copy)})")

            self._cnx.commit()
            cursor.close()
            return copy

    def get_composition_id(self, spo: Spo):
        cursor = self._cnx.cursor()
        result = []

        for module in spo.get_modules():
            mo = cursor.execute(f"SELECT id FROM spocomposition "
                                f"WHERE spo_hash={hash(spo)} "
                                f"AND module_hash={module} ")
            result.append(mo)

        return result

    def update_composition(self, spo: Spo, modules: list[int]):
        cursor = self._cnx.cursor()
        modulenumber = -1
        for id in modules:
            modulenumber += 1
            cursor.execute(f"UPDATE spocomposition SET id={id}, module_hash={spo.get_modules()[modulenumber]} "
                           f"WHERE spo_hash={hash(spo)}")

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
