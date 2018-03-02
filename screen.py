#!/usr/bin/env python3.6

import tkinter as tk

import conf

class Screen:
	def __init__(self,conn):
		self.root = tk.Tk()

	def run():
		self.root.mainloop()



# ----------
def countdown(count):
    # change text in label        
    label['text'] = count

    if count > 0:
        # call countdown again after 1000ms (1s)
        root.after(1000, countdown, count-1)

root = tk.Tk()

label = tk.Label(root)
label.place(x=35, y=15)

# call countdown first time    
countdown(5)
# root.after(0, countdown, 5)
