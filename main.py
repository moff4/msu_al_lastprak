#!/usr/bin/env python3.6

import sys
from mainmenu import MainMenu
from screen import Screen

HELP_MSG = '''
                          +---------------+                                   .
                          |   T A N K S   |
                          +---------------+

    Flags:
       -h | --help         - See this msg again

    src: https://github.com/moff4/msu_al_lastprak
'''

def main(args):
	conn = 1
	MM = MainMenu()
	while conn != None:
		MM.run()
		conn , mode = MM.get_result()
		if conn != None:
			print('---%s---'%mode)
			sc = Screen(conn,mode == 'server') # conn - connector.Connector()
			sc.run()

	#
	# to be continued ...
	#


if __name__ == '__main__':
	if ('-h' in sys.argv) or ('--help' in sys.argv):
		print(HELP_MSG)
	else:
		main(sys.argv)
