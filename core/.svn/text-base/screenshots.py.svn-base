#!/usr/bin/env python

################################################################################
## NAME: SCREENSHOTS
## DATE: Nove 2011
## AUTHOR: Jason R Alexander
## MAIL: sunnysidesounds@gmail.com
## INFO: This takes screenshots with firefox
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
	for configv in config.screenshotList:
		#print configv
		browser = wobj.setBrowser(config.browser)
		browser.get(configv)
		uniqueFilename = wobj.getUrlEnding(configv)
		#Let the user know what is happening
		print '[' + str(count) + '] ' + 'Taking screenshot of ' + configv
		wobj.getScreenshot(uniqueFilename, config.screenshotFileName)	
		browser.close()
		count = count + 1

