#!/usr/bin/env python

################################################################################
## NAME: W3C VALIDATOR
## DATE: Oct 2011
## AUTHOR: Jason R Alexander
## MAIL: sunnysidesounds@gmail.com
## INFO: This is a w3c vaildator
################################################################################

import sys
import os
import re
import multiprocessing
import httplib
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

	#create a wapf instance
	wobj = wapf.wapf(config.baseUrl, config.browser)
	
	count = 1
	for configv in config.w3cList:
		wobj.message('', config.w3cFileName)
		wobj.message('[' + str(count) + '] Results for: ' + configv, config.w3cFileName)	
		wobj.message('---------------------------------------------------', config.w3cFileName)
		w3c = wobj.validateUrl(configv, config.w3cFileName)
		count = count + 1

