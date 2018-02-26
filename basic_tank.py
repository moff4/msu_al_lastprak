#!/usr/bin/env python3.6

import conf
from basic_missle import Basic_Missle

class Basic_Tank:
	def __init__(self,engine,x,y,power,angle):
		self.engine = engine
		self.__X = x
		self.__Y = y
		self.__angle = angle
		self.__power = power # min , max == 0, 100
		self.__missle_class = Basic_Missle
		self.move_counter = 0
		self.max_step = conf.Basic_tank_max_step

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
	#
	def draw(self):
		# FIXME
		return {}

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
		self.engine.add_missle_or_blow(self.__missle_class(engine=self.engine,power=self.__power,angle=self.__angle,x=self.__X,y=self.__Y))
