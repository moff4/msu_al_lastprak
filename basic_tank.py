#!/usr/bin/env python3.6
import math

import conf
from basic_missile import Basic_Missile

class Basic_Tank:
	def __init__(self,engine,x,y,power=50,angle=None):
		self.engine = engine
		self.__X = x
		self.__Y = y
		if angle = None:
			self.__angle = -math.pi/4.0
		else:
			self.__angle = angle
			
		self.__power = power # min , max == 0, 100
		self.__missile_class = Basic_Missile
		self.move_counter = 0
		self.max_step = conf.Basic_tank_max_step

		self.color = conf.Basic_tank_color # color of tank # FIXME
		self.s = conf.Basic_tank_size / 2.0 # half of size in pixels
		self.cos_30 = int(math.cos(math.pi/6.0) * self.s)
		self.sin_30 = int(math.sin(math.pi/6.0) * self.s)

	#########################
	## ENGINE CONTROLL API ##
	#########################
	#
	# move changes X according to move_counter
	# return new X
	#
	def move(self):
		if self.move_counter > 0:
			self.move_counter -= 1
			self.__X += 1
		elif self.move_counter < 0:
			self.move_counter += 1
			self.__X -= 1
		return self.__X

	#
	# return current position for this obj
	#
	def getXY(self):
		return self.__X,self.__Y

	#
	# return dict with info how to draw this object
	# obj = {
	#   "line" : [ [x1,y1,x2,y2,border_width,color] , ... ]
	#	"circle" : [ [x,y,radius,border_width,color] , ... ]
	#	"rectangle": [ [x1,y1,x2,y2,border_width,color] , ... ]
	# }
	#
	def draw(self):
		a = [ 0 , - self.s ]
		b = [ self.cos_30 , self.sin_30 ]
		c = [ -self.cos_30 , self.sin_30 ]
		dx = int(math.cos(self.__angle) * self.s * 1.5)
		dy = int(math.sin(self.__angle) * self.s * 1.5)
		obj = {
			'lines': [
				[ a[0],a[1], b[0],b[1] , 2 , self.color ],
				[ b[0],b[1], c[0],c[1] , 2 , self.color ],
				[ c[0],c[1], a[0],a[1] , 2 , self.color ],
				[ 0 , 0  ,  dx , dy    , 3 , '#000000']
			]
		}
		return obj

	#######################
	## USER CONTROLL API ##
	#######################
	#
	# save promise to move, task ::= left | right (str)
	#
	def promise_move(self,task):
		if task == 'left':
			self.move_counter -= self.max_step
		elif  task == 'right':
			self.move_counter += self.max_step

	#
	# changes angle , task ::= add | sub (str)
	#
	def change_angle(self,task):
		pass # FIXME
	
	#
	# changes power , task ::= add | sub (str)
	#
	def change_power(self,task):
		pass # FIXME

	#
	# FIRE!!!!!!!
	#
	def fire(self):
		self.engine.add_missile_or_blow(self.__missile_class(engine=self.engine,power=self.__power,angle=self.__angle,x=self.__X,y=self.__Y))
