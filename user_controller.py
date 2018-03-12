#!/usr/bin/env python3.5
import time
import json
import keyboard

import controller

class User_Controller(controller.Controller):
	def __init__(self,conn,engine,left=True):
		super(controller.Controller, self).__init__()#super(controller.Controller, self).__init__(engine)
		self.engine = engine
		self.conn = conn # connector.Connector
		if left:
			self.left = "left"
		else:
			self.left = "right"
		self.go = True
	#
	# command to run & send to peer
	#
	def command(self,dic):
		self.conn.write_msg(json.dumps(dic))
		self.run_command(dic)

	#
	# button reactions
	#
	def press(self,event):
		if event.event_type == "down" and self.go:
			boo = True
			#print("%s , %s, %s , %s , %s ."%(event.event_type,event.name,event.scan_code,type(event.scan_code),event.time))
			obj = {
				"tank": self.left
			}
			# obj = {
			#	"tank" = "left" | "right"
			#	"cmd" = "move" | "power" | "angle" | "fire"
			#	"arg" = smth (or nothing) that depends on cmd
			# }
			if event.name.lower() == 'a': # angle up 
				obj['cmd'] = "angle"
				obj['arg'] = 'add'
			elif event.name.lower() == 'd': # angle down
				obj['cmd'] = "angle"
				obj['arg'] = 'sub'
			elif event.name.lower() == 'w': # power up
				obj['cmd'] = "power"
				obj['arg'] = 'add'
			elif event.name.lower() == 's': # power down
				obj['cmd'] = "power"
				obj['arg'] = 'sub'
			elif event.name.lower() == 'q': # next weapon
				obj['cmd'] = "weapon"
				obj['arg'] = 'next'
			elif event.name.lower() == 'e': # previous weapon
				obj['cmd'] = "weapon"
				obj['arg'] = 'prev'
			elif event.name == 'space': # fire 
				obj['cmd'] = "fire"
				obj['arg'] = ''
			elif event.name in ['left','right']: # move
				obj['cmd'] = "move"
				obj['arg'] = event.name 
			else:
				boo = False
			if boo:
				self.command(obj)

	#
	# set stop flag
	#
	def stop(self):
		self.go = False

	#
	# just loop
	#
	def loop(self):
		keyboard.hook(self.press)
		self.go = True
		while self.go:
			time.sleep(1)




def main():
	User_Controller(None).loop()

if __name__=='__main__':
	main()

