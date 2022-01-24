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
from server.db.StudyCourseMapper import StudyCourseMapper
from server.db.UserMapper import UserMapper


class Administration (object):
    def __init__(self):
        pass
   
    """Modul-spezifische Methoden"""

    def create_module(self, proposal):
        with ModuleMapper() as mapper:
            return mapper.insert(proposal)

    def get_module_by_name(self, name):
        """Alle Module mit Namen name auslesen."""
        with ModuleMapper() as mapper:
            return mapper.find_by_name(name)

    def get_module_by_id(self, number):
        """Das Modul mit der gegebenen ID auslesen."""
        with ModuleMapper() as mapper:
            return mapper.find_by_id(number)

    def get_module_by_hash(self, number):
        """Das Modul mit dem gegebenem Hash auslesen."""
        with ModuleMapper() as mapper:
            return mapper.find_by_hash(number)

    def get_all_modules(self):
        """Alle module auslesen."""
        with ModuleMapper() as mapper:
            return mapper.find_all()

    def save_module(self, module):
        """Den gegebenen Benutzer speichern."""
        with ModuleMapper as mapper:
            mapper.update(module)

    def delete_module(self, module):
        with ModuleMapper() as mapper:
            mapper.delete(module)

    """Modulteil-spezifische Methoden"""

    def create_modulepart(self, proposal):
        with ModulePartMapper() as mapper:
            return mapper.insert(proposal)

    def get_modulepart_by_name(self, name):
        """Alle Modulteile mit Namen name auslesen."""
        with ModulePartMapper() as mapper:
            return mapper.find_by_name(name)

    def get_modulepart_by_id(self, number):
        """Den Modulteil mit der gegebenen ID auslesen."""
        with ModulePartMapper() as mapper:
            return mapper.find_by_id(number)

    def get_all_moduleparts(self):
        """Alle Modulteile auslesen."""
        with ModulePartMapper() as mapper:
            return mapper.find_all()

    def save_moduleparts(self, modulepart):
        """Den gegebenen Modulteil speichern."""
        with ModulePartMapper() as mapper:
            mapper.update(modulepart)

    def delete_modulepart(self, modulepart):
        """Den gegebenen Modulteil aus unserem System löschen."""
        with ModulePartMapper() as mapper:
            mapper.delete(modulepart)

    """Person-spezifische Methoden"""

    def create_person(self, proposal):
        """Eine Person anlegen"""
        with PersonMapper() as mapper:
            return mapper.insert(proposal)

    def get_person_by_name(self, name):
        """Alle Personen mit Namen name auslesen."""
        with PersonMapper() as mapper:
            return mapper.find_by_name(name)

    def get_person_by_id(self, number):
        """Die Person mit der gegebenen ID auslesen."""
        with PersonMapper() as mapper:
            return mapper.find_by_key(number)

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

    """Semester-spezifische Methoden"""

    def create_semester(self, proposal):
        """Ein Semester anlegen"""
        with SemesterMapper() as mapper:
            return mapper.insert(proposal)

    def get_semester_by_name(self, name):
        """Alle Semester mit Namen 'name' auslesen."""
        with SemesterMapper() as mapper:
            return mapper.find_by_name(name)

    def get_semester_by_id(self, number):
        """Das Semester mit der gegebenen ID auslesen."""
        with SemesterMapper() as mapper:
            return mapper.find_by_key(number)

    def get_all_semesters(self):
        """Alle Semester auslesen."""
        with SemesterMapper() as mapper:
            return mapper.find_all()

    def save_semester(self, semester):
        """Das gegebene Semester speichern."""
        with SemesterMapper() as mapper:
            mapper.update(semester)

    def delete_semester(self, semester):
        """Das gegebene Semester aus unserem System löschen."""
        with SemesterMapper() as mapper:
            mapper.delete(semester)

    """SpoValidity-spezifische Methoden"""

    def get_spo_by_semester_hash(self, hashcode: int):
        with SpoValidityMapper() as mapper:
            mapper.find_spos_by_semester_hash(hashcode)

    def get_semester_by_spo_hash(self, hashcode: int):
        with SpoValidityMapper() as mapper:
            mapper.find_semesters_by_spo_hash(hashcode)

    def create_validity(self, proposal):
        with SpoValidityMapper() as mapper:
            mapper.insert(proposal)

    """Spo-spezifische Methoden"""

    def create_spo(self, proposal):
        """Eine SPO anlegen"""
        with SpoMapper() as mapper:
            newobj = mapper.insert(proposal)
        with SpoValidityMapper() as mapper:
             mapper.insert(newobj)
        return newobj

    def get_spo_by_name(self, name):
        """Alle SPOs mit Namen name auslesen."""
        with SpoMapper() as mapper:
            return mapper.find_by_name(name)

    def get_spo_by_id(self, number):
        """Die SPO mit der gegebenen ID auslesen."""
        with SpoMapper() as mapper:
            return mapper.find_by_key(number)

    def get_spo_by_hash(self, spo_hash):
        pass

    def get_latest_by_studycourse(self, studycourse):
        """Die aktuelle SPO eines Studienganges auslesen"""
        with SpoMapper() as mapper:
            return mapper.find_by_latest_creationdate(studycourse)

    def get_spo_by_startsem_studycourse(self, semesterhash: int, studycoursehash: int):
        """Die Spo mit den ausgewählten Startsemester und Studiengang auslesen."""
        with SpoMapper() as mapper:
            return mapper.find_by_startsemester_and_studycourse(semesterhash, studycoursehash)

    def get_all_spos(self):
        """Alle SPOs auslesen."""
        with SpoMapper() as mapper:
            return mapper.find_all()

    def get_all_by_studycourse(self, studycourse_id):
        """Alle Spos eines Studienganges auslesen"""
        with SpoMapper() as mapper:
            return mapper.find_all_by_studycourse(studycourse_id)

    def save_spo(self, spo):
        """Die gegebene Spo speichern."""
        with SpoMapper() as mapper:
            mapper.update(spo)

    def delete_spo(self, spo):
        """Die gegebene Spo aus unserem System löschen."""
        with SpoMapper() as mapper:
            mapper.delete(spo)

    """Studycourse-spezifische Methoden"""

    def create_studycourse(self, proposal):

        with StudyCourseMapper() as mapper:
            return mapper.insert(proposal)

    def get_studycourse_by_name(self, name):

        with StudyCourseMapper() as mapper:
            return mapper.find_by_name(name)

    def get_studycourse_by_id(self, number):

        with StudyCourseMapper() as mapper:
            return mapper.find_by_id(number)

    def get_all_studycourses(self):

        with StudyCourseMapper() as mapper:
            return mapper.find_all()

    def save_studycourse(self, studycourse):

        with StudyCourseMapper() as mapper:
            mapper.update(studycourse)

    def delete_studycourse(self, studycourse):

        with StudyCourseMapper() as mapper:
            mapper.delete(studycourse)

    """User-spezifische Methoden"""

    def create_user(self, user):
        with UserMapper() as mapper:
            return mapper.insert(user)

    def get_user_by_name(self, name):

        with UserMapper() as mapper:
            return mapper.find_by_name(name)

    def get_user_by_id(self, number):

        with UserMapper() as mapper:
            return mapper.find_by_key(number)

    def get_user_by_hash(self, userhash):
        """Einen User anhand seines Hashes ausgeben."""
        with UserMapper() as mapper:
            return mapper.find_by_hash(userhash)

    def get_all_users(self):

        with UserMapper() as mapper:
            return mapper.find_all()

    def save_user(self, user):

        with UserMapper() as mapper:
            mapper.update(user)

    def delete_user(self, user):

        with UserMapper() as mapper:
            mapper.delete(user)

    def get_user_by_google_user_id(self, gid):
        """Den Benutzer mit der gegebenen Google ID auslesen."""
        with UserMapper() as mapper:
            return mapper.find_by_google_user_id(gid)

