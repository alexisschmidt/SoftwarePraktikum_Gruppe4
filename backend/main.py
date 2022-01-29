# -- coding:utf-8 --

# Unser Service basiert auf Flask 2.0.2
from flask import Flask
# Wir benutzen noch CORS 0.5.1, eine Flask-Erweiterung für Cross-Origin Resource Sharing
from flask_cors import CORS
# Auf Flask aufbauend nutzen wir RestX 3.0.10
from flask_restx import Api, Resource, fields

# Wir greifen natürlich auch auf unsere Applikationslogik inkl. BusinessObject-Klassen zurück
from server.Administration import Administration
# Wir nutzen einen selbstgeschriebenen Decorator der die Authentifikation übernimmt
from server.SecurityDecorator import secured
from server.bo.Module import Module
from server.bo.Modulepart import Modulepart
from server.bo.Person import Person
from server.bo.Semester import Semester
from server.bo.Spo import Spo
from server.bo.StudyCourse import StudyCourse
from server.bo.User import User

"""
Instanziieren von Flask. Am Ende dieser Datei erfolgt dann erst der 'Start' von Flask.
"""
app = Flask(__name__, static_folder='./build', static_url_path='/')


@app.route('/')
def index():
    return app.send_static_file('index.html')
"""
Alle Ressourcen mit dem Präfix /sposystem für **Cross-Origin Resource Sharing** (CORS) freigeben.
Diese eine Zeile setzt die Installation des Package flask-cors voraus. 

Sofern Frontend und Backend auf getrennte Domains/Rechnern deployed würden, wäre sogar eine Formulierung
wie etwa diese erforderlich:
CORS(app, resources={r"/sposytem/*": {"origins": "*"}})
Allerdings würde dies dann eine Missbrauch Tür und Tor öffnen, so dass es ratsamer wäre, nicht alle
"origins" zuzulassen, sondern diese explizit zu nennen. Weitere Infos siehe Doku zum Package flask-cors.
"""
CORS(app, resources=r'/sopra/*')

"""
In dem folgenden Abschnitt bauen wir ein Modell auf, das die Datenstruktur beschreibt, 
auf deren Basis Clients und Server Daten austauschen. Grundlage hierfür ist das Package flask-restx.
"""
api = Api(app, version='1.0', title='Sopra API',
          description='Datenverarbeitungssystem für SPOs.')

"""
Anlegen eines Namespace

Namespaces erlauben die Strukturierung von APIs. Dieser Namespace beinhaltet alle
SPO-relevanten Operationen unter dem Präfix /sposystem. 
Eine alternative bzw. ergänzende Nutzung von Namespace könnte etwa sein, unter-
schiedliche API-Versionen voneinander zu trennen, um etwa Abwärtskompatibilität 
(vgl. Lehrveranstaltungen zu Software Engineering) zu gewährleisten. 
Dies ließe sich z.B. umsetzen durch /sposystem/v1, /sposystem/v2 usw.
"""
sposystem = api.namespace('sopra', description='Funktionen des SpoSystems')

"""
Nachfolgend werden analog zu unseren BusinessObject-Klassen transferierbare Strukturen angelegt.
BusinessObject und NamedBo dienen als Basisklassen, auf der die weiteren Strukturen basieren.
"""
bo = api.model('BusinessObject', {
    'id': fields.Integer(attribute='_id', description='Einzigartige Identität eines Objects'),
    'creationdate': fields.DateTime(attribute='_creationdate', description='Tag der erstellung'),
    'createdby': fields.String(attribute='_createdby', description='bearbeitender User')
})

"""Alle BusinessObjects"""
user = api.inherit('User', bo, {
    'firstname': fields.String(attribute='_firstname', description='Vorname eines Users'),
    'lastname': fields.String(attribute='_lastname', description='Nachname eines Users'),
    'email': fields.String(attribute='_email', description='Email adresse eines Users'),
    'google_user_id': fields.String(attribute='_google_user_id', description='Google ID des Users'),
    'isadmin': fields.Integer(attribute='_isadmin', description='Anzeige ob Adminstatus oder nicht'),
    'spo':  fields.Integer(attribute='_spo', description='Die hinterlegte SPO eines Studentenaccounts')
})

