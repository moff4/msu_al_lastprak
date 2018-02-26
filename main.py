#!/usr/bin/env python3.6

import sys
import mainmenu

HELP_MSG = '''
                          +---------------+                                   .
                          |   T A N K S   |
                          +---------------+

    Flags:
       -h | --help         - See this msg again

    src: https://github.com/moff4/msu_al_lastprak
'''

def main(args):
	MM = mainmenu.MainMenu()
	MM.run()
	conn = MM.get_result()
	# conn - connector.Connector()
	#
	# to be continued ...
	#


if __name__ == '__main__':
	if ('-h' in sys.argv) or ('--help' in sys.argv):
		print(HELP_MSG)
	else:
		main(sys.argv)