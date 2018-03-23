#!/usr/bin/env python3.6

import math
from basic_blow import Basic_Blow
import conf

class Basic_Missile:
	def __init__(self,engine,x,y,power,angle):
		self.engine = engine
		self.speed_weight = conf.Missile_speed_weight
		self.__Vx = power * math.cos(angle)
		self.__Vy = power * math.cos(angle)
		self.__X = x
		self.__Y = y
		self.__blow_class = Basic_Blow
		
		self.__size = int(conf.Misslie_size / 2)
		self.__traceback = []
		self.__traceback_length = conf.Missile_trace_length
		self.__main_color =  conf.Misslie_main_color
		self.__trace_color = conf.Misslie_trace_color

		self.__done = False


	#########################
	## ENGINE CONTROLL API ##
	#########################
	#
	# return position for this object
	#
	def getXY(self):
		return int(self.__X),int(self.__Y)
	#
	# move missle for next dx,dy
	#
	def next(self,_timer=0):
		if len(self.__traceback) >= self.__traceback_length:
			self.__traceback[:(self.__traceback_length - 1)]
		self.__traceback = [[self.__X,self.__Y]] + self.__traceback
		dx = (self.__Vx / float(conf.fps)) * self.speed_weight * 10
		dy = (self.__Vy / float(conf.fps)) * self.speed_weight / dx
		for i in range(int(dx)):
			self.__X += 0.1
			self.__Y += dy
			if self.done():
				self.__done = True
				return
		self.__X = int(self.__X)
		self.__Y = int(self.__Y)
		self.__Vy -= conf.G / float(conf.fps)
	#
	# return True if method "next" is over
	# or False
	#
	def done(self):
		if not (0 < self.__X < conf.Game_window_width):
			return True
		elif self.__Y <= self.engine.get_pixel(self.__X):
			return True
		else:
			return self.__done
	#
	# destroy itself and create extra blow or missle objects in case of need
	#
	def reroze(self,_timer=0):
		# experemental
		self.engine.add_missile_or_blow(self.__blow_class(engine=self.engine,x=self.__X,y=self.__Y))
		return
		
		# old and tested 
		y = self.engine.get_pixel(self.__X)
		if y != None:
			self.engine.add_missile_or_blow(self.__blow_class(engine=self.engine,x=self.__X,y=y))

	#
	# return dict with info how to draw this object
	# UPD: obj = {
	#   "line" : [ [x1,y1,x2,y2,border_width,color] , ... ]
	#	"circle" : [ [x,y,radius,border_width,color] , ... ]
	#	"rectangle": [ [x1,y1,x2,y2,border_width,color] , ... ]
	# }
	#
	def draw(self):
		obj = {
			"line":[],
			"circle":[
				[0.0,0.0,self.__size,2,self.__main_color]
			]
		}
		#az = [[self.__X,self.__Y]] + self.__traceback
		# az = self.__traceback
		# for i in range(1,len(az)):
		# 	obj["line"].append([ az[i][0],az[i][1] , az[i][0]-az[i-1][0],az[i][1]-az[i-1][1] , 1, self.__trace_color ])
		return obj
