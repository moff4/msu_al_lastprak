#!/usr/bin/env python3.6

from basic_blow import Basic_Blow
import firecracker_missile2

import math
import conf

class Firecracker_Blow(Basic_Blow):
	def __init__(self,engine,x,y):
		super().__init__(engine,x,y)
		setattr(self, '_Basic_Blow__desctription', conf.FirecrackerBlow_desctription)
		for i in range(parts):
			engine.add_missile_or_blow(firecracker_missile2.Firecracker_Missile2(engine,x,y,conf.FirecrackerBlow_SplinterSpeed,i * math.pi / conf.FirecrackerBlow_SplinterAmount))
