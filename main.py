from mybluetooth import BluetoothManager
import bluetooth
import time

from flask import Flask
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

device = BluetoothManager('/dev/rfcomm0')

class HelloWorld(Resource):
	def get(self):
		device.write('luz')
		time.sleep(2)
		device.write('apagar luz')
		return {'hello': 'world'}

class TurnOnLights(Resource):
	def get(self):
		device.write('luz')
		return {'lights': 'on'}

class TurnOffLights(Resource):
	def get(self):
		device.write('apagar luz')
		return {'lights': 'off'}

api.add_resource(HelloWorld, '/')
api.add_resource(TurnOnLights, '/api/turn_on')
api.add_resource(TurnOffLights, '/api/turn_off')

if __name__ == '__main__':
	app.run(host= '0.0.0.0', debug=True)
