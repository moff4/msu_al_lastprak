#!/usr/bin/env python3.6

import conf

class Basic_Blow:
	def __init__(self,engine,x,y):
		self.engine = engine
		self.__desctription = "Standart Blow"

		self.__X = x
		self.__Y = y
		self.__r = 0
		self.__max_r = int(conf.Blow_max_size/2)
		self.__color = conf.Blow_color
		self.__wave_width = conf.Blow_width

	#########################
	## ENGINE CONTROLL API ##
	#########################
	#
	# return name of this blow
	#
	def get_name(self):
		return self.__desctription
	#
	# return position for this object
	#
	def getXY(self):
		return int(self.__X),int(self.__Y)
	#
	# move missle for next dx,dy
	#
	def next(self,_timer=0):
		self.__r += 1
	#
	# return True if method "next" is over
	# or False
	#
	def done(self):
		return self.__r >= self.__max_r
	#
	# destroy itself and create extra blow or missle objects in case of need
	#
	def reroze(self,_timer=0):
		self.engine.blow_landscape(self.__X,self.__Y,self.__max_r)#self.engine.blow_landscape(self.__X,self.__max_r)
		# damage smbd's tank
		pass # normal

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
			"circle":[
				[0.0,0.0,self.__r,self.__wave_width,self.__color]
			]
		}
		return obj
