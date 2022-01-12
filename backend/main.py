# -- coding:utf-8 --
from flask import Flask
from flask_restx import Api, Resource, fields
from flask_cors import CORS

# Wir greifen natürlich auf unsere Applikationslogik inkl. BusinessObject-Klassen zurück
from server.SecurityDecorator import secured
from server.Administration import Administration
from server.bo.Spo import Spo
from server.bo.User import User
from server.bo.Module import Module
from server.bo.Modulepart import Modulepart
from server.bo.StudyCourse import StudyCourse
from server.bo.Person import Person

"""
from server.bo.Module import Module
from server.bo.Modulepart import Modulepart
from server.bo.StudyCourse import StudyCourse
from server.bo.Person import Person
"""

# Außerdem nutzen wir einen selbstgeschriebenen Decorator der die Authentifikation übernimmt

app = Flask(__name__)
CORS(app, resources=r'/sopra/*')

api = Api(app, version='1.0', title='Sopra API',
          description='Datenverarbeitungssystem für SpOs.')

"""Anlegen von Namespaces 
Namespaces erlauben uns die Strukturierung von APIs.
"""
sposystem = api.namespace('sopra', description='Funktionen des SpoSystems')

"""Nachfolgend werden analog zu unseren BusinessObject-Klassen transferierbare Strukturen angelegt.
BusinessObject dient als Basisklasse, auf der die weiteren Strukturen "" aufsetzen."""

bo = api.model('BusinessObject', {
    'id': fields.Integer(attribute='_id', description='Einzigartige Identität eines Objects')
})

"""Alle anderen BusinessObjects"""
user = api.inherit('User', bo, {
    'firstname': fields.String(attribute='__firstname', description='Vorname eines Users'),
    'lastname': fields.String(attribute='__lastname', description='Nachname eines Users'),
    'email': fields.String(attribute='__email', description='Email adresse eines Users'),
    'google_user_id': fields.String(attribute='__google_user_id', description='Google ID des Users'),
    'isadmin': fields.Integer(attribute='__isadmin', description='Anzeige ob Adminstatus oder nicht')
})

namedbo = api.inherit('Namedbo', bo, {
    'name': fields.String(attribute='_name', description='Name eines NamedBOs'),
    'title': fields.String(attribute='_name', description='Titel eines NamedBOs')
})

spo = api.inherit('Spo', namedbo, {
    'start_semester': fields.Integer(attribute='_start_semester', description='Anfangssemester der SPO-gültigkeit'),
    'end_semester': fields.Integer(attribute='_end_semester', description='Endsemester der SPO-gültigkeit'),
    'modules': fields.List(attribute='_modules',
                           cls_or_instance=fields.Integer, description='Liste der Module der SPO'),
    'studycourse': fields.Integer(attribute='_studycourse_id', description='Studycourse der SPO')

})

spoelement = api.inherit('Spoelement', namedbo, {
    'edvnr': fields.Integer(attribute='_edvnr', description='EDV nr des Spoelements'),
    'ects': fields.Integer(attribute='_ects', description='Die Anzahl der ECTS des Moduls'),
    'workload': fields.String(attribute='_workload',
                              description='Arbeitszeit für das Spoelement und ihre Zusammensetzung')
})

module = api.inherit('Module', spoelement, {
    'type': fields.String(attribute='_type', description='Typ des Moduls'),
    'requirement': fields.String(attribute='_requirement', description='Voraussetzungen für das Modul'),
    'outcome': fields.String(attribute='_outcome', description='Outcome des Moduls'),
    'examtype': fields.String(attribute='_examtype', description='Prüfungstyp des Moduls'),
    'instructor': fields.Integer(attribute='_instructor', description='Modulverantwortlicher'),
    'moduleparts': fields.List(attribute='__moduleparts', cls_or_instance=fields.Integer,
                               description='Modulteile des Moduls')
})

modulepart = api.inherit('Modulepart', spoelement, {
    'sws': fields.String(attribute='_sws', description='Anzahl der SWS des Modulteils'),
    'language': fields.String(attribute='_language', descpription='Sprache des Modulteils'),
    'description': fields.String(attribute='_description', description='Beschreibung des Modulteils'),
    'connection': fields.String(attribute='_connection', description='Verbindung zu anderen Modulteilen'),
    'literature': fields.String(attribute='_literature', description='Literatur für das Modulteil'),
    'sources': fields.String(attribute='_sources', description='Quellen'),
    'semester': fields.Integer(attribute='_semester', description='Semester des Modulteils'),
    'professor': fields.Integer(attribute='_professor', description='Prof des Modulteils')
})

