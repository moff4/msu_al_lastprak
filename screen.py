#!/usr/bin/env python3.6

import tkinter as tk
import time

from engine import Engine
import user_controller as user_cntl
import socket_controller as sock_cntl
import conf

#
# Screen with main picturebox
#
class Screen:
	def __init__(self,conn,left=True):
		# self.root = tk.Tk(screenName=conf.Screen_ScreenName)
		self.root = tk.Tk()
		self.root.configure(background=conf.Screen_BackgroundColor)
		self.root.geometry('%sx%s+%s+%s'%(str(conf.Screen_width),str(conf.Screen_height),str(conf.Screen_left),str(conf.Screen_top)))
		self.conn = conn # change on controllers
		self.fps_delay = int(1000.0/conf.fps)
		
		self.canvas = tk.Canvas(self.root, width=conf.Game_window_width, height=conf.Game_window_height,background="#FFFFFF")
		__cc = int((conf.Screen_width-conf.Game_window_width)/2)
		self.canvas.place(x=__cc,y=__cc)
		
		self.user_cntl = None
		self.sock_cntl = None

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

		self.engine = Engine(self.canvas)
	#
	#
	#
	def run(self):
		self.draw_picture() # later must be uncommented
		if __name__ != "__main__":
			self.fork()
		self.root.mainloop()
		self.wait()

	#
	#
	#
	def fork(self):
		def PUSK(cl,cn):
			user_cntl(self.conn).loop()
		
		self.user_cntl = Thread(target=PUSK,args=[user_cntl,self.conn])
		self.user_cntl.start()
		
		self.sock_cntl,sock_cntl

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
	def draw_picture(self):
		self.root.after(self.fps_delay,self.draw_picture)
		self.engine.f()
		#self.engine.single_draw() # maybe need new thread ???? test this later FIXME

if __name__ == '__main__':
	Screen(None).run()