person = api.inherit('Person', bo, {
    'firstname': fields.String(attribute='_firstname', description='Vorname einer Person'),
    'lastname': fields.String(attribute='_lastname', description='Nachname einer Person'),
    'email': fields.String(attribute='_email', description='Email adresse einer Person')
})

namedbo = api.clone('Namedbo', bo, {
    'name': fields.String(attribute='_name', description='Name eines NamedBOs'),
    'title': fields.String(attribute='_title', description='Titel eines NamedBOs')
})

"""Alle NamedBos:"""
spo = api.inherit('Spo', namedbo, {
    'start_semester': fields.Integer(attribute='_start_semester', description='Anfangssemester der SPO-gültigkeit'),
    'end_semester': fields.Integer(attribute='_end_semester', description='Endsemester der SPO-gültigkeit'),
    'studycourse': fields.Integer(attribute='_studycourse', description='Studycourse der SPO'),
    'modules':  fields.List(attribute='_modules', cls_or_instance = fields.Integer, description='Module einer SPO'),
})

spoelement = api.inherit('Spoelement', namedbo, {
    'edvnr': fields.String(attribute='_edvnr', description='EDV nr des Spoelements'),
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
    'parts':  fields.List(attribute='_parts', cls_or_instance = fields.Integer, description='Teile eines Moduls')
})

modulepart = api.inherit('Modulepart', spoelement, {
    'sws': fields.Integer(attribute='_sws', description='Anzahl der SWS des Modulteils'),
    'language': fields.String(attribute='_language', descpription='Sprache des Modulteils'),
    'description': fields.String(attribute='_description', description='Beschreibung des Modulteils'),
    'connection': fields.String(attribute='_connection', description='Verbindung zu anderen Modulteilen'),
    'literature': fields.String(attribute='_literature', description='Literatur für das Modulteil'),
    'sources': fields.String(attribute='_sources', description='Quellen'),
    'semester': fields.Integer(attribute='_semester', description='Semester des Modulteils'),
    'professor': fields.Integer(attribute='_professor', description='Prof des Modulteils'),
    'module': fields.Integer(attribute='_module', description='Das zugehörige Modul')
})

studycourse = api.inherit('StudyCourse', namedbo)

semester = api.inherit('Semester', namedbo)


"""Alles @sposystem.route('')"""


@sposystem.route('/spos')
@sposystem.response(500, 'falls es zu einem Server-seitigen Fehler kommt.')
class SpoListOperations(Resource):
    @sposystem.marshal_list_with(spo)
    #@secured
    def get(self):
        """
        Auslesen aller SPO-Objekte.
        Sollten keine SPO-Objekte verfügbar sein, so wird eine leere Sequenz zurückgegeben.
        """
        adm = Administration()
        spo_list = adm.get_all_spos()
        return spo_list

    @sposystem.marshal_with(spo, code=200)
    @sposystem.expect(expect=spo, validate=True)
    #@secured
    def post(self, **kwargs):
        """
        Erstellen eines Spo-Objekts in der Datenbank.
        """
        adm = Administration()
        proposal = Spo.from_dict(api.payload)

        if proposal is not None:
            newspo = adm.create_spo(proposal, kwargs['user'])
            return newspo, 200
        else:
            return '', 500


''' @sposystem.route('/spos/all/<int:id>')
@sposystem.response(500, 'falls es zu einem Server-seitigen Fehler kommt.')
class SpoListOperations(Resource):
    @sposystem.marshal_list_with(spo)
    @secured
    def get(self, id):
        """
        Auslesen aller SPO-Objekte.
        Sollten keine SPO-Objekte verfügbar sein, so wird eine leere Sequenz zurückgegeben.
        """
        adm = Administration()
        spo = adm.get_spo_by_id(id)
        return spo '''


