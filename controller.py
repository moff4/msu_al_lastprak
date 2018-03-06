#!/usr/bin/env python3.6

class Controller:
	def __init__(self,engin):
		self.engin = engin

	#
	# dick = {
	#	"tank" = "left" | "right"
	#	"cmd" = "move" | "power" | "angle" | "fire"
	#	"arg" = smth (or nothing) that depends on cmd
	# }
	#
	def run_command(self,dick):
		index = int(dick["tank"] == "right") # 0 - left , right - 1
		cmd = dick["cmd"]
		if  cmd  == "move":
			self.engin.Tank[index].promise_move(dick["arg"])
		elif cmd == "power":
			self.engin.Tank[index].change_angle(dick["arg"])
		elif cmd == "angle":
			self.engin.Tank[index].change_power(dick["arg"])
		elif cmd == "fire":
			self.engin.Tank[index].fire()
		else:
			pass