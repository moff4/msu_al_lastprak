#!/usr/bin/env python3.6

import tkinter as tk
import time

from engine import Engine
import conf

#
# Screen with main picturebox
#
class Screen:
	def __init__(self,conn):
		self.root = tk.Tk(screenName=conf.Screen_ScreenName)
		self.root.configure(background=conf.Screen_BackgroundColor)
		self.root.geometry('%sx%s+%s+%s'%(str(conf.Screen_width),str(conf.Screen_height),str(conf.Screen_left),str(conf.Screen_top)))
		#self.connector = conn # change on controllers
		self.fps_delay = int(1000.0/conf.fps)
		
		self.canvas = tk.Canvas(self.root, width=conf.Game_window_width, height=conf.Game_window_height)
		#self.canvas.pack()
		__cc = int((conf.Screen_width-conf.Game_window_width)/2)
		self.canvas.place(x=__cc,y=__cc)
		
		### EXAMPLES ####
		#self.canvas.create_line(0, 0, 200, 100)
		#self.canvas.create_line(0, 100, 200, 0, fill="red", dash=(4, 4))
		#self.canvas.create_rectangle(50, 25, 150, 75, fill="blue")

		self.engine = Engine(self.canvas)
	#
	#
	#
	def run(self):
		#self.draw_picture() # later must be uncommented
		self.root.mainloop()

	#
	#
	#
	def draw_picture(self):
		self.root.after(self.fps_delay,self.draw_picture)
		self.engine.single_draw() # maybe need new thread ???? test this later FIXME

if __name__ == '__main__':
	Screen(None).run()