@sposystem.route('/spos/<int:id>')
@sposystem.response(500, 'falls es zu einem Server-seitigen Fehler kommt.')
@sposystem.param('id', 'Die ID des SPO-Objekts')
class SpoOperations(Resource):

    @sposystem.marshal_with(spo)
    #@secured
    def get(self, id):
        """
        Auslesen eines bestimmten SPO-Objekts.
        Das auszulesende Objekt wird durch die ```id``` in dem URI bestimmt.
        """
        adm = Administration()
        s = adm.get_spo_by_id(id)
        return s


@sposystem.route('/spo/hash/<int:spo_hash>')
@sposystem.response(500, 'falls es zu einem Server-seitigen Fehler kommt.')
@sposystem.param('spo_hash', 'Der Hash des SPO-Objekts')
class SpoOperations(Resource):

    @sposystem.marshal_with(spo)
    #@secured
    def get(self, spo_hash):
        """
        Auslesen eines bestimmten SPO-Objekts.
        Das auszulesende Objekt wird durch den ```spo_hash``` in dem URI bestimmt.
        """
        adm = Administration()
        s = adm.get_spo_by_hash(spo_hash)
        print(s)
        return s

    #@secured
    def delete(self, spo_hash):
        """
        Löschen eines bestimmten SPO-Objekts.
        Das zu löschende Objekt wird durch die ```spo_hash``` in dem URI bestimmt.
        """
        adm = Administration()
        s = adm.get_spo_by_hash(spo_hash)
        adm.delete_spo(s)
        return '', 200


@sposystem.route('/spo-by-startsemester-and-studycourse/<int:semester_hash>/<int:studycourse_hash>')
@sposystem.response(500, 'falls es zu einem Server-seitigen Fehler kommt.')
@sposystem.param('semester_hash', 'Der Hash des Startsemesters')
@sposystem.param('studycourse_hash', 'Der Hash des Studiengangs')
class SpoSemStudOperations(Resource):

    @sposystem.marshal_with(spo)
    @secured
    def get(self, semester_hash, studycourse_hash):
        """
        Auslesen eines bestimmten SPO-Objekts.
        Das auszulesende Objekt wird durch die ```id``` in dem URI bestimmt.
        """
        adm = Administration()
        s = adm.get_spo_by_startsem_studycourse(semester_hash, studycourse_hash)
        return s


@sposystem.route('/spos/studycourse/<int:id>')
@sposystem.response(500, 'falls es zu einem Server-seitigen Fehler kommt.')
@sposystem.param('id', 'Die ID des SPO-Objekts')
class SpoOperations(Resource):
    @sposystem.marshal_list_with(spo)
    # @secured
    def get(self, id):
        adm = Administration()
        s = adm.get_all_by_studycourse(id)
        return s

    @secured
    def delete(self, spo_hash):
        adm = Administration()
        s = adm.get_spo_by_hash(spo_hash)
        adm.delete_spo(s)
        return '', 200


@sposystem.route('/modules')
@sposystem.response(500, 'falls es zu einem Server-seitigen Fehler kommt.')
class ModuleListOperations(Resource):
    @sposystem.marshal_list_with(module, code=200)
    # @secured
    def get(self):

        adm = Administration()
        modules = adm.get_all_modules()
        return modules

    @sposystem.marshal_with(module, code=200)
    @sposystem.expect(module)
    @secured
    def post(self, **kwargs):
        """
        Erstellen eines Module-Objekts in der Datenbank.
         """
        adm = Administration()
        proposal = Module.from_dict(api.payload)

        if proposal is not None:
            mo = adm.create_module(proposal, kwargs['user'])
            return mo, 200
        else:
            return '', 500


