#!/usr/bin/env python3.5

import json
import sys,tty,termios

import controller

class User_Controller(controller.Controller):
	def __init__(self,conn):
		super(controller.Controller, self).__init__()
		self.conn = conn # connector.Connector

	#
	# command to run & send to peer
	#
	def command(self,dic):
		self.conn.write_msg(json.dumps(dic))
		self.run_command(dic)

	#
	# button reactions
	#

	#
	# just loop
	#
	def loop(self):
		pass


class _Getch:
	def __call__(self):
			fd = sys.stdin.fileno()
			old_settings = termios.tcgetattr(fd)
			try:
				tty.setraw(sys.stdin.fileno())
				ch = sys.stdin.read(3)
			finally:
				termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
			return ch

def get():
	inkey = _Getch()
	while(1):
		k=inkey()
		if k!='':
			break
		if k=='\x1b[A':
			print("up")
		elif k=='\x1b[B':
			print("down")
		elif k=='\x1b[C':
			print("right")
		elif k=='\x1b[D':
			print("left")
		else:
			print("not an arrow key!")

def main():
	for i in range(0,20):
		get()

if __name__=='__main__':
	main()

