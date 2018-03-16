#!/usr/bin/env python3.6

import conf
import random
import math
import numpy as np

from basic_tank import Basic_Tank

from scipy.interpolate import interp1d
from scipy import interpolate

class Engine:
	def __init__(self,canvas,draw_landscape=True):
		self.__canvas = canvas 
		self.Tank = [None,None] # users' tanks # LEFT TANK MUST BE 0 , RIGHT TANK MUST BE 1
		self.SCORE = [None,None]
		self.__missiles_n_blows= [] # missiles and blows
		self.__threads = []	# threads
		self.__internal_timer = 0 # count already drawen frames
		if draw_landscape:
			self.__weights = self.__find_seed()
			self.__pixels = self.__generate(self.__weights)
			self.__draw_landscape()
		self.__ready = 0

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
		"""
		dx	=	800
		dy	=	[ 30 ,   50,    50,    40,    2  ]
		w	=	[ 0.029, 0.016 ,0.005, 0.013, 0.25]
		az = []
		for i in range(len(w)):
			az.append([w[i],dy[i]*random.random(),dx*random.random()])
		return az
		"""
		# TIMUR
		weights = [math.trunc(np.random.uniform()*conf.Game_window_height) for i in range(0,conf.Game_window_width,conf.Game_window_width//conf.POLYNOMIAL_DEGREE)]
		return weights
#		weights = [math.trunc(random.random()*conf.Game_window_height) for i in range(0,conf.Game_window_width,conf.Game_window_width//conf.POLYNOMIAL_DEGREE)]
		#return weights + [weights[0]]

	#
	# return pixels
	#
	def __generate(self,weights):
		# ANDREY
		"""
		pix = []
		min_y = 50
		for i in range(conf.Game_window_width):
			x = 0.0
			for j in weights:
				x += j[1] + j[1] * math.sin(j[0] * (i + j[2]))
			pix.append(min_y + int(x))
		return pix
		"""
		# TIMUR
		grid = [i for i in range(0,conf.Game_window_width,conf.Game_window_width//conf.POLYNOMIAL_DEGREE)]
		if (max(grid) != conf.Game_window_width):
			grid[-1] = conf.Game_window_width
	#	print(grid, len(grid))
	#	print(weights, len(weights))
		f = interp1d(grid,weights,kind='cubic')
		pixels = [f(x) for x in range(max(grid))]
	#	print(pixels)
		fmin = min(pixels)
		fmax = max(pixels)
		return list(map(lambda x: 50 + math.trunc(conf.Game_window_height / conf.COMPRESSION_RATIO * (x-fmin)/(fmax-fmin)), pixels))
		
		
		"""
		f = np.poly1d(np.polyfit(range(0,conf.Game_window_width+1,conf.Game_window_width//conf.POLYNOMIAL_DEGREE),weights,conf.POLYNOMIAL_DEGREE))
		pixels = [f(x) for x in range(conf.Game_window_width)]
		fmin = min(pixels)
		fmax = max(pixels)
		return list(map(lambda x: math.trunc(conf.Game_window_height / conf.COMPRESSION_RATIO * (x-fmin)/(fmax-fmin)), pixels))
		"""
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
		Y = self.__pixels[X]
		for i in range(X-R, X+R):
			origin = self.__pixels[i]
			circle = math.sqrt(pow(R,2)-pow((i-X),2))
			self.__pixels[i]=int(max(0,min(origin,Y-circle)+max(0,origin-Y-circle)))
			
	#
	# print on canvas, that game is over and smbd won or game is over
	#
	def print_end(self):
		"""TODO: 
		      вынести константы в conf.py
		      научить эту процедуру определять какое сообщение нужно печатать
		      вынести score и aiming в отдельную процедуру
		"""
		#win or lose
		self.__canvas.create_text(conf.Game_window_width / 2,conf.Game_window_height / 10,fill="green",font="Times 50 italic bold",text="You win")
		#self.__canvas.create_text(conf.Game_window_width / 2,conf.Game_window_height / 10,fill="red",font="Times 50 italic bold",text="You lose")
		
		# score
		self.__canvas.create_text(conf.Game_window_width / 10,conf.Game_window_height / 10,fill="blue",font="Arial 15 italic bold",text="1000")
		self.__canvas.create_text(conf.Game_window_width / 10 * 9,conf.Game_window_height / 10,fill="blue",font="Arial 15 italic bold",text=" 999")
		#aiming
		self.__canvas.create_text(conf.Game_window_width / 10,conf.Game_window_height / 20,fill="blue",font="Arial 15 italic bold",text="45° | 100%")
		
	#
	# return False if any user got score >= max score
	#
	def check_game(self):
		return True # FIXME

	#
	# delete all objects from canvas
	#
	def clean(self):
		for i in self.__canvas.find_all(): # old but tested
			self.__canvas.delete(i)

	#
	# just return weights and nothing else
	#
	def get_weights(self):
		return self.__weights

	#
	# just set new weights and nothing else
	#
	def set_weights(self,weights):
		self.__weights = weights
		self.__pixels = self.__generate(self.__weights)
		self.__ready += 1
	#
	# get dict with info how to draw obj
	# and it's current position
	# and draw it
	# UPD: obj = {
	#   "line" : [ [x1,y1,x2,y2,border_width,color] , ... ]
	#	"circle" : [ [x,y,radius,border_width,color] , ... ]
	#	"rectangle": [ [x1,y1,x2,y2,border_width,color] , ... ]
	# }*
	# DONT FORGET TO CHECK IF KEY IN DICT
	#
	def __draw_obj(self,obj,X,Y):
		if 'line' in obj:		
			for l in obj.pop('line'):
				self.canvas.create_line(l[0] + X,l[1] + Y,l[2] + X,l[3] + Y,width = l[4],fill =l[5])
		if 'circle' in obj:	
			for l in obj.pop('circle'):
				self.canvas.create_oval(l[0]-l[2] + X,l[1]-l[2] + Y,l[0]+l[2] + X,l[1]+l[2] + Y,width = l[3],fill =l[4])
		if 'rectangle' in obj:	
			for l in obj.pop('rectangle'):
				self.canvas.create_rectangle(l[0] + X,l[1] + Y,l[2] + X,l[3] + Y,width = l[4],fill =l[5])

	#
	# single draw
	#
	def single_draw(self):
		for tank in self.Tank:
			tank.move() # that's all

		i = 0
		while i < len(self.__missiles_n_blows): # each of them missile or blow
			self.__missiles_n_blows[i].next(self.__internal_timer)
			if self.__missiles_n_blows[i].done():
				self.__missiles_n_blows[i].reroze(self.__internal_timer)
				self.__missiles_n_blows.pop(i)
			else:
				i+=1

		for i in (self.Tank + self.__missiles_n_blows):
			obj = i.draw(),
			x,y = i.getXY()
			self.__draw_obj(obj,x,y)
		self.__internal_timer += 1

	#
	# return landscape Y for current x
	#
	def get_pixel(self,x):
		try:
			return self.__pixels[x]
		except:
			return None

	#
	# return True if engine is ready for game
	#
	def is_ready(self):
		return self.__ready == 2

	#
	# add new missile or blow
	#
	def add_missile_or_blow(self,obj):
		self.__missiles_n_blows.append(obj)
		
	#
	# add's new tank
	#
	def add_tank(self,tank,pos):
		i = int(pos != 'left')
		self.Tank[i] 	= tank
		self.SCORE[i]	= 0.0

	#
	# place tanks
	#
	def place_tanks(self,x1=None,x2=None):
		if x1 == None and x2 == None:
			z = (float(conf.Game_window_width) / 4.0)
			x1 = z + (random.random() * z - z/2.0)
			x2 = z - (random.random() * z - z/2.0)
		tank1 = Basic_Tank(self,x1,self.get_pixel(x1),angle=conf.Pi/4)
		tank2 = Basic_Tank(self,x2,self.get_pixel(x2),angle=3*conf.Pi/4)
		self.add_tank(tank1,"left")
		self.add_tank(tank2,"right")
		self.__ready += 1
		return x1,x2
