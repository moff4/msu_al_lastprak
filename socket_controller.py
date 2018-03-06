#!/usr/bin/env python3.6

import json
import controller

class Socket_Controller(controller.Controller):
	def __init__(self,conn):
		super(controller.Controller, self).__init__()
		self.conn = conn # connector.Connector

	#
	# main loop # do all that should do
	#
	def loop(self):
		while True:
			self.run_command(json.loads(self.conn.read_msg()))