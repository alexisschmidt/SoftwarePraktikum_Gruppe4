import datetime

from server.bo.Module import Module
from server.bo.Modulepart import Modulepart
from server.bo.Person import Person
from server.bo.Semester import Semester
from server.bo.Spo import Spo
from server.bo.StudyCourse import StudyCourse
from server.bo.User import User

from server.db.ModuleMapper import ModuleMapper
from server.db.ModulePartMapper import ModulePartMapper
from server.db.PersonMapper import PersonMapper
from server.db.SemesterMapper import SemesterMapper
from server.db.SpoMapper import SpoMapper
from server.db.SpoValidityMapper import SpoValidityMapper
from server.db.SpoCompositionMapper import SpoCompositionMapper
from server.db.StudyCourseMapper import StudyCourseMapper
from server.db.UserMapper import UserMapper


class Administration (object):
    def __init__(self):
        pass
   
    """Spo-spezifische Methoden"""

    def create_spo(self, proposal: Spo, creator):
        """
        Legt das Objekt in der Datenbank an und setzt creationate und creator,
        wenn das Zielobjekt noch nicht in der DB existiert.

        Zusätzlich wird für eine SPO ein bzw. 2 Einträge in spovalidity erstellt,
        die die Attribute _start_semester und _end_semester darstellen und Einträge in spocomposition,
        die die Module einer SPO darstellen

        :param proposal: Ein Spo Objekt
        :param creator: Ein User, creator des Objekts
        """
        proposal.set_creationdate(datetime.date.today())
        proposal.set_creator(hash(creator))
        # Gibt es diese SPO schon?
        with SpoMapper() as mapper:
            spo = mapper.find_by_hash(hash(proposal))

        if spo is None:
            # Ist schon ein Ende der Gültigkeit angegeben?
            if proposal.get_end_semester() != 0:
                valtype = True
            else:
                valtype = False
            with SpoMapper() as mapper:
                newobj = mapper.insert(proposal)
            with SpoValidityMapper() as mapper:
                mapper.insert_validity(proposal, valtype)
            with SpoCompositionMapper() as mapper:
                mapper.insert_compositions(proposal)
            return newobj
        else:
            return spo

    def get_spo_by_hash(self, hashcode):
        """Die SPO mit dem gegebenem Hash auslesen."""
        with SpoMapper() as mapper:
            result = mapper.find_by_hash(hashcode)
        with SpoValidityMapper() as mapper:
            val = mapper.find_validities_by_spo(hashcode)
            result.set_start_semester(val[0])
            result.set_end_semester(val[1])
        with ModuleMapper() as mapper:
            modules = mapper.find_by_spo(hashcode)
            result.set_modules(modules)
        return result

    def get_spo_by_id(self, id: int):
        """Die SPO mit der gegebenen ID auslesen."""
        with SpoMapper() as mapper:
            spo = mapper.find_hash_by_id(id)
            result = mapper.find_by_hash(spo)
        with SpoValidityMapper() as mapper:
            val = mapper.find_validities_by_spo(spo)
            result.set_start_semester(val[0])
            result.set_end_semester(val[1])
        with ModuleMapper() as mapper:
            modules = mapper.find_by_spo(spo)
            result.set_modules(modules)
        return result

    def get_latest_by_studycourse(self, studycourse):
        """Die aktuelle SPO eines Studienganges auslesen"""
        with SpoMapper() as mapper:
            spo = mapper.find_by_latest_creationdate(studycourse)
            result = mapper.find_by_hash(spo)
        with SpoValidityMapper() as mapper:
            val = mapper.find_validities_by_spo(spo)
            result.set_start_semester(val[0])
            result.set_end_semester(val[1])
        with ModuleMapper() as mapper:
            modules = mapper.find_by_spo(spo)
            result.set_modules(modules)
        return result

    def get_spo_by_startsem_studycourse(self, semesterhash: int, studycoursehash: int):
        """Die Spo mit den ausgewählten Startsemester und Studiengang auslesen."""
        with SpoMapper() as mapper:
            spo = mapper.find_by_startsemester_and_studycourse(semesterhash, studycoursehash)
            result = mapper.find_by_hash(spo)
        with SpoValidityMapper() as mapper:
            val = mapper.find_validities_by_spo(spo)
            result.set_start_semester(val[0])
            result.set_end_semester(val[1])
        with ModuleMapper() as mapper:
            modules = mapper.find_by_spo(spo)
            result.set_modules(modules)
        return result

    def get_all_spos(self):
        """Alle SPOs auslesen."""
        result = []
        with SpoMapper() as mapper:
            spos = mapper.find_all()
        for hashcode in spos:
            obj = mapper.find_by_hash(hashcode)
            with SpoValidityMapper() as mapper:
                for i in spos:
                    vals = mapper.find_validities_by_spo(i)
                    obj.set_start_semester(vals[0])
                    obj.set_end_semester(vals[1])
            with ModuleMapper() as mapper:
                modules = mapper.find_by_spo(hashcode)
                obj.set_modules(modules)
            result.append(obj)
        return result

    def get_all_by_studycourse(self, studycourse):
        """Alle Spos eines Studienganges auslesen"""
        with SpoMapper() as mapper:
            return mapper.find_all_by_studycourse(studycourse)

    def delete_spo(self, spo):
        """Die gegebene Spo aus unserem System löschen."""
        with SpoMapper() as mapper:
            mapper.delete(spo)

    """Modul-spezifische Methoden"""

    def create_module(self, proposal: Module, creator):
        """
        Legt das Objekt in der Datenbank an und setzt creationate und creator,
        wenn das Zielobjekt noch nicht in der DB existiert.

        :param proposal: Ein Modul Objekt
        :param creator: Ein User, creator des Objekts
        """
        proposal.set_creationdate(datetime.date.today())
        proposal.set_creator(hash(creator))
        with ModuleMapper() as mapper:
            return mapper.insert(proposal)

    def get_module_by_name(self, name: str):
        """Alle Module mit Namen name auslesen."""
        with ModuleMapper() as mapper:
            return mapper.find_by_name(name)

    def get_module_by_id(self, id: int):
        with ModuleMapper() as mapper:
            modhash = mapper.find_hash_by_id(id)
            return mapper.find_by_hash(modhash)

    def get_module_by_hash(self, modulehash):
        """Das Modul mit dem gegebenem Hash auslesen."""
        with ModuleMapper() as mapper:
            return mapper.find_by_hash(modulehash)

    def get_all_modules(self):
        """Alle module auslesen."""
        with ModuleMapper() as mapper:
            return mapper.find_all()

    def get_all_by_spo(self, spohash: int):
        """Gibt alle Module einer SPO aus"""
        with ModuleMapper() as mapper:
            return mapper.find_all_by_spo(spohash)

    def delete_module(self, module):
        with ModuleMapper() as mapper:
            mapper.delete(module)

    """Modulteil-spezifische Methoden"""

    def create_modulepart(self, proposal: Modulepart, creator):
        """
        Legt das Objekt in der Datenbank an und setzt creationate und creator,
        wenn das Zielobjekt noch nicht in der DB existiert.

        :param proposal: Ein Modulepart Objekt
        :param creator: Ein User, creator des Objekts
        """
        proposal.set_creationdate(datetime.date.today())
        proposal.set_creator(hash(creator))
        with ModulePartMapper() as mapper:
            return mapper.insert(proposal)

    def get_modulepart_by_name(self, name):
        """Alle Modulteile mit Namen name auslesen."""
        with ModulePartMapper() as mapper:
            return mapper.find_by_name(name)

    def get_modulepart_by_id(self, id: int):
        with ModulePartMapper() as mapper:
            mphash = mapper.find_hash_by_id(id)
            return mapper.find_by_hash(mphash)

    def get_modulepart_by_module(self, modulehash):
        result = []
        with ModulePartMapper() as mapper:
            mp = mapper.find_hash_by_module(modulehash)
            for hash in mp:
                obj = mapper.find_by_hash(hash)
                result.append(obj)
        return result

    def get_modulepart_by_hash(self, hashcode):
        """Das Modulteil mit dem gegebenem Hash auslesen."""
        with ModuleMapper() as mapper:
            return mapper.find_by_hash(hashcode)

    def get_all_moduleparts(self):
        """Alle Modulteile auslesen."""
        with ModulePartMapper() as mapper:
            return mapper.find_all()

    def delete_modulepart(self, modulepart):
        """Den gegebenen Modulteil aus unserem System löschen."""
        with ModulePartMapper() as mapper:
            mapper.delete(modulepart)

    """Semester-spezifische Methoden"""

    def create_semester(self, proposal: Semester, creator: int):
        """
        Legt das Objekt in der Datenbank an und setzt creationate und creator,
        wenn das Zielobjekt noch nicht in der DB existiert.

        :param proposal: Ein Semester Objekt
        :param creator: Ein User, creator des Objekts
        """
        proposal.set_creationdate(datetime.date.today())
        proposal.set_creator(hash(creator))
        with SemesterMapper() as mapper:
            return mapper.insert(proposal)

    def get_semester_by_name(self, name):
        """Alle Semester mit Namen 'name' auslesen."""
        with SemesterMapper() as mapper:
            return mapper.find_by_name(name)

    def get_semester_by_id(self, id):
        with SemesterMapper() as mapper:
            semhash = mapper.find_hash_by_id(id)
            return mapper.find_by_hash(semhash)

    def get_semester_by_hash(self, hashcode):
        """Das Semester mit dem gegebenem Hash auslesen."""
        with SemesterMapper() as mapper:
            return mapper.find_by_hash(hashcode)

    def get_all_semesters(self):
        """Alle Semester auslesen."""
        with SemesterMapper() as mapper:
            return mapper.find_all()

    def delete_semester(self, semester):
        """Das gegebene Semester aus unserem System löschen."""
        with SemesterMapper() as mapper:
            mapper.delete(semester)

    """Studycourse-spezifische Methoden"""

    def create_studycourse(self, proposal: StudyCourse, creator):
        """
        Legt das Objekt in der Datenbank an und setzt creationate und creator,
        wenn das Zielobjekt noch nicht in der DB existiert.

        :param proposal: Ein Studycourse Objekt
        :param creator: Ein User, creator des Objekts
        """
        proposal.set_creationdate(datetime.date.today())
        proposal.set_creator(hash(creator))
        with StudyCourseMapper() as mapper:
            return mapper.insert(proposal)

    def get_all_studycourses(self):

        with StudyCourseMapper() as mapper:
            return mapper.find_all()

    def get_studycourse_by_name(self, name):
        """Den Studiengang mit dem gegebenen Namen auslesen."""
        with StudyCourseMapper() as mapper:
            return mapper.find_by_name(name)


    def get_studycourse_by_id(self, id: int):
        with StudyCourseMapper() as mapper:
            schash = mapper.find_hash_by_id(id)
            return mapper.find_by_hash(schash)

    def get_studycourse_by_hash(self, hashcode: int):
        with StudyCourseMapper() as mapper:
            return mapper.find_by_hash(hashcode)

    def delete_studycourse(self, studycourse):

        with StudyCourseMapper() as mapper:
            mapper.delete(studycourse)

    """User-spezifische Methoden"""

    def create_user(self, proposal: User, creator):
        """
        Legt das Objekt in der Datenbank an und setzt creationate und creator,
        wenn das Zielobjekt noch nicht in der DB existiert.

        :param proposal: Ein User Objekt
        :param creator: Ein User, creator des Objekts
        """
        proposal.set_creationdate(datetime.date.today())
        proposal.set_creator(creator)
        with UserMapper() as mapper:
            return mapper.insert(proposal)

    def get_user_by_name(self, name):

        with UserMapper() as mapper:
            return mapper.find_by_name(name)

    def get_user_by_hash(self, userhash):
        """Einen User anhand seines Hashes ausgeben."""
        with UserMapper() as mapper:
            return mapper.find_by_hash(userhash)

    def get_user_by_google_user_id(self, gid):
        """Den Benutzer mit der gegebenen Google ID auslesen."""
        with UserMapper() as mapper:
            return mapper.find_by_google_user_id(gid)

    def get_all_users(self):
        with UserMapper() as mapper:
            return mapper.find_all()

    def save_user(self, user, creator: int):
        with UserMapper() as mapper:
            mapper.update(user)

    def delete_user(self, user):

        with UserMapper() as mapper:
            mapper.delete(user)

    """Person-spezifische Methoden"""

    def create_person(self, proposal: Person, creator):
        """
        Legt das Objekt in der Datenbank an und setzt creationate und creator,
        wenn das Zielobjekt noch nicht in der DB existiert.

        :param proposal: Ein Person Objekt
        :param creator: Ein User, creator des Objekts
        """
        proposal.set_creationdate(datetime.date.today())
        proposal.set_creator(hash(creator))
        with PersonMapper() as mapper:
            return mapper.insert(proposal)

    def get_person_by_name(self, name):
        """Alle Personen mit Namen name auslesen."""
        with PersonMapper() as mapper:
            return mapper.find_by_name(name)

    def get_person_by_id(self, id):
        with PersonMapper() as mapper:
            phash = mapper.find_hash_by_id(id)
            return mapper.find_by_hash(phash)

    def get_person_by_hash(self, number):
        """Die Person mit dem gegebenem Hash auslesen."""
        with PersonMapper() as mapper:
            return mapper.find_by_hash(number)

    def get_all_persons(self):
        """Alle Personen auslesen."""
        with PersonMapper() as mapper:
            return mapper.find_all()

    def save_person(self, person):
        """Die gegebene Person speichern."""
        with PersonMapper() as mapper:
            mapper.update(person)

    def delete_person(self, person):
        """Die gegebene Person aus unserem System löschen."""
        with PersonMapper() as mapper:
            mapper.delete(person)


