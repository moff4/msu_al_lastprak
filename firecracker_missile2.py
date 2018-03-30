#!/usr/bin/env python3.6

from basic_missile import Basic_Missile
import firecracker_blow2
import conf

class Firecracker_Missile2(Basic_Missile):
	def __init__(self,engine,x,y,power,angle):
		super().__init__(engine,x,y,power,angle)
		setattr(self, '_Basic_Missile__main_color', conf.Firecracker2_main_color)
		setattr(self, '_Basic_Missile__size', conf.Firecracker2_Misslie_size)
		setattr(self, '_Basic_Missile__blow_class', firecracker_blow2.Firecracker_Blow2)
		self.speed_weight = conf.Firecracker2_Missile_speed_weight