@sposystem.route('/modules/<int:id>')
@sposystem.response(500, 'falls es zu einem Server-seitigen Fehler kommt.')
@sposystem.param("id", "Die id des Modules")
class ModuleOperations(Resource):
    @sposystem.marshal_with(module)
    # @secured
    def get(self, id):
        """Auslesen eines bestimmten Modul-Objekts"""
        adm = Administration()
        mo = adm.get_module_by_id(id)
        return mo

    @secured
    def delete(self, id):
        """Löschen eines bestimmten Module-Objekts.
        Das zu löschende Objekt wird durch die ```id``` in dem URI bestimmt."""

        adm = Administration()
        mo = adm.get_module_by_id(id)
        adm.delete_module(mo)
        return '', 200


@sposystem.route('/module/hash/<int:module_hash>')
@sposystem.response(500, 'falls es zu einem Server-seitigen Fehler kommt.')
@sposystem.param("module_hash", "Der Hash des Modules")
class ModuleHashOperations(Resource):
    @sposystem.marshal_with(module)
    @secured
    def get(self, module_hash):
        """Auslesen eines durch hash bestimmten Modul-Objekts"""
        adm = Administration()
        mo = adm.get_module_by_hash(module_hash)
        return mo

    @secured
    def delete(self, module_hash):
        """Löschen eines bestimmten Module-Objekts.
        Das zu löschende Objekt wird durch den hash in dem URI bestimmt."""

        adm = Administration()
        mo = adm.get_module_by_hash(module_hash)
        adm.delete_module(mo)
        return '', 200


@sposystem.route('/module/spo/<int:spo_hash>')
@sposystem.response(500, 'Falles es zu einem Server-seitigen Fehler kommt.')
@sposystem.param('spo_hash', 'Der Hash der SPO')
class ModuleSpoOperations(Resource):
    @sposystem.marshal_with(module)
    @secured
    def get(self, spo_hash):
        adm = Administration()
        mo = adm.get_all_by_spo(spo_hash)
        return mo


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
    @secured
    def post(self, **kwargs):
        """
        Erstellen eines Modulepart-Objekts in der Datenbank.
        """
        adm = Administration()
        proposal = Modulepart.from_dict(api.payload)
        if proposal is not None:
            mopart = adm.create_modulepart(proposal, kwargs['user'])
            return mopart, 200
        else:
            return '', 500


@sposystem.route('/moduleparts/<int:id>')
@sposystem.response(500, 'falls es zu einem Server-seitigen Fehler kommt.')
@sposystem.param("id", "Die id des Moduleparts")
class ModulePartOperations(Resource):
    @sposystem.marshal_with(modulepart)
    # @secured
    def get(self, id):
        """Auslesen eines bestimmten Modulepart-Objekts"""
        adm = Administration()
        mopart = adm.get_modulepart_by_id(id)
        return mopart

    @secured
    def delete(self, id):
        """Löschen eines bestimmten Modulepart-Objekts.
        Das zu löschende Objekt wird durch die ```id``` in dem URI bestimmt."""

        adm = Administration()
        mopart = adm.get_modulepart_by_id(id)
        adm.delete_modulepart(mopart)
        return '', 200


@sposystem.route('/moduleparts/<int:modulepart_hash>')
@sposystem.response(500, 'falls es zu einem Server-seitigen Fehler kommt.')
@sposystem.param("modulepart_hash", "Der Hash des Moduleparts")
class ModulePartOperations(Resource):
    @sposystem.marshal_with(modulepart)
    @secured
    def get(self, modulepart_hash):
        """Auslesen eines durch den Hash bestimmten Modulepart-Objekts"""
        adm = Administration()
        mopart = adm.get_modulepart_by_hash(modulepart_hash)
        return mopart


@sposystem.route('/modulepart/<int:module_hash>')
@sposystem.response(500, 'Falls es zu einem Server-seitigen Fehler kommt.')
@sposystem.param('module_hash', 'Der Hash des Modules')
class ModulePartModuleOperations(Resource):

    @sposystem.marshal_list_with(modulepart)
    #@secured
    def get(self, module_hash):
        adm = Administration()
        mopart = adm.get_modulepart_by_module(module_hash)
        return mopart