studycourse = api.inherit('StudyCourse', namedbo)

person = api.inherit('Person', namedbo, {
    'firstname': fields.String(attribute='__firstname', description='Vorname einer Person'),
    'lastname': fields.String(attribute='__lastname', description='Nachname einer Person'),
    'email': fields.String(attribute='__email', description='Email adresse einer Person')
})

"""Alles @sposystem.route('')"""


@sposystem.route('/users')
@sposystem.response(500, 'falls es zu einem Server-seitigen Fehler kommt.')
class UserListOperations(Resource):
    @sposystem.marshal_list_with(user)
    @secured
    def get(self):
        """
        Auslesen aller User Objekte.
        Sollte kein User Objekt verfügbar sein, wird eine leere Sequenz zurückgegeben
        """
        adm = Administration()
        users = adm.get_all_users()
        return users

    @sposystem.marshal_with(user, code=200)
    @sposystem.expect(user)
    # @secured
    def post(self):

        adm = Administration()
        proposal = User.from_dict(api.payload)

        if proposal is not None:
            c = adm.create_user(proposal.get_firstname(), proposal.get_lastname(), proposal.get_email(), proposal.get_google_user_id())
            return c, 200
        else:
            return '', 500


@sposystem.route('/users/<int:id>')
@sposystem.response(500, 'Falls es zu einem Server-seitigen Fehler kommt.')
@sposystem.param('id', 'Die ID des User-Objekts')
class UserOperations(Resource):
    @sposystem.marshal_with(user)
    @secured
    def get(self, id):
        """Auslesen eines bestimmten Customer-Objekts.
        Das auszulesende Objekt wird durch die ```id``` in dem URI bestimmt."""

        adm = Administration()
        us = adm.get_user_by_id(id)
        return us

    @sposystem.marshal_with(user)
    @sposystem.expect(user, validate=True)
    @secured
    def put(self, id):
        """Update eines bestimmten User-Objekts.
        **ACHTUNG: ** relevante id ist die id, die mittels URI bereitgestellt und somit als Methodenparameter
        verwendet wird. Dieser Parameter überschreibt das ID-Attribut des im Payload der Anfrage übermittelten
        User-Objekts."""

        adm = Administration()
        us = User.from_dict(api.payload)

        if us is not None:
            """Hierdurch wird die id des zu überschreibenden (vgl. Update) Customer-Objekts gesetzt.
            Siehe Hinweise oben."""

            us.set_id(id)
            adm.save_user(us)
            return '', 200
        else:
            return '', 500

    @secured
    def delete(self, id):
        """Löschen eines bestimmten User-Objekts.
        Das zu löschende Objekt wird durch die ```id``` in dem URI bestimmt."""

        adm = Administration()
        us = adm.get_user_by_id(id)
        adm.delete_user(us)
        return '', 200


@sposystem.route('/users-by-name/<string:lastname>')
@sposystem.response(500, 'Falls es zu einem Server-seitigen Fehler kommt.')
@sposystem.param('lastname', 'Der Nachname des Users')
class UserByNameOperations(Resource):
    @sposystem.marshal_with(user)
    @secured
    def get(self, lastname):
        """
        Auslesen von Customer-Objekten, die durch den Nachnamen bestimmt werden.
        Die auszulesenden Objekte werden durch ```lastname``` in dem URI bestimmt.
        """

        adm = Administration()
        us = adm.get_user_by_name(lastname)
        return us


@sposystem.route('/spos')
@sposystem.response(500, 'falls es zu einem Server-seitigen Fehler kommt.')
class SpoListOperations(Resource):
    @sposystem.marshal_list_with(spo)
    @secured
    def get(self):
        """
        Auslesen aller SPO-Objekte.
        Sollten keine SPO-Objekte verfügbar sein, so wird eine leere Sequenz zurückgegeben.
        """
        adm = Administration()
        spo_list = adm.get_all_spos()
        return spo_list

    @sposystem.marshal_with(spo, code=200)
    @sposystem.expect(spo, validate=True)
    @secured
    def post(self):
        adm = Administration()
        proposal = Spo.from_dict(api.payload)

        if proposal is not None:
            newspo = adm.create_spo(proposal.get_name(),
                                    proposal.get_title(),
                                    proposal.get_start_semester(),
                                    proposal.get_end_semester(),
                                    proposal.get_studycourse())
            return newspo, 200
        else:
            return '', 500


