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
		self.fps_landscape = int(1000.0/conf.fps_landscape)
		
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

		stop_button = tk.Button(self.root,text=conf.stop_button_name,fg=conf.MainMenu_BackgroundColor)
		stop_button.bind("<Button-1>", self.stop_game)
		stop_button.place(height=21,width=120,x=70,y=conf.Game_window_height+20)

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
		try:
			if not self.left:
				while not self.engine.is_ready():
					time.sleep(0.5)
			self.draw_picture()
			self.draw_landscape()
			print('loop-start')
			self.root.mainloop()
			print('loop-stop')
		except SystemExit:
			print('loop-system')
		except BaseException:
			print('loop-base')
		finally:
			print('loop-finally-start')
			self.wait()
			print('loop-finally-middle')
			self.root.destroy()
			print('loop-finally-stop')

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
		except:
			pass
		for i in [self.user_cntl,self.sock_cntl]:
			try:
				if i != None:
					i.join()
			except:
				pass

	#
	# return True if any of threads are dead
	#
	def check_game(self):
		try:
			boo = self.user_cntl.is_alive() and self.sock_cntl.is_alive()
			if boo:
				self.print_end()
			return boo
		except:
			return True

	#
	# instructions to stop the game
	#
	def stop_game(self,event):
		self.go = False
		try:
			self.sock.stop()
		except Exception as e:
			print('stop-game: %s'%e)
		try:
			self.user.stop()
		except Exception as e:
			print('stop-game: %s'%e)
		try:
			self.engine.print_end()
		except Exception as e:
			print('stop-game: %s'%e)
		time.sleep(5.0)
		raise BaseException('Must be!')

	#
	# callback from timer to draw picture
	#
	def draw_picture(self):
		if self.go:
			self.root.after(self.fps_delay,self.draw_picture)
			self.engine.single_draw()
			if self.engine.check_game() or not self.check_game():
				self.stop_game('just suka stop')

	#
	# callback from timer to draw picture
	#
	def draw_landscape(self):
		if self.go:
			self.root.after(self.fps_landscape,self.draw_landscape)
			self.engine.draw_landscape()

if __name__ == '__main__':
	Screen(None).run()


