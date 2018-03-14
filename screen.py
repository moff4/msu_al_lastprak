#!/usr/bin/env python3.6

import tkinter as tk
import time

from engine import Engine
from basic_tank import Basic_Tank
from user_controller import User_Controller as user_cntl
from socket_controller import Socket_Controller as sock_cntl
import conf
from threading import Thread

#
# Screen with main picturebox
#
class Screen:
	def __init__(self,conn,left=True):
		# self.root = tk.Tk(screenName=conf.Screen_ScreenName)
		self.root = tk.Tk()
		self.root.configure(background=conf.Screen_BackgroundColor)
		self.root.geometry('%sx%s+%s+%s'%(str(conf.Screen_width),str(conf.Screen_height),str(conf.Screen_left),str(conf.Screen_top)))
		self.left = left
		self.conn = conn # change on controllers
		self.fps_delay = int(1000.0/conf.fps)
		
		self.canvas = tk.Canvas(self.root, width=conf.Game_window_width, height=conf.Game_window_height,background="#FFFFFF")
		__cc = int((conf.Screen_width-conf.Game_window_width)/2)
		self.canvas.place(x=__cc,y=__cc)

		self.engine = Engine(self.canvas,draw_landscape = left)
		self.left = left
		if left:
			self.conn.send_weight(self.engine.get_weights())#self.connector.send_weight(self.engine.get_weights())
			self.place_tanks()
		else:
			self.conn.ping()

		self.user_cntl = None
		self.sock_cntl = None
		self.fork()
		
		self.go = True

		text= ""
		avr = 0.0
		SUBSTR = "<LEFT-OR-RIGHT>"
		for i in conf.Screen_help_msg:
			if SUBSTR in i:
				if left:
					position = conf.Screen_left_pos
				else:
					position = conf.Screen_right_pos
				j = i[:i.find(SUBSTR)-1] + position + i[i.find(SUBSTR)+len(SUBSTR):]
			else:
				j = i
			text += j + "\n"
			avr += len(i)
		avr /= len(conf.Screen_help_msg)
		width = min([0.8*conf.Screen_width,int(avr)*10])
		height = len(conf.Screen_help_msg) * 20
		message = tk.Message(self.root, text=text, background=conf.Screen_BackgroundColor,width=width)
		left = (conf.Screen_width - width)/2
		message.place(y = conf.Game_window_height + int(__cc * 1.5),x=left)
	
	#
	# main loop
	#
	def run(self):
		if not self.left:
			while not self.engine.is_ready():
				time.sleep(0.5)
		self.draw_picture()
		self.root.mainloop()
		self.wait()

	#
	# place tanks
	#
	def place_tanks(self,x1=None,x2=None):
		x1 , x2 = self.engine.place_tanks()
		self.conn.send_tanks(x1,x2)


	#
	# start controller's
	#
	def fork(self):		
		self.user = user_cntl(self.conn,self.engine,self.left)
		self.user_cntl = Thread(target=self.user.loop,args=[])
		self.user_cntl.start()
		
		self.sock = sock_cntl(self.conn,self.engine,not self.left)
		self.sock_cntl = Thread(target=self.sock.loop,args=[])
		self.sock_cntl.start()

	#
	# wait for both threads
	#
	def wait(self):
		try:
			self.conn.close()
			for i in [self.user_cntl,self.sock_cntl]:
				if i != None:
					i.join()
		except:
			pass

	#
	#
	#
	def stop_game(self):
		self.go = False
		self.sock.stop()
		self.user.stop()
		self.engine.clean()
		self.engine.print_end()
		self.wait()

	#
	# callback from timer to draw picture
	#
	def draw_picture(self):
		print('---DRAW---')
		if self.go:
			self.root.after(self.fps_delay,self.draw_picture)
			self.engine.single_draw()
			if not self.engine.check_game():
				self.stop_game()

if __name__ == '__main__':
	Screen(None).run()


