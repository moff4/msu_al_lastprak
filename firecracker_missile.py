#!/usr/bin/env python3.6

from basic_missile import Basic_Missile
from basic_blow import Basic_Blow

class Firecracker_Missile(Basic_Missile):
	def __init__(self,engine,x,y,power,angle):
		super().__init__(engine,x,y,power,angle)
		setattr(self, '_Basic_Missile__desctription', "Firecracker")
