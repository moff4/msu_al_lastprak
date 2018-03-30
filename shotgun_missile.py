#!/usr/bin/env python3.6

from basic_missile import Basic_Missile
from shotgun_blow import Shotgun_Blow

import conf
import math

def SetObject(self, desctription):
	setattr(self, '_Basic_Missile__desctription', desctription)
	setattr(self, '_Basic_Missile__main_color', "purple")
	setattr(self, '_Basic_Missile__blow_class', Shotgun_Blow)	
	setattr(self, '_Basic_Missile__size', 2)
	self.speed_weight = 5 * conf.Missile_speed_weight
	
class Shotgun_Missile(Basic_Missile):
	def __init__(self,engine,x,y,power,angle):			
		self.__flag = 0
		parts = 5
		delta = math.pi / 60
		self.__pellet = []
		for i in range(-parts,parts+1):
			if i != 0:
				self.__pellet.append(Shotgun_Missile2(engine,x,y,power,angle + delta * i))
		super().__init__(engine,x,y,power,angle)
		SetObject(self, 'Shotgun')
	def next(self,_timer=0):
		super().next(_timer)
		if self.__flag == 0:
			self.__flag == 1
			while self.__pellet:
				self.engine.add_missile_or_blow(self.__pellet.pop())

class Shotgun_Missile2(Basic_Missile):
	def __init__(self,engine,x,y,power,angle):
		super().__init__(engine,x,y,power,angle)
		SetObject(self, 'Shotgun2')
