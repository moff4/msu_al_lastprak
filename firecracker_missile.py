#!/usr/bin/env python3.6

from basic_missile import Basic_Missile
import firecracker_blow
import conf

class Firecracker_Missile(Basic_Missile):
	def __init__(self,engine,x,y,power,angle):
		super().__init__(engine,x,y,power,angle)
		#
		# FIXME 
		# const must be in conf.py
		#
		setattr(self, '_Basic_Missile__desctription', "Firecracker")
		setattr(self, '_Basic_Missile__main_color', "yellow")
		setattr(self, '_Basic_Missile__blow_class', firecracker_blow.Firecracker_Blow)

