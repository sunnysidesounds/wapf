#!/usr/bin/env python

################################################################################
## NAME: RUN SCRIPT
## DATE: Oct 2011
## AUTHOR: Jason R Alexander
## MAIL: sunnysidesounds@gmail.com
## INFO: This script when executed will run the scripts in the core. Each script a different multi-process
################################################################################

import sys
import os
import re
import multiprocessing
import httplib
import time
import glob
from termcolor import colored
sys.path.append( os.path.join( os.getcwd(), '..' ) )

import wapf
import config

scriptList = []
coreList = []
customList = []
configsList = []
utilitiesList = []
executionList = []
errorList = []

#termcolor color
runColor = 'white'
errorColor = 'red'

#title and words
runTitle = colored('wapf --> Web Analyzing & Profiling Framework [ ' + config.wapfVersion + ' ]', runColor)


# -----------------------------------------------------------------------------------------------------
def executeUtilityScript(script, command, filename = ''):
	"""This just runs scripts in a method """
	if(utilitiesList.count(script)):
		os.chdir("./utilities")	
		
		if(filename == ''):
			exec_command = "python ../utilities/" + script + ' ' + command
		else:
			fileExists = os.path.exists('./log/'+filename+'.txt')
			if(fileExists == True):
				exec_command = "python ../utilities/" + script + ' ' + command + ' | tee -a ../log/'+filename+'.txt'			
			else:
				exec_command = "python ../utilities/" + script + ' ' + command + ' | tee -a ../log/'+filename+'.txt'
		runScript = os.system(exec_command)
	return runScript

# -----------------------------------------------------------------------------------------------------
def executeCusConfigScript(script, command):
	"""This just runs scripts in a method """
	if(coreList.count(script)):
		os.chdir("./core")	
		exec_command = "python ../core/" + script + ' ' + command
		runScript = os.system(exec_command)
	elif(customList.count(script)):
		os.chdir("./custom")	
		exec_command = "python ../custom/" + script + ' ' + command
		runScript = os.system(exec_command)
	return runScript

# -----------------------------------------------------------------------------------------------------
def executeScript(script):
	"""This just runs scripts in a method """
	if(coreList.count(script)):
		os.chdir("./core")	
		runScript = os.system("python ../core/" + script)
	elif(customList.count(script)):
		os.chdir("./custom")	
		runScript = os.system("python ../custom/" + script)
	return runScript

# -----------------------------------------------------------------------------------------------------
def removeFromList(the_list, match):
	"""Used for removing color and size: tile- tags """
	newlist = []
	for item in the_list:
		if item.startswith(match):
			continue
		else:
			newlist.append(item)
	return newlist

# -----------------------------------------------------------------------------------------------------
#Change to directory and get all core scripts
dirList=os.listdir("./core")
for files in dirList:
	extension = os.path.splitext(files)[1]
	if(extension == '.py'):	
		scriptList.append(files)
		coreList.append(files)

#Then change to directory and get all custom scripts
dirList=os.listdir("./custom")
for files in dirList:
	extension = os.path.splitext(files)[1]
	if(extension == '.py'):	
		scriptList.append(files)
		customList.append(files)

#Then change to directory and get all custom config files
dirList=os.listdir("./configs")
for files in dirList:
	extension = os.path.splitext(files)[1]
	if(extension == '.py'):	
		configsList.append(files)

#Then change to directory and get all utilities files
dirList=os.listdir("./utilities")
for files in dirList:
	extension = os.path.splitext(files)[1]
	if(extension == '.py'):	
		utilitiesList.append(files)

# -----------------------------------------------------------------------------------------------------

if __name__ == '__main__':
	wobj = wapf.wapf(config.baseUrl, config.browser)
	
	jobs = []
	count = 1
	try:
		values = sys.argv[1:]
		utility = sys.argv[1]			
		#This is if value two is present, if it isn't just pass it on
		try:
			configs = sys.argv[2]
			commands = sys.argv[2]
		except:
			configs = ''
			pass
		#This is if value three is present, if it isn't just pass it on
		try:
			cmdValue = sys.argv[3]
		except:
			cmdValue = ''
			pass

		
		#check if there is config file
		checkConfig = configs.startswith('config_')
		checkCmd = utility.startswith('-u')
		
		#run header
		print ''
		print wobj.lineset(1)
		print runTitle
		print wobj.lineset(1)
		
		#if you just want to run utility commands
		if(len(values) != 0 and len(utility) != 0 and checkCmd):
			try:
				print colored('Run Status --> utility:', runColor)
				print colored(' [1] Running ' + commands + '.py', runColor)
				print ''
				print wobj.lineset(1)
				print ''				
				
				command = commands + '.py'
				#build write file
				writeFile = commands + '_' + config.today
				#execute and write to file
				runExecution = executeUtilityScript(command, cmdValue, writeFile)
			except:
				print ''
				print colored('Error please state a utility script you would like to run, Please try again!', errorColor)
				print ''					
		#if value is not zero and configs is not zero and configs is a custom config file
		elif(len(values) != 0 and len(configs) != 0 and checkConfig):
			try:
				#if there is a custom config value and more than 2 values, give notice and make them try again
				notvalid = sys.argv[3]
				print ''
				print colored('Error only 2 values can be give while using a custom config file, Please try again!', errorColor)
				print ''
			
			except:
				#else lets run the script with custom config file
				print colored('Run Status --> custom config:', runColor)
				print colored(' [1] Running ' + values[0] + '.py', runColor)
				print colored(' [2] Running ' + str(configs) + '.py', runColor)
				print ''
				print wobj.lineset(1)
				print ''
								
				for val in values:
					#Get custom config file (check a second time for config_? )
					if(val.startswith('config_')):
						configuration = val + '.py'
						configsExists = configsList.count(configuration)
						if(configsExists == 1):			
							error = 0
							executionList.append(configuration)	
						else:
							error = 1
							errorMessage = colored('Error config file: [' + configuration + '] doesn\'t exists, Please try again', errorColor)
							errorList.append(error)					
					
					#Get run file
					else:
						script = val + '.py'
						scriptExists = scriptList.count(script)
						if(scriptExists == 1):			
							error = 0
							executionList.append(script)
						else:
							error = 1
							errorMessage = colored('Error run file: [' + script + '] doesn\'t exists, Which should of been caught before this step!', errorColor)
							errorList.append(error)
				#check for file exists errors
				if 1 in errorList:
					print ''
					print errorMessage
					print ''
				else:
					#run the script and configuration file
					runExecution = executeCusConfigScript(executionList[0], executionList[1])
					print ''
					print wobj.lineset(1)
					print ''										
		#else if value not zero and value two is not a config file, so use default config
		elif (len(values) != 0 and checkConfig != 'config_'):
			print colored('Run Status --> default config:', runColor)
			
			for val in values:
				script = val + '.py'
				exists = scriptList.count(script)
				if(exists == 1):			
					executionList.append(script)
				else:
					print colored(' [0] ' +script + ' does not exist!', runColor)
					
			for executions in executionList:
				p = multiprocessing.current_process()				
				print colored(' [' + str(count) + '] Running ' + executions + ' ---> [PID] ' + str(p.pid), runColor)
				count = count + 1
				process = multiprocessing.Process(target=executeScript, args=(executions,))
				jobs.append(process)
				process.start()		
			print ''
			print wobj.lineset(1)			
			print ''		
		#No values passed give help
		else:
			print ''
			print colored('Please enter a command, or run "list" or "help" for details on how to use this framework. ', errorColor)
			print ''
		
	except KeyboardInterrupt:
		sys.exit(0)
	
