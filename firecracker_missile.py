#!/usr/bin/env python3.6

from basic_missile import Basic_Missile
import firecracker_blow
import conf

class Firecracker_Missile(Basic_Missile):
	def __init__(self,engine,x,y,power,angle):
		super().__init__(engine,x,y,power,angle)
		setattr(self, '_Basic_Missile__desctription', conf.Firecracker_desctription)
		setattr(self, '_Basic_Missile__main_color', conf.Firecracker_main_color)
		setattr(self, '_Basic_Missile__blow_class', firecracker_blow.Firecracker_Blow)
