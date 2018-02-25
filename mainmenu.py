#!/usr/bin/env python3.6

import tkinter as tk
import conf as cfg

class MainMenu:
	def __init__(self):
		self.root = tk.Tk(screenName=cfg.MainMenu_ScreenName)
		self.root.configure(background=cfg.MainMenu_BackgroundColor)
		self.root.geometry('%sx%s+%s+%s'%(str(cfg.MainMenu_width),str(cfg.MainMenu_height),str(cfg.MainMenu_left),str(cfg.MainMenu_top)))
		
		#
		# Need to choose font   FIXME
		#
		tk.Label(self.root, text=cfg.MainMenu_logo,bg=cfg.MainMenu_BackgroundColor).place(height=20,width=100,x=80,y=15)

		self.radiobutton_var = tk.IntVar()
		
		Radiobutton_1 = tk.Radiobutton(self.root,bg=cfg.MainMenu_BackgroundColor, text=cfg.MainMenu_radio_text_1, variable=self.radiobutton_var,value=0)
		Radiobutton_1.place(height=20,width=75,x=85,y=45)
		Radiobutton_2 = tk.Radiobutton(self.root,bg=cfg.MainMenu_BackgroundColor, text=cfg.MainMenu_radio_text_2, variable=self.radiobutton_var,value=1)
		Radiobutton_2.place(height=20,width=75,x=85,y=70)

		self.str_host = tk.StringVar()
		self.str_host.set(str(cfg.Connection_default_host))
		self.str_port = tk.StringVar()
		self.str_port.set(str(cfg.Connection_default_port))

		tk.Label(self.root, text=cfg.Label_host_name, bg=cfg.MainMenu_BackgroundColor).place(height=20,width=100,x=15,y=100)
		tk.Label(self.root, text=cfg.Label_port_name, bg=cfg.MainMenu_BackgroundColor).place(height=20,width=100,x=15,y=130)
		tk.Entry(self.root, textvariable=self.str_host).place(height=20,width=100,x=85,y=100)
		tk.Entry(self.root, textvariable=self.str_port).place(height=20,width=100,x=85,y=130)
		
		start_button = tk.Button(self.root,text=cfg.Start_button_name,fg=cfg.MainMenu_BackgroundColor)
		start_button.bind("<Button-1>", self.start_button_click)
		start_button.place(height=21,width=120,x=70,y=160)
		exit_button = tk.Button(self.root,text=cfg.Exit_button_name,fg=cfg.MainMenu_BackgroundColor)
		exit_button.bind("<Button-1>", self.exit_button_click)
		exit_button.place(height=21,width=120,x=70,y=190)

	def start_button_click(self,x):
		pass

	def exit_button_click(self,x):
		self.root.quit()

	def run(self):
		self.root.mainloop()