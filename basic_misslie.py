#!/usr/bin/env python3.6

import math
from basic_blow import Basic_Blow
import conf

class Basic_Misslie:
	def __init__(self,engine,x,y,power,angle):
		self.engine = engine
		self.speed_weight = conf.Missle_speed_weight
		self.__Vx = power * math.cos(angle) * speed_weight
		self.__Vy = power * math.cos(angle) * speed_weight
		self.__X = x
		self.__Y = y
		self.__blow_class = Basic_Blow

	#########################
	## ENGINE CONTROLL API ##
	#########################
	#
	# return position for this object
	#
	def getXY(self):
		return self.__X,self.__Y
	#
	# move missle for next dx,dy
	#
	def next(self):
		self.__X += self.__Vx / float(conf.fps)
		self.__Y += self.__Vy / float(conf.fps)
		self.__Vy -= conf.G / float(conf.fps)
	#
	# return True if method "next" is over
	# or False
	#
	def done(self):
		if not (0 < self.__X < conf.Game_window_width):
			return True
		elif self.__Y > self.engine.get_pixel(self.__X):
			return True
		else:
			return False
	#
	# destroy itself and create extra blow or missle objects in case of need
	#
	def reroze(self):
		self.engine.add_missle_or_blow(self.__blow_class(engine=self.engine,x=self.__X,y=self.engine.get_pixel(self.__X)))

	#
	# return dict with info how to draw this object
	#
	def draw(self):
		# FIXME
		return {}