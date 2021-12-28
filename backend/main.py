# -- coding:utf-8 --

from flask import Flask
from flask_restx import Api, Resource, fields
from flask_cors import CORS

# Wir greifen natürlich auf unsere Applikationslogik inkl. BusinessObject-Klassen zurück
from server.bo.Businessobject import BusinessObject
from server.bo.NamedBo import NamedBo
from server.bo.Spo import Spo
from server.bo.SpoElement import SpoElement
from server.bo.Module import Module
from server.bo.Modulepart import Modulepart
from server.bo.StudyCourse import StudyCourse
from server.bo.Person import Person
from server.bo.User import User

from server.Administration import Administration

# Außerdem nutzen wir einen selbstgeschriebenen Decorator der die Authentifikation übernimmt
from server.SecurityDecorator import secured

app = Flask(__name__)
CORS(app, resources=r'/sopra/*')

api = Api(app, version='1.0', title='Sopra API',
          description='Datenverarbeitungssystem für SpOs.')

"""Alegen von Namespaces 
Namespaces erlauben uns die Strukturierung von APIs.
"""
sposystem = api.namespace('sopra', description='Funktionen des SpoSystems')

"""Nachfolgend werden analog zu unseren BusinessObject-Klassen transferierbare Strukturen angelegt.
BusinessObject dient als Basisklasse, auf der die weiteren Strukturen "" aufsetzen."""

bo = api.model('BusinessObject', {
    'id': fields.Integer(attribute='_id', description='Einzigartige Identität eines Objects')
})

"""Alle anderen BusinessObjects"""
user = api.inherit('User', 'BusinessObject', {
    'firstname': fields.String(attibute='__firstname', description='Vorname eines Users'),
    'lastname': fields.String(attibute='__lastname', description='Nachname eines Users'),
    'email': fields.String(attibute='__email', description='Emailadresse eines Users')
})

namedbo = api.inherit('Namedbo', bo, {
    'name': fields.String(attribute='_name', description='Name eines NamedBOs'),
    'title': fields.String(attribute='_name', description='Titel eines NamedBOs')
})

spo = api.inherit('Spo', namedbo, {
    'start_date': fields.Date(attribute='_start_date', description='Anfangsdatum der SPO-gültigkeit'),
    'end_date': fields.Date(attribute='_end_date', description='Enddatum der SPO-gültigkeit')
})

spoelement = api.inherit('Spoelement', namedbo, {
    'edvnr': fields.String(attibute='_edvnr', description='EDV nr des Spoelements'),
    'ects': fields.String(attibute='_ects', description=''),
    'workload': fields.String(attibute='_workload',
                              description='Arbeitszeit für das Spoelement und ihre Zusammensetzung')
})

module = api.inherit('Module', namedbo, {
    'type': fields.String(attribute='_type', description='Typ des Moduls'),
    'requirement': fields.String(attribute='_requirement', description='Voraussetzungen für das Modul'),
    'outcome': fields.String(attribute='_outcome', description='Outcome des Moduls'),
    'examtype': fields.String(attribute='_examtype', description='Prüfungstyp des Moduls'),
    'instructor': fields.String(attribute='_instructor', description='Modulverantwortlicher')
})

modulepart = api.inherit('Modulepart', namedbo, {
    'sws': fields.String(attribute='_sws', description='Anzahl der SWS des Modulteils'),
    'language': fields.String(attribute='_language', descpription='Sprache des Modulteils'),
    'description': fields.String(attibute='_description', attribute='Beschreibung des Modulteils'),
    'connection': fields.String(attibute='_connection', attribute='Verbindung zu anderen Modulteilen'),
    'literature': fields.String(attibute='_literature', attribute='Literatur für das Modulteil'),
    'sources': fields.String(attibute='_sources', attribute='Quellen'),
    'semester': fields.String(attibute='_semester', attribute='Semester des Modulteils')
})

studycourse = api.inherit('StudyCourse', namedbo)

person = api.inherit('Person', namedbo, {
    'firstname': fields.String(attibute='__firstname', description='Vorname einer Person'),
    'lastname': fields.String(attibute='__lastname', description='Nachname einer Person'),
    'email': fields.String(attibute='__email', description='Emailadresse einer Person')
})

"""Alles @sposystem.route('')"""



@sposystem.route('/users')
@sposystem.response(500, 'falls es zu einem Server-seitigen Fehler kommt.')
class UserListOperations(Resource):

    @sposystem.marshal_with(user, code=200)
    @sposystem.expect(user)
    @secured
    def post(self):

        adm = Administration()
        proposal = User.from_dict(api.payload)

        if proposal is not None:
            c = adm.create_user(proposal.get_firstname(), proposal.get_lastname(), proposal.get_email())
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

    @secured
    def delete(self, id):
        """Löschen eines bestimmten User-Objekts.
        Das zu löschende Objekt wird durch die ```id``` in dem URI bestimmt."""

        adm = Administration()
        us = adm.get_user_by_id(id)
        adm.delete_user(us)
        return '', 200

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


@sposystem.route('/spos/<int:id>')
@sposystem.response(500, 'falls es zu einem Server-seitigen Fehler kommt.')
@sposystem.param('id', 'Die ID des SPO-Objekts')
class SpoOperations(Resource):
    @sposystem.marshal_with(spo)
    @secured
    def get(self, id):
        """
        Auslesen eines bestimmten SPO-Objekts.
        Das auszulesende Objekt wird durch die ```id``` in dem URI bestimmt.
        """

        adm = Administration()
        spo = adm.get_spo_by_id(id)
        return spo

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

    @sposystem.marshal_with(spo)
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

    @sposystem.marshal_with(spo, code=200)
    @sposystem.expect(spo)
    @secured
    def post(self, id):

        adm = Administration()
        proposal = User.from_dict(api.payload)

        if proposal is not None:
            c = adm.create_user(proposal.get_firstname(), proposal.get_lastname(), proposal.get_email())
            return c, 200
        else:
            return '', 500



"""**ACHTUNG:** Diese Zeile wird nur in der lokalen Entwicklungsumgebung ausgeführt und hat in der Cloud keine Wirkung!
"""
if __name__ == '__main__':
    app.run(debug=True)
