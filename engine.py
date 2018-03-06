#!/usr/bin/env python3.6

import conf
import random
import math
import numpy as np

class Engine:
	def __init__(self,canvas):
		self.__canvas = canvas 
		self.__Tank = [] # users' tanks
		self.__missiles_n_blows= [] # missiles and blows
		self.__threads = []	# threads
		self.__weights = self.__find_seed()
		self.__pixels = self.__generate(self.__weights)
		self.__draw_landscape()

	def f(self):
		self.clean()
		self.__weights = self.__find_seed()
		self.__pixels = self.__generate(self.__weights)
		self.__draw_landscape()

	#
	# return weights
	#
	def __find_seed(self):
		# ANDREY
		dx	=	800
		dy	=	[ 30 ,   50,    50,    40,    2  ]
		w	=	[ 0.029, 0.016 ,0.005, 0.013, 0.25]
		az = []
		for i in range(len(w)):
			az.append([w[i],dy[i]*random.random(),dx*random.random()])
		return az

		# TIMUR
		weights = [math.trunc(random.random()*conf.Game_window_height) for i in range(0,conf.Game_window_width,conf.Game_window_width//conf.POLYNOMIAL_DEGREE)]
		return weights + [weights[0]]

	#
	# return pixels
	#
	def __generate(self,weights):
		# ANDREY
		pix = []
		min_y = 50
		for i in range(conf.Game_window_width):
			x = 0.0
			for j in weights:
				x += j[1] + j[1] * math.sin(j[0] * (i + j[2]))
			pix.append(min_y + int(x))
		return pix

		# TIMUR
		f = np.poly1d(np.polyfit(range(0,conf.Game_window_width+1,conf.Game_window_width//conf.POLYNOMIAL_DEGREE),weights,conf.POLYNOMIAL_DEGREE))
		pixels = [f(x) for x in range(conf.Game_window_width)]
		fmin = min(pixels)
		fmax = max(pixels)
		return list(map(lambda x: math.trunc(conf.Game_window_height / conf.COMPRESSION_RATIO * (x-fmin)/(fmax-fmin)), pixels))

	#
	# just draw landscape and nothing more
	#
	def __draw_landscape(self):
		for i in range(len(self.__pixels)-1):
			self.__canvas.create_line(i,conf.Game_window_height-self.__pixels[i],i+1,conf.Game_window_height-self.__pixels[i+1])#,fill='green')
	
	
	#
	# u know X, u can get Y
	# u should create explosion funnel in (X,Y) with radius R
	#
	def blow_landscape(self,X,R):
		pass # FIXME
	
	#
	# delete all objects from canvas
	#
	def clean(self):
		map(self.__canvas.delete,self.__canvas.find_all()) # new ; maybe faster
		
		# for i in self.__canvas.find_all(): # old but tested
		# 	self.__canvas.delete(i)

	#
	# just return weights and nothing else
	#
	def get_weights(self):
		return self.__weights

	#
	# get dict with info how to draw obj
	# and it's current position
	# and draw it
	# UPD: obj = {
	#   "line" : [ [x1,y1,x2,y2,border_width,color] , ... ]
	#	"circle" : [ [x,y,radius,border_width,color] , ... ]
	#	"rectangle": [ [x1,y1,x2,y2,border_width,color] , ... ]
	# }
	# DONT FORGET TO CHECK IF KEY IN DICT
	#
	def __draw_obj(self,obj,X,Y):
		pass # FIXME

	#
	# single draw
	#
	def single_draw(self):
		for tank in self.__Tanks:
			tank.move() # ???? is that's all # UPD that's all

		i = 0
		while i < len(self.__missiles_n_blows): # each of them missile or blow
			self.__missiles_n_blows[i].next()
			if self.__missiles_n_blows[i].done():
				self.__missiles_n_blows[i].reroze()
				self.__missiles_n_blows.pop(i)
			else:
				i+=1

		for i in (self.__Tanks + self.__missiles_n_blows):
			obj = i.draw(),
			x,y = i.getXY()
			self.__draw_obj(obj,x,y)

	#
	# return landscape Y for current x
	#
	def get_pixel(self,x):
		try:
			return self.__pixels[x]
		except:
			return None

	#
	# add new missile or blow
	#
	def add_missile_or_blow(self,obj):
		self.__missiles_n_blows.append(obj)
		
		
