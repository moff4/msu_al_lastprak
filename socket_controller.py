#!/usr/bin/env python3.6

import json
import controller

class Socket_Controller(controller.Controller):
	def __init__(self,conn,engine,left=True):
		super(controller.Controller, self).__init__()#super(controller.Controller, self).__init__(engine)
		self.engine = engine
		self.conn = conn # connector.Connector
		self.left = left # if that user's tank is left one
		self.go = True


	#
	# set stop flag
	#
	def stop(self):
		self.go = False

	#
	# main loop # do all that should do
	#
	def loop(self):
		while self.go:
			msg = self.conn.read_msg()
			if msg != None:
				msg = json.loads(msg)
				if 'weights' in msg:
					self.engine.set_weights()
				elif 'left_x' in msg:
					self.engine.place_tanks(msg['left_x'],msg['right_x'])
				else:
					self.run_command(msg)
			else:
				self.go = False