@sposystem.route('/spos/<int:id>')
@sposystem.response(500, 'falls es zu einem Server-seitigen Fehler kommt.')
@sposystem.param('id', 'Die ID des SPO-Objekts')
class SpoOperations(Resource):

    @sposystem.marshal_with(spo)
    @secured
    def get_by_id(self, id):
        """
        Auslesen eines bestimmten SPO-Objekts.
        Das auszulesende Objekt wird durch die ```id``` in dem URI bestimmt.
        """

        adm = Administration()
        spo = adm.get_spo_by_id(id)
        return spo

    @sposystem.marshal_with(spo)
    @sposystem.expect(spo, validate=True)
    @secured
    def put(self, id):
        """
        Update eines bestimmten SPO-Objekts.
        **ACHTUNG: ** relevante id ist die id, die mittels URI bereitgestellt und somit als Methodenparameter
        verwendet wird. Dieser Parameter überschreibt das ID-Attribut des im Payload der Anfrage übermittelten
        SPO-Objekts.
        """

        adm = Administration()
        spo = Spo.from_dict(api.payload)

        if spo is not None:
            """
            Hierdurch wird die id des zu überschreibenden (vgl. Update) SPO-Objekts gesetzt.
            Siehe Hinweise oben.
            """
            spo.set_id(id)
            adm.save_spo(spo)
            return '', 200
        else:
            return '', 500

    @secured
    def delete(self, id):
        """
        Löschen eines bestimmten SPO-Objekts.
        Das zu löschende Objekt wird durch die ```id``` in dem URI bestimmt.
        """

        adm = Administration()
        spo = adm.get_spo_by_id(id)
        adm.delete_spo(spo)
        return '', 200

    @sposystem.marshal_list_with(spo)
    @secured
    def get_modules_by_spo(self, id):

        adm = Administration()
        s = adm.get_spo_by_id(id)
        molist = adm.get_all_modules(s)
        return molist


"""
@sposystem.route('/spos/<semester: startsemester>')
@sposystem.response(500, 'falls es zu einem Server-seitigen Fehler kommt.')
@sposystem.param('start_semester', 'Das Startsemester des SPO-Objekts')
class SpoStartSemesterOperations:

    @sposystem.marshal_with(spo)
    @secured
    def get_by_start_semester(self, semester):
"""


@sposystem.route('/modules')
@sposystem.response(500, 'falls es zu einem Server-seitigen Fehler kommt.')
class ModuleListOperations(Resource):
    @sposystem.marshal_list_with(module, code=200)
    @secured
    def get(self):

        adm = Administration()
        modules = adm.get_all_modules()
        return modules

    @sposystem.marshal_with(module)
    @secured
    def post(self):

        adm = Administration()
        proposal = Module.from_dict(api.payload)
        if proposal is not None:
            mo = adm.create_module(proposal.get_name(),
                                   proposal.get_title(),
                                   proposal.get_requirement(),
                                   proposal.get_examtype(),
                                   proposal.get_instructor(),
                                   proposal.get_outcome(),
                                   proposal.get_type(),
                                   proposal.get_modulepart_id(),
                                   proposal.get_ects(),
                                   proposal.get_edvnr(),
                                   proposal.get_workload()
                                   )
            return mo, 200
        else:
            return '', 500


@sposystem.route('/modules/<int:id>')
@sposystem.response(500, 'falls es zu einem Server-seitigen Fehler kommt.')
@sposystem.param("id", "Die id des Modules")
class ModuleOperations(Resource):
    @sposystem.marshal_with(module)
    @secured
    def get(self, id):
        """Auslesen eines bestimmten Modul-Objekts"""
        adm = Administration()
        mo = adm.get_module_by_id(id)
        return mo

    @sposystem.marshal_with(module)
    @sposystem.expect(module, validate=True)
    @secured
    def put(self, id):
        """Update eines bestimmten Module-Objekts.
        **ACHTUNG: ** relevante id ist die id, die mittels URI bereitgestellt und somit als Methodenparameter
        verwendet wird. Dieser Parameter überschreibt das ID-Attribut des im Payload der Anfrage übermittelten
        User-Objekts."""

        adm = Administration()
        mo = Module.from_dict(api.payload)

        if mo is not None:
            """Hierdurch wird die id des zu überschreibenden (vgl. Update) Customer-Objekts gesetzt.
            Siehe Hinweise oben."""

            mo.set_id(id)
            adm.save_module(mo)
            return '', 200
        else:
            return '', 500

    @secured
    def delete(self, id):
        """Löschen eines bestimmten Module-Objekts.
        Das zu löschende Objekt wird durch die ```id``` in dem URI bestimmt."""

        adm = Administration()
        mo = adm.get_module_by_id(id)
        adm.delete_module(mo)
        return '', 200


