from contextlib import redirect_stdout
import sys

class BluetoothManager(object):

	device = None

	def __init__(self, device):
		self.device = device

	def write(self, msg):
		old_stdout = sys.stdout
		sys.stdout = open(self.device, 'w')
		print(msg)
		sys.stdout = old_stdout
