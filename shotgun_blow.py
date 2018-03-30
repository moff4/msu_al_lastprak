#!/usr/bin/env python3.6

from basic_blow import Basic_Blow
#import shotgun_missile

import math
import conf

class Shotgun_Blow(Basic_Blow):
	def __init__(self,engine,x,y):
		super().__init__(engine,x,y)
		setattr(self, '_Basic_Blow__desctription', "Shotgun Blow")		
		setattr(self, '_Basic_Blow__max_r', int(conf.Blow_max_size/10))
		setattr(self, '_Basic_Blow__wave_width', int(conf.Blow_width))
