#!/usr/bin/env python3.6

from basic_blow import Basic_Blow
import firecracker_missile

import math
import conf

class Firecracker_Blow(Basic_Blow):
	def __init__(self,engine,x,y):
		super().__init__(engine,x,y)
		setattr(self, '_Basic_Blow__desctription', "Firecracker Blow")
		#
		# FIXME 
		# const must be in conf.py
		#
		parts = 10
		for i in range(parts):
			engine.add_missile_or_blow(firecracker_missile.Firecracker_Missile2(engine,x,y,10,i * math.pi / parts))