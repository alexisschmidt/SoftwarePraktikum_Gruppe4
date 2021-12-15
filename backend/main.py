#-- coding:utf-8 --

from flask import Flask
from flask_restx import Api, Resource, fields
from flask_cors import CORS

from server.Administration import Administration
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


"""Alles @sposystem.route('')"""



"""**ACHTUNG:** Diese Zeile wird nur in der lokalen Entwicklungsumgebung ausgeführt und hat in der Cloud keine Wirkung!
"""
if __name__ == '__main__':
    app.run(debug=True)