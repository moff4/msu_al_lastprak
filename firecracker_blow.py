#!/usr/bin/env python3.6

from basic_blow import Basic_Blow
#from basic_missile import Basic_Missile ##
#from firecracker_missile import Firecracker_Missile2
import firecracker_missile

import math
import conf

class Firecracker_Blow(Basic_Blow):
	def __init__(self,engine,x,y):
		super().__init__(engine,x,y)
		setattr(self, '_Basic_Blow__desctription', "Firecracker Blow")
		parts = 10
		for i in range(parts):
			BM = firecracker_missile.Firecracker_Missile2(engine,x,y,10,i * math.pi / parts)
			engine.add_missile_or_blow(BM)

class Firecracker_Blow2(Basic_Blow):
	def __init__(self,engine,x,y):
		super().__init__(engine,x,y)
		setattr(self, '_Basic_Blow__desctription', "Firecracker Blow2")
		setattr(self, '_Basic_Blow__max_r', int(conf.Blow_max_size/3))
