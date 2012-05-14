#!/usr/bin/env python

################################################################################
## NAME: PORT SCANNER UTILITY
## DATE: Nov 2011
## AUTHOR: Jason R Alexander
################################################################################

import sys
from socket import *


if __name__ == '__main__':
	try:
		target = sys.argv[1]
	except:	
		target = raw_input('Enter host to scan: ')
	
	targetIP = gethostbyname(target)
	print 'Starting scan on host ', targetIP

	#scan reserved ports
	for i in range(20, 1025):
		s = socket(AF_INET, SOCK_STREAM)

		result = s.connect_ex((targetIP, i))

		if(result == 0) :
			print 'Port %d: OPEN' % (i,)
		s.close()
	print ''


