#-- coding:utf-8 --

from flask import Flask
from flask_restx import Api, Resource, fields
from flask_cors import CORS

# Wir greifen natürlich auf unsere Applikationslogik inkl. BusinessObject-Klassen zurück
from server.bo.Businessobject import BusinessObject
from server.bo.NamedBo import NamedBo
from server.bo.Spo import Spo
from server.bo.SpoElement import  SpoElement
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
user = api.inherit('User', BusinessObject, {
    'firstname': fields.String(attibute='__firstname', description='Vorname eines Users'),
    'lastname': fields.String(attibute='__lastname', description='Nachname eines Users'),
    'email': fields.String(attibute='__email', description='Emailadresse eines Users')
})

namedbo = api.inherit('Namedbo', bo,{
    'name': fields.String(attribute='_name', description='Name eines NamedBOs'),
    'title': fields.String(attribute='_name', description='Titel eines NamedBOs')
})

spo = api.inherit('Spo', namedbo, {
    'start_date': fields.Date(attribute='_start_date', description='Anfangsdatum der SPO-gültigkeit'),
    'end_date': fields.Date(attribute='_end_date', description='Enddatum der SPO-gültigkeit')
})

spoelement = api.inherit('Spoelement', namedbo,{
    'edvnr': fields.String(attibute='_edvnr', description='EDV nr des Spoelements'),
    'ects': fields.String(attibute='_ects', description=''),
    'workload': fields.String(attibute='_workload', description='Arbeitszeit für das Spoelement und ihre Zusammensetzung')
})

module = api.inherit('Module', namedbo, {
    'type': fields.String(attribute='_type', description='Typ des Moduls'),
    'requirement': fields.String(attribute='_requirement', description='Voraussetzungen für das Modul'),
    'outcome': fields.String(attribute='_outcome', description='Outcome des Moduls'),
    'examtype': fields.String(attribute='_examtype', description='Prüfungstyp des Moduls'),
    'instructor': fields.String(attribute='_instructor', description='Modulverantwortlicher')
})

modulepart = api.inherit('Modulepart', namedbo,{
    'sws': fields.String(attribute='_sws', description='Anzahl der SWS des Modulteils'),
    'language': fields.String(attribute='_sanguage', descpription='Sprache des Modulteils'),
    'description': fields.String(attibute='_description', attribute='Beschreibung des Modulteils'),
    'connection': fields.String(attibute='_connection', attribute='Verbindung zu anderen Modulteilen'),
    'literature': fields.String(attibute='_literature', attribute='Literatur für das Modulteil'),
    'sources': fields.String(attibute='_sources', attribute='Quellen'),
    'semester': fields.String(attibute='_semester', attribute='Semester des Modulteils')
})

studycourse = api.inherit('StudyCourse', namedbo)

person = api.inherit('Person', namedbo,{
    'firstname': fields.String(attibute='__firstname', description='Vorname einer Person'),
    'lastname': fields.String(attibute='__lastname', description='Nachname einer Person'),
    'email': fields.String(attibute='__email', description='Emailadresse einer Person')
})




"""Alles @sposystem.route('')"""



"""**ACHTUNG:** Diese Zeile wird nur in der lokalen Entwicklungsumgebung ausgeführt und hat in der Cloud keine Wirkung!
"""
if __name__ == '__main__':
    app.run(debug=True)