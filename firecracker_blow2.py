#!/usr/bin/env python3.6

from basic_blow import Basic_Blow

import math
import conf

class Firecracker_Blow2(Basic_Blow):
	def __init__(self,engine,x,y):
		super().__init__(engine,x,y)
		setattr(self, '_Basic_Blow__desctription', "Firecracker Blow2")
		setattr(self, '_Basic_Blow__max_r', int(conf.Blow_max_size/3))
