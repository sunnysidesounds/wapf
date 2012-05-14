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

	# Get file contents
	fd = open('../readme.txt')
	contents = fd.readlines()
	fd.close()
	
	new_contents = []
	
	# Get rid of empty lines
	for line in contents:
	    # Strip whitespace, should leave nothing if empty line was just "\n"
	    if not line.strip():
	        continue
	    # We got something, save it
	    else:
	        line = line.replace("*", " ", 3)
	        line = line.replace("<version>", config.wapfVersion, 3)
	        line = line.replace("NOTE: THIS FILE IS PARSED BY THE FRAMEWORK. FOR BETTER READABILITY RUN 'help'", " ", 3)
	        new_contents.append(line)
	
	# Print file sans empty lines
	print "".join(new_contents)


