#!/usr/bin/env python3.6

class Engine:
	def __init__(self):
		self.__PAUSED = True
		self.__Tanks	= [] # users' tanks
		self.__missles_n_blows= [] # missles and blows
		self.__threads = []	# threads
		self.__weights = self.find_seed()
		self.__pixels = self.generate(weights)

	#
	# return weights
	#
	def __find_seed(self):
		pass

	#
	# return pixels
	#
	def __generate(self,weights):
		pass

	#
	# get dict with info how to draw obj
	# and it's current position
	# and draw it
	#
	def __draw_obj(self,obj,X,Y):
		pass # FIXME

	#
	# single draw
	#
	def __single_draw(self):
		for tank in self.__Tanks:
			tanks.move() # ???? is that's all

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
	#
	# main loop for render engine
	#
	def mainloop(self):
		delay = 1.0/conf.fps
		self.__PAUSED = False
		while not self.__PAUSED:
			t = Thread(target=self.__single_draw)
			t.start()
			self.__threads.append(t)
			i = 0
			while i < len(self.__threads):
				if not self.__threads[i].is_alive():
					self.__threads.pop(i).join()
				else:
					i += 1
			time.sleep(delay)