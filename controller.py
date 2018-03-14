#!/usr/bin/env python3.6

class Controller:
	def __init__(self):
		#self.engine = engine
		pass

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
			self.engine.Tank[index].promise_move(dick["arg"])
		elif cmd == "power":
			self.engine.Tank[index].change_angle(dick["arg"])
		elif cmd == "angle":
			self.engine.Tank[index].change_power(dick["arg"])
		elif cmd == "weapon":
			self.engine.Tank[index].change_weapon(dick["arg"])
		elif cmd == "fire":
			self.engine.Tank[index].fire()
		else:
			pass