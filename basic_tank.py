#!/usr/bin/env python3.6
import math
import time

import conf
from basic_missile import Basic_Missile
from firecracker_missile import Firecracker_Missile
from firecracker_missile2 import Firecracker_Missile2
from shotgun_missile import Shotgun_Missile

class Basic_Tank:
	def __init__(self,engine,x,y,power=50,angle=None,weapons=[Basic_Missile,Firecracker_Missile,Shotgun_Missile]):
		self.engine = engine
		self.__X = x
		self.__Y = y
		print('TANK-INIT: x = %s ; y = %s'%(x,y))
		if angle == None:
			self.__angle = -math.pi/4.0
		else:
			self.__angle = angle
			
		self.__power = power # min , max == 0, 100
		self.__MAX_POWER = 100.0
		self.__MAX_ANGLE = 2 * math.pi
		self.__weapons = weapons
		self.__weapon_counter = 0
		self.move_counter = 0
		self.max_step = conf.Basic_tank_max_step

		
		self.color = conf.Basic_tank_color # color of tank
		self.s = conf.Basic_tank_size / 2.0 # half of size in pixels
		self.ss = self.s ** 2
		self.cos_30 = int(math.cos(math.pi/6.0) * self.s)
		self.sin_30 = int(math.sin(math.pi/6.0) * self.s)

		self.__min = self.s + 1
		self.__max = conf.Game_window_width - self.__min

		self.rad = math.pi / 180.0
		self.last_presses = [['nothing',0.0],['nothing',0.0]]

	#
	# return weight if same button was pressed several times at once
	#
	def same_press(self,task):
		if ((self.last_presses[0][0] == task) and (time.time() < (self.last_presses[0][1]+0.35))) and ((self.last_presses[1][0] == task) and (time.time() < (self.last_presses[1][1]+0.35))):
			w = 3
		else:
			w = 1
		self.last_presses.pop(0)
		self.last_presses.append([task,time.time()])
		return w


	#########################
	## ENGINE CONTROLL API ##
	#########################

	#
	# return current weapon name
	#
	def get_current_weapon_name(self):
		return self.__weapons[ self.__weapon_counter ](engine=self.engine,power=self.__power,angle=self.__angle,x=self.__X,y=self.engine.get_pixel(self.__X)).get_name()

	#
	# return current tank's power
	#
	def get_power(self):
		return self.__power
	#
	# returns True if current tank is near point(X,Y)
	#
	def near(self,X,Y):
		return ((self.__X - X) ** 2 + (self.__Y - Y) ** 2) <= self.ss
	#
	# return current tank's angle
	#
	def get_angle(self):
		return self.__angle

	#
	# move changes X according to move_counter
	# return new X
	#
	def move(self):
		self.__X += self.move_counter
		self.move_counter = 0
		if self.__X < self.__min:
			self.__X = self.__min
		elif self.__X > self.__max :
			self.__X = self.__max
		return self.__X

	#
	# return current position for this obj
	#
	def getXY(self):
		self.__X = int(self.__X)
		self.__Y = self.engine.get_pixel(self.__X)
		return self.__X,self.__Y
		#return int(self.__X),self.engine.get_pixel(self.__X)

	#
	# return dict with info how to draw this object
	# obj = {
	#   "line" : [ [x1,y1,x2,y2,border_width,color] , ... ]
	#	"circle" : [ [x,y,radius,border_width,color] , ... ]
	#	"rectangle": [ [x1,y1,x2,y2,border_width,color] , ... ]
	# }
	#
	def draw(self):
		a = [ 0 , self.s ]
		b = [ self.cos_30 , -self.sin_30 ]
		c = [ -self.cos_30 , -self.sin_30 ]
		dx = int(math.cos(self.__angle) * self.s * 1.5)
		dy = int(math.sin(self.__angle) * self.s * 1.5)
		obj = {
			'line': [
				[ a[0],a[1], b[0],b[1] , 
				  b[0],b[1], c[0],c[1] ,
				  c[0],c[1], a[0],a[1] , 2 , self.color ],
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
			self.move_counter -= self.max_step * self.same_press(task)
		elif  task == 'right':
			self.move_counter += self.max_step * self.same_press(task)

	#
	# changes angle , task ::= add | sub (str)
	#
	def change_angle(self,task):
		if task == 'add':
			self.__angle = (self.__angle + self.rad * self.same_press(task)) % self.__MAX_ANGLE
		elif task == 'sub':
			self.__angle = (self.__angle - self.rad * self.same_press(task)) % self.__MAX_ANGLE
	
	#
	# changes power , task ::= add | sub (str)
	#
	def change_power(self,task):
		if task == 'add' and self.__power < self.__MAX_POWER:
			self.__power += 1 * self.same_press(task)
		elif task == 'sub' and self.__power > 0:
			self.__power -= 1 * self.same_press(task)

	#
	# changes weapon , task ::= next | prev (str)
	#
	def change_weapon(self,task):
		if task == 'next':
			self.__weapon_counter = (self.__weapon_counter + 1) % len(self.__weapons)
		else:
			self.__weapon_counter = (self.__weapon_counter - 1 + len(self.__weapons)) % len(self.__weapons)

	#
	# FIRE!!!!!!!
	#
	def fire(self):
		self.engine.add_missile_or_blow(self.__weapons[self.__weapon_counter%len(self.__weapons)](engine=self.engine,power=self.__power,angle=self.__angle,x=self.__X  + math.cos(self.__angle) * self.s,y=self.engine.get_pixel(self.__X) + math.sin(self.__angle) * self.s))
