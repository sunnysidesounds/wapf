#!/usr/bin/env python

################################################################################
## NAME: VERSION RUN SCRIPT
## DATE: Oct 2011
## AUTHOR: Jason R Alexander
## MAIL: sunnysidesounds@gmail.com
## INFO: This just outputs version information
################################################################################

import sys
import os
import time
sys.path.append( os.path.join( os.getcwd(), '..' ) )
#custom modules
import wapf


if __name__ == '__main__':
	#config importer
	# ---------------------------------------------------------------------------------------------------
	try:
		#get the second argument as this contains the config file
		customConfig = sys.argv[1]
		#strip the .py as we don't need it here
		customConfig = customConfig[:-3].strip()		
		#append new path
		sys.path.append("../configs")
		#import the argument as config. (So you don't have to swap "config." object values 
		exec("import " + customConfig + " as config" )
	except:
		#if not argument import default config
		import config
	# ---------------------------------------------------------------------------------------------------
	wobj = wapf.wapf(config.baseUrl, config.browser)
	print ''
	print wobj.lineset(1)
	print config.wapfVersion
	print ''
	print 'SVN Information available to working copies only:'
	runScript = os.system("svn info")
	print wobj.lineset(1)
	print ''

