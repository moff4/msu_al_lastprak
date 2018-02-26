#!/usr/bin/env python3.6

import conf

class Basic_Blow:
	def __init__(self,engine,x,y):
		self.engine = engine
		self.__X = x
		self.__Y = y

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
		pass # FIXME
	#
	# return True if method "next" is over
	# or False
	#
	def done(self):
		pass # FIXME
	#
	# destroy itself and create extra blow or missle objects in case of need
	#
	def reroze(self):
		pass # normal

	#
	# return dict with info how to draw this object
	#
	def draw(self):
		# FIXME
		return {}