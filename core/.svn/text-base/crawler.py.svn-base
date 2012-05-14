#!/usr/bin/env python

################################################################################
## NAME: MULTI-THREAD CRAWLER
## DATE: Oct 2011
## AUTHOR: Jason R Alexander
## MAIL: JasonAlexander@zumiez.com
## INFO: This is a basic multi-thread crawler recursive crawler 
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

def bKrawler(linksList):
	for link in linksList:
		listPostion = list(linksList).index(link)
		status = str(wobj.statusCode(link))
		#Check HTTP Response
		if(status == '200'):		
			if link not in finalList:									
				#Write just links to file for later processing
				wobj.rawMessage(link, config.crawlerFileName, 1)						
				finalList.add(link)
				try:
					childLinks = wobj.getAllUniqueLinks(link)	
					bKrawler(childLinks)
				except Exception, e:
					print "Thread finished crawl: " + str(e)
					pass						
		else:				
			print '404 Reponse ' + link					
	crawlList = list(finalList)
	return crawlList


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
	finalList = set()
	nestedLinksList = []
	linksList = config.crawlerList
	for links in linksList:
		nestedLinksList.append(wobj.getAllUniqueLinks(links))	
	
	jobs = []
	for thread in nestedLinksList:	    
		process = multiprocessing.Process(target=bKrawler, args=(thread,))		
		jobs.append(process)
		process.start()
	print 'Crawler threads started: ' + str(len(nestedLinksList))
	print wobj.lineset(1)
	
	
	
	