@sposystem.route('/module/<int:module_id>')
@sposystem.response(500, 'falls es zu einem Server-seitigen Fehler kommt.')
@sposystem.param('id', 'Die id des Moduls')
class ModulePartsOperations(Resource):
    @sposystem.marshal_list_with(module)
    @secured
    def get(self, id):
        adm = Administration()
        moparts = adm.get_module_by_id(id)
        moparts.get_moduleparts()

        return moparts


@sposystem.route('/moduleparts')
@sposystem.response(500, 'falls es zu einem Server-seitigen Fehler kommt.')
class ModulePartListOperations(Resource):
    @sposystem.marshal_list_with(modulepart, code=200)
    @secured
    def get(self):

        adm = Administration()
        moduleparts = adm.get_all_moduleparts()
        return moduleparts

    @sposystem.marshal_with(modulepart)
    @sposystem.expect(modulepart)
    # @secured
    def post(self):

        adm = Administration()
        proposal = Modulepart.from_dict(api.payload)
        if proposal is not None:
            mopart = adm.create_modulepart(proposal.get_name(),
                                           proposal.get_title(),
                                           proposal.get_language(),
                                           proposal.get_literature(),
                                           proposal.get_semester(),
                                           proposal.get_sources(),
                                           proposal.get_connection(),
                                           proposal.get_description(),
                                           proposal.get_sws(),
                                           proposal.get_professor(),
                                           proposal.get_ects(),
                                           proposal.get_edvnr(),
                                           proposal.get_workload()
                                           )
            return mopart, 200
        else:
            return '', 500


@sposystem.route('/moduleparts/<int:id>')
@sposystem.response(500, 'falls es zu einem Server-seitigen Fehler kommt.')
@sposystem.param("id", "Die id des Moduleparts")
class ModulePartOperations(Resource):
    @sposystem.marshal_with(modulepart)
    @secured
    def get(self, id):
        """Auslesen eines bestimmten Modulepart-Objekts"""
        adm = Administration()
        mopart = adm.get_modulepart_by_id(id)
        return mopart

    @sposystem.marshal_with(modulepart)
    @sposystem.expect(modulepart, validate=True)
    @secured
    def put(self, id):
        """Update eines bestimmten Modulepart-Objekts.
        **ACHTUNG: ** relevante id ist die id, die mittels URI bereitgestellt und somit als Methodenparameter
        verwendet wird. Dieser Parameter überschreibt das ID-Attribut des im Payload der Anfrage übermittelten
        User-Objekts."""

        adm = Administration()
        mopart = Modulepart.from_dict(api.payload)

        if mopart is not None:
            """Hierdurch wird die id des zu überschreibenden (vgl. Update) Customer-Objekts gesetzt.
            Siehe Hinweise oben."""

            mopart.set_id(id)
            adm.save_modulepart(mopart)
            return '', 200
        else:
            return '', 500

    @secured
    def delete(self, id):
        """Löschen eines bestimmten Modulepart-Objekts.
        Das zu löschende Objekt wird durch die ```id``` in dem URI bestimmt."""

        adm = Administration()
        mopart = adm.get_modulepart_by_id(id)
        adm.delete_modulepart(mopart)
        return '', 200


@sposystem.route('/studycourses')
@sposystem.response(500, 'falls es zu einem Server-seitigen Fehler kommt.')
class StudycourseListOperations(Resource):
    @sposystem.marshal_list_with(studycourse)
    @secured
    def get(self):
        """
        Auslesen aller SPO-Objekte.
        Sollten keine SPO-Objekte verfügbar sein, so wird eine leere Sequenz zurückgegeben.
        """

        adm = Administration()
        studycourse_list = adm.get_all_studycourses()
        return studycourse_list

    @sposystem.marshal_list_with(studycourse, code=200)
    @sposystem.expect(studycourse)
    # @secured
    def post(self):
        adm = Administration()
        proposal = StudyCourse.from_dict(api.payload)

        if proposal is not None:
            sc = adm.create_studycourse(proposal.get_name(), proposal.get_title())
            return sc, 200
        else:
            return'', 500


