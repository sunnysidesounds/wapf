#!/usr/bin/env python

################################################################################
## NAME: LIST ALL CORE/CUSTOM SCRIPTS
## DATE: Oct 2011
## AUTHOR: Jason R Alexander
## MAIL: sunnysidesounds@gmail.com
## INFO: List all executable core/custom scripts
################################################################################

import sys
import os
import re
import multiprocessing
import httplib
import time
import glob
sys.path.append( os.path.join( os.getcwd(), '..' ) )

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

	
	print config.baseUrl
	
	count_core = 1
	count_custom = 1
	
	print 'List of core scripts:'
	
	dirList=os.listdir("../core")
	for files in dirList:
		extension = os.path.splitext(files)[1]
		if(extension == '.py'):
			print '['+ str(count_core) +'] ' + files
			count_core = count_core + 1
	
	print ''
	print 'List of custom scripts:'
	
	dirList=os.listdir("../custom")
	for files in dirList:
		extension = os.path.splitext(files)[1]
		if(extension == '.py'):
			print '['+ str(count_custom) +'] ' + files
			count_custom = count_custom + 1
	
	
	print ''
