#!/usr/bin/env python3.6

import json
import socket
import binascii as asc
from threading import Thread

import conf

class Connector:
	def __init__(self,mode,host,port):
		self.__socket = None # That's socket
		self.mode = mode
		self.host = host
		self.port = port
		self.threads = []

	#
	# connect to peer
	#
	def connect(self):
		if self.mode == 'client':
			sock = socket.socket()
			sock.connect((self.host,self.port))
			#sock.settimeout(conf.Socket_listen_timeout)
		elif self.mode == 'server':
			sock = socket.socket()
			sock.bind(('',self.port))
			sock.listen(1)
			sock.settimeout(conf.Socket_listen_timeout)
			sock , addr = sock.accept()
			#sock.settimeout(conf.Socket_listen_timeout)
		else:
			raise RuntimeError('Invalid mode')
		self.send_ping(sock)
		if not self.get_ping(sock):
			raise RuntimeError('Handshake missed')
		self.__socket = sock

	#
	# return True if there are opened socket 
	#
	def success(self):
		return self.__socket != None

	def close(self):
		try:
			self.write_msg(conf.CLOSE_MSG)
			self.__socket.close()
			for i in self.threads:
				i.join()
		except:
			pass
		self.__socket = None


	#
	# low-level send msg
	#
	def __send(self,sock,msg):
		if type(msg) == str:
			msg = msg.decode()
		query = asc.b2a_base64(str(len(msg)).encode())[:-1] + b' ' + msg
		print('send: %s'%(query.decode()))
		sock.send(query)

	#
	# low-level recv msg
	#
	def __recv(self,sock):
		query = b''
		q = b''
		while q != b' ':
			q = sock.recv(1)
			query += q
		st = sock.recv(int(asc.a2b_base64(query[:-1]).decode()))
		print('recv: %s'%(query.decode() + st.decode()))
		return st
	#
	# recv ping signal
	# return True if got ping
	# or False
	#
	def get_ping(self,sock):
		return self.__recv(sock) == conf.PING_MSG

	#
	# just send ping signal
	#
	def send_ping(self,sock):
		self.__send(sock,conf.PING_MSG)

	#
	# answer for ping request
	#
	def __answer_ping(self):
		def delay_ping():
			time.sleep(conf.delay_ping)
			self.write_msg(conf.PING_MSG)
		t = Thread(target=lambda x:delay_ping,args=[self.__socket])
		t.start()
		self.threads.append(t)
		i = 0
		while i < len(self.threads):
			if not self.threads[i].is_alive():
				self.threads.pop(i).join()
			else:
				i += 1

	#
	# recv msg from socket
	# return bytes in case of success 
	# or None if socket is closed
	#
	def read_msg(self):
		try:
			msg = self.__recv(self.__socket)
		except Exception as e:
			print('Warning: read from socket: %s'%e)
			msg = b''
			raise SystemError
		if msg == conf.PING_MSG:
			self.__answer_ping()
			return self.read_msg()
		elif msg == conf.CLOSE_MSG:
			self.close()
			return None
		else:
			return msg.decode()

	#
	# send msg into socket
	#
	def write_msg(self,msg):
		if type(msg) == str:
			msg = msg.encode()
		try:
			self.__send(self.__socket,msg)
			return True
		except Exception as e:
			print('Warning: send into socket: %s'%e)
			raise SystemError('tak nado')
			return False

	#
	# send weight's to peer
	#
	def send_weight(self,weights):
		self.write_msg(json.dumps({'weights':weights}))

	#
	# send tanks' coordinates to peer
	#
	def send_tanks(self,left_x,right_x):
		self.write_msg(json.dumps({'left_x':left_x,'right_x':right_x}))		


	#
	# just ping peer
	#
	def ping(self):
		self.send_ping(self.__socket)

if __name__ == '__main__':
	Flag = True
	def loop(conn):
		while Flag:
			print(conn.read_msg())
	import sys
	conn = Connector(sys.argv[1],'127.0.0.1',1234)
	conn.connect()
	from threading import Thread
	t = Thread(target=loop,args=[conn])
	t.start()
	try:
		while Flag:
			conn.write_msg(input('>>'))
	except KeyboardInterrupt:
		pass
	except Exception:
		pass
	Flag = False