@sposystem.route('/users')
@sposystem.response(500, 'falls es zu einem Server-seitigen Fehler kommt.')
class UserListOperations(Resource):    
    @sposystem.marshal_list_with(user)
    # @secured
    def get(self):
        """
        Auslesen aller User Objekte.
        Sollte kein User Objekt verfügbar sein, wird eine leere Sequenz zurückgegeben
        """
        adm = Administration()
        users = adm.get_all_users()
        return users

    @sposystem.marshal_list_with(user, code=200)
    @sposystem.expect(user)
    #@secured
    def post(self, **kwargs):
        """
        Erstellen eines User-Objekts in der Datenbank.
        """
        adm = Administration()
        proposal = User.from_dict(api.payload)

        if proposal is not None:
            c = adm.create_user(proposal, kwargs['user'])
            return c, 200
        else:
            return '', 500

    @sposystem.marshal_with(user)
    @sposystem.expect(user, validate=True)
    #@secured
    def put(self, id, **kwargs):
        """
        Update eines bestimmten User-Objekts.\n
        **ACHTUNG: ** relevante id ist die id, die mittels URI bereitgestellt und somit als Methodenparameter
        verwendet wird. Dieser Parameter überschreibt das ID-Attribut des im Payload der Anfrage übermittelten
        User-Objekts.
        """
        adm = Administration()
        us = User.from_dict(api.payload)

        if us is not None:
            """Hierdurch wird die id des zu überschreibenden (vgl. Update) Customer-Objekts gesetzt.
            Siehe Hinweise oben."""

            us.set_id(id)
            adm.save_user(us, kwargs['user'])
            return '', 200
        else:
            return '', 500