@sposystem.route('/studycourse/<int:id>')
@sposystem.response(500, 'Falls es zu einem Server-seitigen Fehler kommt.')
@sposystem.param('id', 'Die ID des Studycourse-Objekts')
class StudycourseOperations(Resource):
    @sposystem.marshal_with(studycourse)
    @secured
    def get(self, id):
        """Auslesen eines bestimmten Studycourse-Objekts.
        Das auszulesende Objekt wird durch die```id```in dem URI bestimmt."""

        adm = Administration()
        sc = adm.get_studycourse_by_id(id)
        return sc

    @secured
    def delete(self, id):
        """Löschen eines bestimmten Studycourse-Objekts.
        Das zu löschende Objekt wird durch die```id```in dem URI bestimmt."""

        adm = Administration()
        sc = adm.get_studycourse_by_id(id)
        adm.delete_studycourse(sc)
        return'', 200

    @sposystem.marshal_with(studycourse)
    @sposystem.expect(studycourse, validate=True)
    @secured
    def put(self, id):
        """Update eines bestimmten Studycourse-Objekts.
        **ACHTUNG: ** relevante id ist die id, die mittels URI bereitgestellt und somit als Methodenparameter
        verwendet wird. Dieser Parameter überschreibt das ID-Attribut des im Payload der Anfrage übermittelten
        User-Objekts."""

        adm = Administration()
        sc = StudyCourse.from_dict(api.payload)

        if sc is not None:
            """Hier durch wird die id des zu überschreibenden (vgl.Update)Studycourse-Objekts gesetzt.
            Siehe Hinweise oben."""

            sc.set_id(id)
            adm.save_studycourse(sc)
            return'', 200
        else:
            return'', 500


@sposystem.route('/persons')
@sposystem.response(500, 'falls es zu einem Server-seitigen Fehler kommt.')
class PersonListOperations(Resource):
    @sposystem.marshal_list_with(person)
    @secured
    def get(self):
        """
        Auslesen aller Person-Objekte.
        Sollten keine Person-Objekte verfügbar sein, so wird eine leere Sequenz zurückgegeben.
        """

        adm = Administration()
        person_list = adm.get_all_persons()

        return person_list

    @sposystem.marshal_list_with(person, code=200)
    @sposystem.expect(person)
    # @secured
    def post(self):
        adm = Administration()
        proposal = Person.from_dict(api.payload)

        if proposal is not None:
            pe = adm.create_person(proposal.get_firstname(),
                                   proposal.get_lastname(), proposal.get_email())
            return pe, 200
        else:
            return'', 500


@sposystem.route('/persons/<int:id>')
@sposystem.response(500, 'Falls es zu einem Server-seitigen Fehler kommt.')
@sposystem.param('id', 'Die ID des Person-Objekts')
class PersonOperations(Resource):
    @sposystem.marshal_with(person)
    @secured
    def get(self, id):
        """Auslesen eines bestimmten Person-Objekts.
        Das auszulesende Objekt wird durch die```id```in dem URI bestimmt."""

        adm = Administration()
        pe = adm.get_person_by_id(id)
        return pe

    @secured
    def delete(self, id):
        """Löschen eines bestimmten Person-Objekts.
        Das zu löschende Objekt wird durch die```id```in dem URI bestimmt."""

        adm = Administration()
        pe = adm.get_person_by_id(id)
        adm.delete_person(pe)
        return'', 200

    @sposystem.marshal_with(person)
    @sposystem.expect(person, validate=True)
    @secured
    def put(self, id):
        """Update eines bestimmten Studycourse-Objekts.
        **ACHTUNG: ** relevante id ist die id, die mittels URI bereitgestellt und somit als Methodenparameter
        verwendet wird. Dieser Parameter überschreibt das ID-Attribut des im Payload der Anfrage übermittelten
        User-Objekts."""

        adm = Administration()
        pe = Person.from_dict(api.payload)

        if pe is not None:
            """Hierdurch wird die id des zu überschreibenden (vgl.Update)Studycourse-Objekts gesetzt.
            Siehe Hinweise oben."""

            pe.set_id(id)
            adm.save_person(pe)
            return'', 200
        else:
            return'', 500


"""**ACHTUNG:** Diese Zeile wird nur in der lokalen Entwicklungsumgebung ausgeführt und hat in der Cloud keine Wirkung!
"""
if __name__ == '__main__':
    app.run(debug=True)
