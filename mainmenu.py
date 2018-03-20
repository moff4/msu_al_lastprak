#!/usr/bin/env python3.6

import tkinter as tk
from tkinter import messagebox
import conf as cfg
import traceback

from connector import Connector

class MainMenu:
	def __init__(self):
		#self.root = tk.Tk(screenName=cfg.MainMenu_ScreenName)
		self.root = tk.Tk()
		self.root.configure(background=cfg.MainMenu_BackgroundColor)
		self.root.geometry('%sx%s+%s+%s'%(str(cfg.MainMenu_width),str(cfg.MainMenu_height),str(cfg.MainMenu_left),str(cfg.MainMenu_top)))
		
		tk.Label(self.root, text=cfg.MainMenu_logo,bg=cfg.MainMenu_BackgroundColor).place(height=20,width=100,x=80,y=15)

		self.radiobutton_var = tk.IntVar()
		self.radiobutton_var.set(0)
		Radiobutton_1 = tk.Radiobutton(self.root,bg=cfg.MainMenu_BackgroundColor, text=cfg.MainMenu_radio_text_1, variable=self.radiobutton_var,value=0)
		Radiobutton_1.bind("<Button-1>", self.Radiobutton_1_click)
		Radiobutton_1.place(height=20,width=75,x=85,y=70)
		Radiobutton_2 = tk.Radiobutton(self.root,bg=cfg.MainMenu_BackgroundColor, text=cfg.MainMenu_radio_text_2, variable=self.radiobutton_var,value=1)
		Radiobutton_2.bind("<Button-1>", self.Radiobutton_2_click)
		Radiobutton_2.place(height=20,width=75,x=85,y=45)


		self.str_host = tk.StringVar()
		self.str_host.set(str(cfg.Connection_default_host))
		self.str_port = tk.StringVar()
		self.str_port.set(str(cfg.Connection_default_port))

		self.host_label = tk.Label(self.root, text=cfg.Label_host_name, bg=cfg.MainMenu_BackgroundColor)
		self.host_label.place(height=20,width=100,x=15,y=100)
		tk.Label(self.root, text=cfg.Label_port_name, bg=cfg.MainMenu_BackgroundColor).place(height=20,width=100,x=15,y=130)
		self.host_entry = tk.Entry(self.root, textvariable=self.str_host)
		self.host_entry.place(height=20,width=100,x=85,y=100)
		tk.Entry(self.root, textvariable=self.str_port).place(height=20,width=100,x=85,y=130)
		
		start_button = tk.Button(self.root,text=cfg.Start_button_name,fg=cfg.MainMenu_BackgroundColor)
		start_button.bind("<Button-1>", self.start_button_click)
		start_button.place(height=21,width=120,x=70,y=160)
		exit_button = tk.Button(self.root,text=cfg.Exit_button_name,fg=cfg.MainMenu_BackgroundColor)
		exit_button.bind("<Button-1>", self.exit_button_click)
		exit_button.place(height=21,width=120,x=70,y=190)

		self.Radiobutton_1_click(None) # click on radio button
		self.__result = None , None

	#
	# return the result
	#
	def get_result(self):
		return self.__result

	#
	# client radiobutton enabled
	#
	def Radiobutton_1_click(self,x):
		self.host_entry.config(state=tk.NORMAL)
		#self.host_label.config(foreground=cfg.MainMenu_BackgroundColor)

	#
	# server radiobutton enabled
	#
	def Radiobutton_2_click(self,x):
		self.host_entry.config(state=tk.DISABLED)
		#self.host_label.config(foreground='#000000')

	#
	# start button pressed
	#
	def start_button_click(self,x):
		err_msg = ''
		if self.radiobutton_var.get() == 1:
			mode = 'server'
			host = 'null'
		else:
			mode = 'client'
			host = self.str_host.get()
		
		port = self.str_port.get()
		try:
			err_msg = 'Port value should be integer'
			port = int(port)
			err_msg = ''
			if not (0 < port < 10000):
				err_msg = 'Invalid port value'
			elif (len(host)<=0):
				err_msg = 'Invalid host value'
			
			if len(err_msg) > 0:
				raise Runtime('Loh')
		except Exception as e:
			messagebox.showerror('Error','%s'%err_msg)
			return
		try:
			conn = Connector(mode=mode,host=host,port=port)
			conn.connect()
			if not conn.success():
				if mode == 'client':
					err_msg = 'Cannot connect to %s:%s'%(host,port)
				else:
					err_msg = 'No connections to port %s'%(port)
				messagebox.showerror('Error','%s'%err_msg)
			else:
				self.__result = conn , mode
				self.root.quit()
		except Exception as e:
			#e = traceback.format_exc()
			messagebox.showerror('Smth happened','%s'%e)

	#
	# exit button pressed
	#
	def exit_button_click(self,x):
		self.__result = None
		raise SystemExit
		#self.root.destroy()

	#
	# run GUI
	#
	def run(self):
		try:
			self.root.mainloop()
		except SystemExit:
			pass