@sposystem.route('/user/<int:user_hash>')
@sposystem.response(500, 'Falls es zu einem Server-seitigen Fehler kommt.')
@sposystem.param('lastname', 'Der Hash des User-Objekts')
class ModuleHashOperations(Resource):
    @sposystem.marshal_with(user)
    @secured
    def get(self, user_hash):
        """
        Auslesen eines Customer-Objekts, das durch sein Hash bestimmt wird.\n
        Das auszulesende Objekt wird durch ```user_hash``` in dem URI bestimmt.
        """
        adm = Administration()
        us = adm.get_user_by_hash(user_hash)
        return us

    @secured
    def delete(self, user_hash: int):
        """
        Löschen eines bestimmten User-Objekts.\n
        Das zu löschende Objekt wird durch die ```id``` in dem URI bestimmt.
        """
        adm = Administration()
        us = adm.get_user_by_hash(user_hash)
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
        Auslesen von Customer-Objekten, die durch den Nachnamen bestimmt werden.\n
        Die auszulesenden Objekte werden durch ```lastname``` in dem URI bestimmt.
        """
        adm = Administration()
        us = adm.get_user_by_name(lastname)
        return us


@sposystem.route('/studycourses')
@sposystem.response(500, 'falls es zu einem Server-seitigen Fehler kommt.')
class StudycourseListOperations(Resource):
    @sposystem.marshal_list_with(studycourse)
    #@secured
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
    @secured
    def post(self, **kwargs):
        """
        Erstellen eines StudyCourse-Objekts in der Datenbank.
        """
        adm = Administration()
        proposal = StudyCourse.from_dict(api.payload)

        if proposal is not None:
            sc = adm.create_studycourse(proposal, kwargs['user'])
            return sc, 200
        else:
            return'', 500


@sposystem.route('/studycourse/<int:id>')
@sposystem.response(500, 'Falls es zu einem Server-seitigen Fehler kommt.')
@sposystem.param('id', 'Die ID des Studycourse-Objekts')
class StudycourseOperations(Resource):
    @sposystem.marshal_with(studycourse)
    # @secured
    def get(self, id):
        """Auslesen eines bestimmten Studycourse-Objekts.
        Das auszulesende Objekt wird durch die```id```in dem URI bestimmt."""

        adm = Administration()
        sc = adm.get_all_by_studycourse(id)
        return sc

    @secured
    def delete(self, id):
        """Löschen eines bestimmten Studycourse-Objekts.
        Das zu löschende Objekt wird durch die```id```in dem URI bestimmt."""

        adm = Administration()
        sc = adm.get_studycourse_by_id(id)
        adm.delete_studycourse(sc)
        return'', 200


@sposystem.route('/studycourse/<int:studycourse_hash>')
@sposystem.response(500, 'falls es zu einem Server-seitigen Fehler kommt.')
@sposystem.param("studycourse_hash", "Der Hash des Studiengangs")
class ModulePartOperations(Resource):
    @sposystem.marshal_with(studycourse)
    @secured
    def get(self, studycourse_hash):
        adm = Administration()
        sc = adm.get_studycourse_by_hash(studycourse_hash)
        return sc


@sposystem.route('/persons')
@sposystem.response(500, 'falls es zu einem Server-seitigen Fehler kommt.')
class PersonListOperations(Resource):
    @sposystem.marshal_list_with(person)
    # @secured
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
    @secured
    def post(self, **kwargs):
        """
        Erstellen eines Person-Objekts in der Datenbank.
        """

        adm = Administration()
        proposal = Person.from_dict(api.payload)

        if proposal is not None:
            pe = adm.create_person(proposal, kwargs['user'])
            return pe, 200
        else:
            return'', 500


@sposystem.route('/persons/<int:id>')
@sposystem.response(500, 'Falls es zu einem Server-seitigen Fehler kommt.')
@sposystem.param('id', 'Die ID des Person-Objekts')
class PersonOperations(Resource):
    @sposystem.marshal_with(person)
    # @secured
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


@sposystem.route('/person/<int:person_hash>')
@sposystem.response(500, 'falls es zu einem Server-seitigen Fehler kommt.')
@sposystem.param("person_hash", "Der Hash der Person")
class ModulePartOperations(Resource):
    @sposystem.marshal_with(studycourse)
    @secured
    def get(self, person_hash):
        adm = Administration()
        pe = adm.get_person_by_hash(person_hash)
        return pe

    @secured
    def delete(self, person_hash):
        """Löschen eines bestimmten Person-Objekts.
        Das zu löschende Objekt wird durch die```id```in dem URI bestimmt."""

        adm = Administration()
        pe = adm.get_person_by_id(person_hash)
        adm.delete_person(pe)
        return '', 200


@sposystem.route('/semesters')
@sposystem.response(500, 'falls es zu einem Server-seitigen Fehler kommt.')
class SemesterListOperations(Resource):
    @sposystem.marshal_list_with(semester, code=200)
    # @secured
    def get(self):

        adm = Administration()
        semesters = adm.get_all_semesters()
        return semesters

    @sposystem.marshal_with(semester, code=200)
    @sposystem.expect(semester)
    @secured
    def post(self, **kwargs):
        """
        Erstellen eines Semester-Objekts in der Datenbank.
        """
        adm = Administration()
        proposal = Semester.from_dict(api.payload)
        if proposal is not None:
            se = adm.create_semester(proposal, kwargs['user'])
            return se, 200
        else:
            return '', 500


@sposystem.route('/studycourse/<int:studycourse_hash>')
@sposystem.response(500, 'falls es zu einem Server-seitigen Fehler kommt.')
@sposystem.param("studycourse_hash", "Der Hash des Studiengangs")
class ModulePartOperations(Resource):
    @sposystem.marshal_with(studycourse)
    @secured
    def get(self, studycourse_hash):
        adm = Administration()
        sc = adm.get_studycourse_by_hash(studycourse_hash)
        return sc

    @secured
    def delete(self, id):
        """Löschen eines bestimmten Semester-Objekts.
        Das zu löschende Objekt wird durch die ```id``` in dem URI bestimmt."""

        adm = Administration()
        se = adm.get_semester_by_id(id)
        adm.delete_semester(se)
        return '', 200


"""**ACHTUNG:** Diese Zeile wird nur in der lokalen Entwicklungsumgebung ausgeführt und hat in der Cloud keine Wirkung!
"""

print(app.url_map)

if __name__ == '__main__':
    app.run(debug=True)
