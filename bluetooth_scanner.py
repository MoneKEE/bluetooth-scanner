import cb
import struct
import time
import binascii
import numpy as np
from time import sleep
from console import clear

class MyCentralManagerDelegate (object):
	def __init__(self):
		self.peripheral = None
		self.p_list = [['name','peripheral_id','state','service_id', 'is_primary', 'characteristic_id', 'value', 'notifying', 'properties']]

	def print_list(self,p):
		print('********************************')
		for row in self.p_list:
			print(row)
		print('********************************')
		sleep(1)
		clear()

	def did_update_state(self):
		print('*** Peripheral %s state updated: %s' % (self.peripheral.name, self.peripheral.state))

	def did_discover_peripheral(self, p):
		p_uuids = [item[1] for item in self.p_list[1:]]

		if p.uuid not in p_uuids:
			print('+++ Discovered peripheral: %s (%s)' % (p.name, p.uuid))
			self.p_list.append([p.name,p.uuid,'','','','','','',''])
			#self.print_list(self.p_list)
		if p.name and '1109' in p.name:	
			self.peripheral = p
			cb.connect_peripheral(self.peripheral)

	def did_connect_peripheral(self, p):
		clear()
		print('*** Connected %s state: %s' % (p.name, p.state))
		print('*** Discovering services for %s...' % p.name)
		'''
		index = [item[1] for item in self.p_list].index(p.uuid)
		self.p_list[index][2] = p.state
		'''
		cb.stop_scan()
		p.discover_services()

	def did_fail_to_connect_peripheral(self, p, error):
		print('+++ Failed to connect to %s' % p.name)
		print('+++ Resuming scan...')
		cb.scan_for_peripherals()

	def did_disconnect_peripheral(self, p, error):
		print('*** Disconnected %s, error: %s' % (p.name, error,))
		self.peripheral = None
		print('+++ Resuming scan...')
		cb.scan_for_peripherals()

	def did_discover_services(self, p, error):
		'''
		services_list = []
		index = [item[1] for item in self.p_list].index(p.uuid)
		'''
		for s in p.services:
			print('*** service id: %s / primary?: %s' % (s.uuid, s.primary))
			print('*** Discovering characteristics...')

			#Update p_list with the discovered service info
			'''
			if s.uuid not in [item[3] for item in self.p_list if item[1] == p.uuid]:			
				if self.p_list[index][3] == '':
					self.p_list[index][3] = s.uuid
					self.p_list[index][4] = s.primary
				else:
					tmp_list = self.p_list[index]
					self.p_list.insert(index+1,tmp_list[:3] + [s.uuid,s.primary] + ['','','',''])
					'''

		#self.print_list(self.p_list)		

			p.discover_characteristics(s)

	def did_discover_characteristics(self, s, error):
		print('*** %s characteristics:' % s.uuid)
		for c in s.characteristics:

			self.peripheral.read_characteristic_value(c)
			self.peripheral.set_notify_value(c, True)
			print('*** 	characteristic id: %s / value: %s / notifying: %s / properties: %s' % (c.uuid, c.value, c.notifying, c.properties))

			'''
			if c.uuid not in [item[5] for item in self.p_list if item[3] == s.uuid]:			
				if self.p_list[index][5] == '':
					self.p_list[index][5] = c.uuid
					self.p_list[index][6] = c.value
					self.p_list[index][6] = c.notifying
					self.p_list[index][6] = c.properties
				else:
					tmp_list = self.p_list[index]
					self.p_list.insert(index+1,tmp_list[:3] + [s.uuid,s.primary,'','','',''])
			'''

	def did_write_value(self, c, error):
		pass

	def did_update_value(self, c, error):
		print('*** %s updated value: %s' % (c.uuid, c.value.encode('hex')))

delegate = MyCentralManagerDelegate()
print('Scanning for peripherals...')
cb.set_verbose(False)
cb.set_central_delegate(delegate)
cb.scan_for_peripherals()

# Keep the connection alive until the 'Stop' button is pressed:
try:
	while True: pass

except KeyboardInterrupt:
	# Disconnect everything:
	cb.reset()
