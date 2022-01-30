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

    @staticmethod
    def create_spo(proposal: Spo, creator):
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

    @staticmethod
    def get_spo_by_hash(hashcode):
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

    @staticmethod
    def get_spo_by_id(id: int):
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

    @staticmethod
    def get_latest_by_studycourse(studycourse):
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

    @staticmethod
    def get_spo_by_startsem_studycourse(semesterhash: int, studycoursehash: int):
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

    @staticmethod
    def get_all_spos():
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

    @staticmethod
    def get_all_by_studycourse(studycourseid: int):
        """Alle Spos eines Studienganges auslesen"""
        with StudyCourseMapper() as mapper:
            schash = mapper.find_hash_by_id(studycourseid)
        result = []
        with SpoMapper() as spomapper:
            spos = spomapper.find_all_by_studycourse(schash)
            for spo in spos:
                hashcode = hash(spo)
                with SpoValidityMapper() as valmapper:
                    vals = valmapper.find_validities_by_spo(hashcode)                            
                    if (vals[0] is not None):
                        spo.set_start_semester(vals[0])    
                    if (vals[1] is not None):
                        spo.set_end_semester(vals[1])
                with ModuleMapper() as modmapper:
                    modules = modmapper.find_by_spo(hashcode)
                    spo.set_modules(modules)
                result.append(spo)
        return result

    @staticmethod
    def delete_spo(spo):
        """Die gegebene Spo aus unserem System löschen."""
        with SpoMapper() as mapper:
            mapper.delete(spo)

    """Modul-spezifische Methoden"""

    @staticmethod
    def create_module(proposal: Module, creator):
        """
        Legt das Objekt in der Datenbank an und setzt creationate und creator,
        wenn das Zielobjekt noch nicht in der DB existiert.

        :param proposal: Ein Modul Objekt
        :param creator: Ein User, creator des Objekts
        """
        proposal.set_creationdate(datetime.date.today())
        proposal.set_creator(hash(creator))
        with ModuleMapper() as mapper:
            existing = mapper.find_by_hash(hash(proposal))
            if existing is None:
                newobj = mapper.insert(proposal)
                return newobj
    @staticmethod
    def get_module_by_name(name: str):
        """Alle Module mit Namen name auslesen."""
        with ModuleMapper() as mapper:
            return mapper.find_by_name(name)

    @staticmethod
    def get_module_by_id(id: int):
        with ModuleMapper() as mapper:
            modhash = mapper.find_hash_by_id(id)
            return mapper.find_by_hash(modhash)

    @staticmethod
    def get_module_by_hash(modulehash):
        """Das Modul mit dem gegebenem Hash auslesen."""
        with ModuleMapper() as mapper:
            return mapper.find_by_hash(modulehash)

    @staticmethod
    def get_all_modules():
        """Alle module auslesen."""
        with ModuleMapper() as mapper:
            return mapper.find_all()

    @staticmethod
    def get_all_by_spo(spohash: int):
        """Gibt alle Module einer SPO aus"""
        with ModuleMapper() as mapper:
            return mapper.find_all_by_spo(spohash)

    @staticmethod
    def delete_module(module):
        with ModuleMapper() as mapper:
            mapper.delete(module)

    """Modulteil-spezifische Methoden"""

    @staticmethod
    def create_modulepart(proposal: Modulepart, creator):
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

    @staticmethod
    def get_modulepart_by_name(name):
        """Alle Modulteile mit Namen name auslesen."""
        with ModulePartMapper() as mapper:
            return mapper.find_by_name(name)

    @staticmethod
    def get_modulepart_by_id(id: int):
        with ModulePartMapper() as mapper:
            mphash = mapper.find_hash_by_id(id)
            return mapper.find_by_hash(mphash)

    @staticmethod
    def get_modulepart_by_module(modulehash):
        result = []
        with ModulePartMapper() as mapper:
            mparts = mapper.find_hash_by_module(modulehash)
            for mparthash in mparts:
                obj = mapper.find_by_hash(mparthash)
                result.append(obj)
        return result

    @staticmethod
    def get_modulepart_by_hash(hashcode):
        """Das Modulteil mit dem gegebenem Hash auslesen."""
        with ModuleMapper() as mapper:
            return mapper.find_by_hash(hashcode)

    @staticmethod
    def get_all_moduleparts():
        """Alle Modulteile auslesen."""
        with ModulePartMapper() as mapper:
            return mapper.find_all()

    @staticmethod
    def delete_modulepart(modulepart):
        """Den gegebenen Modulteil aus unserem System löschen."""
        with ModulePartMapper() as mapper:
            mapper.delete(modulepart)

    """Semester-spezifische Methoden"""

    @staticmethod
    def create_semester(proposal: Semester, creator):
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

    @staticmethod
    def get_semester_by_name(name):
        """Alle Semester mit Namen 'name' auslesen."""
        with SemesterMapper() as mapper:
            return mapper.find_by_name(name)

    @staticmethod
    def get_semester_by_id(id):
        with SemesterMapper() as mapper:
            semhash = mapper.find_hash_by_id(id)
            return mapper.find_by_hash(semhash)

    @staticmethod
    def get_semester_by_hash(hashcode):
        """Das Semester mit dem gegebenem Hash auslesen."""
        with SemesterMapper() as mapper:
            return mapper.find_by_hash(hashcode)

    @staticmethod
    def get_all_semesters():
        """Alle Semester auslesen."""
        with SemesterMapper() as mapper:
            return mapper.find_all()

    @staticmethod
    def delete_semester(semester):
        """Das gegebene Semester aus unserem System löschen."""
        with SemesterMapper() as mapper:
            mapper.delete(semester)

    """Studycourse-spezifische Methoden"""

    @staticmethod
    def create_studycourse(proposal: StudyCourse, creator):
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

    @staticmethod
    def get_all_studycourses():
        result = []
        with StudyCourseMapper() as mapper:
            sclist = mapper.find_all()
            for sc in sclist:
                result.append(mapper.find_by_hash(sc))
        return result

    @staticmethod
    def get_studycourse_by_name(name):
        """Den Studiengang mit dem gegebenen Namen auslesen."""
        with StudyCourseMapper() as mapper:
            return mapper.find_by_name(name)

    @staticmethod
    def get_studycourse_by_id(id: int):
        with StudyCourseMapper() as mapper:
            schash = mapper.find_hash_by_id(id)
            return mapper.find_by_hash(schash)

    @staticmethod
    def get_studycourse_by_hash(hashcode: int):
        with StudyCourseMapper() as mapper:
            return mapper.find_by_hash(hashcode)

    @staticmethod
    def delete_studycourse(studycourse):

        with StudyCourseMapper() as mapper:
            mapper.delete(studycourse)

    """User-spezifische Methoden"""
    @staticmethod
    def create_user(proposal: User):
        """
        Legt das Objekt in der Datenbank an und setzt creationate und creator,
        wenn das Zielobjekt noch nicht in der DB existiert.

        :param proposal: Ein User Objekt
        """
        proposal.set_creationdate(datetime.date.today())
        with UserMapper() as mapper:
            us = mapper.find_by_hash(hash(proposal))
            if us is None:
                return mapper.insert(proposal)

    @staticmethod
    def get_user_by_name(name):

        with UserMapper() as mapper:
            return mapper.find_by_name(name)

    @staticmethod
    def get_user_by_hash(userhash):
        """Einen User anhand seines Hashes ausgeben."""
        with UserMapper() as mapper:
            return mapper.find_by_hash(userhash)

    @staticmethod
    def get_user_by_google_user_id(gid):
        """Den Benutzer mit der gegebenen Google ID auslesen."""
        with UserMapper() as mapper:
            return mapper.find_by_google_user_id(gid)

    @staticmethod
    def get_all_users():
        with UserMapper() as mapper:
            return mapper.find_all()

    @staticmethod
    def save_user(user):
        with UserMapper() as mapper:
            us = mapper.find_by_google_user_id(user.get_google_user_id())
        if us is None:
            mapper.insert(user)
        else:
            mapper.update(user)

    @staticmethod
    def delete_user(user):

        with UserMapper() as mapper:
            mapper.delete(user)

    """Person-spezifische Methoden"""

    @staticmethod
    def create_person(proposal: Person, creator):
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

    @staticmethod
    def get_person_by_name(name):
        """Alle Personen mit Namen name auslesen."""
        with PersonMapper() as mapper:
            return mapper.find_by_name(name)

    @staticmethod
    def get_person_by_id(id):
        with PersonMapper() as mapper:
            phash = mapper.find_hash_by_id(id)
            return mapper.find_by_hash(phash)

    @staticmethod
    def get_person_by_hash(number):
        """Die Person mit dem gegebenem Hash auslesen."""
        with PersonMapper() as mapper:
            return mapper.find_by_hash(number)

    @staticmethod
    def get_all_persons():
        """Alle Personen auslesen."""
        with PersonMapper() as mapper:
            return mapper.find_all()

    @staticmethod
    def save_person(person):
        """Die gegebene Person speichern."""
        with PersonMapper() as mapper:
            mapper.update(person)

    @staticmethod
    def delete_person(person):
        """Die gegebene Person aus unserem System löschen."""
        with PersonMapper() as mapper:
            mapper.delete(person)

