#!/usr/bin/env python

################################################################################
## NAME: HELP FILE
## DATE: Nov 2011
## AUTHOR: Jason R Alexander
## MAIL: sunnysidesounds@gmail.com
## INFO: This is the help/readme file
################################################################################

#TODO: Make this more dynamic and make it so the readme and terminal views are them same without using line replace

import sys
import os
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

	print 'Most up-to-date help documentation is located at: ' + str(config.readmeDoc) + '\n'
	openBrowser = raw_input('Are you running this framework in headless mode?(Y/N) ')
	print '\n'
	if(openBrowser == 'Y' or openBrowser == 'y'):
		print 'Please go to ' + str(config.readmeDoc) + ' for the most up-to-date help documentation '
		print '\n'
	else:
		print 'Opening help documentation in new browser window! \n'
		wobj = wapf.wapf(config.baseUrl, config.browser)
		browser = wobj.setBrowser(config.browser)
		browser.get(config.readmeDoc)
		