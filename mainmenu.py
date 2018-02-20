#!/usr/bin/env python3.6

import tkinter as tk
import conf as cfg

class MainMenu:
	def __init__(self):
		self.root = tk.Tk(screenName=cfg.MainMenu_ScreenName)
		self.root.configure(background=cfg.MainMenu_BackgroundColor)
		self.root.geometry('%sx%s+%s+%s'%(str(cfg.MainMenu_width),str(cfg.MainMenu_height),str(cfg.MainMenu_left),str(cfg.MainMenu_top)))
		#
		# 2 chechboxes + 2 textboxes
		#

		#
		# 2 Buttons
		# 
		self.__start_button = tk.Button(self.root,text=cfg.start_button_name,bg=cfg.MainMenu_BackgroundColor)
		self.__start_button.bind("<Button-1>", self.start_button_click)
		self.__start_button.place(height=30,width=75,x=150,y=330)
		self.__exit_button = tk.Button(self.root,text=cfg.exit_button_name,bg=cfg.MainMenu_BackgroundColor)
		self.__exit_button.bind("<Button-1>", self.exit_button_click)
		self.__exit_button.place(height=30,width=75,x=300,y=330)

	def start_button_click(self,x):
		pass

	def exit_button_click(self,x):
		self.root.quit()

	def run(self):
		self.root.mainloop()