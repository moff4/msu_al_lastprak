#!/usr/bin/env python3.6

import conf
import random
import math
import numpy as np

class Engine:
	def __init__(self,canvas):
		self.__canvas = canvas 
		self.__Tank = [] # users' tanks
		self.__missles_n_blows= [] # missles and blows
		self.__threads = []	# threads
		self.__weights = self.__find_seed()
		self.__pixels = self.__generate(self.__weights)

	#
	# return weights
	#
	def __find_seed(self):
		weights = [math.trunc(random.random()*conf.Game_window_height) for i in range(0,conf.Game_window_width,conf.Game_window_width//conf.POLYNOMIAL_DEGREE)]
		return weights + [weights[0]]

	#
	# return pixels
	#
	def __generate(self,weights):
		f = np.poly1d(np.polyfit(range(0,conf.Game_window_width+1,conf.Game_window_width//conf.POLYNOMIAL_DEGREE),weights,conf.POLYNOMIAL_DEGREE))
		pixels = [f(x) for x in range(conf.Game_window_width)]
		fmin = min(pixels)
		fmax = max(pixels)
		return list(map(lambda x: math.trunc(conf.Game_window_height / conf.COMPRESSION_RATIO * (x-fmin)/(fmax-fmin)), pixels))

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
		while i < len(self.__missles_n_blows): # each of them missle or blow
			self.__missles_n_blows[i].next()
			if self.__missles_n_blows[i].done():
				self.__missles_n_blows[i].reroze()
				self.__missles_n_blows.pop(i)
			else:
				i+=1

		for i in (self.__Tanks + self.__missles_n_blows):
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
	# add new missle or blow
	#
	def add_missle_or_blow(self,obj):
		self.__missles_n_blows.append(obj)
		
		
