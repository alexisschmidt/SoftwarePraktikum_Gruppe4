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
namedbo = api.inherit('Namedbo', bo){
    'name': fields.string(attribute='_name', description='Name eines NamedBOs')
    'title': fields.string(attribute='_name', description='Titel eines NamedBOs')
}

spo = api.inherit('Spo', namedbo){
    'start_date': fields.date(attribute='_start_date', description='Anfangsdatum der SPO-gültigkeit'),
    'end_date': fields.date(attribute='_end_date', description='Enddatum der SPO-gültigkeit')
}




"""Alles @sposystem.route('')"""



"""**ACHTUNG:** Diese Zeile wird nur in der lokalen Entwicklungsumgebung ausgeführt und hat in der Cloud keine Wirkung!
"""
if __name__ == '__main__':
    app.run(debug=True)