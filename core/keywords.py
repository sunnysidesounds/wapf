#!/usr/bin/env python

################################################################################
## NAME: KEYWORD DENSITY
## DATE: Nov 2011
## AUTHOR: Jason R Alexander
## MAIL: sunnysidesounds@gmail.com
## INFO: This gets keyword density of a specific list of pages
################################################################################

import sys
import os
import re
import multiprocessing
import httplib
import time
import string
sys.path.append( os.path.join( os.getcwd(), '..' ) )
from BeautifulSoup import BeautifulSoup
import wapf
#import config
import operator
import sgmllib

#THIS NEEDS A LOT OF WORK-
#Need to be able to switch from read and cleaning a file to read from a list via the config file


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

	
	#config.baseUrl = 'http://www.zumiez.com/'
	#config.browser = 'firefox'
	config.enableWrite = 1
	logRawFile = 'zumiez_raw_links103011'
	logCleanFile = 'zumiez_clean_links103011'
	logPath = '../log/'
	#config.template = "{0:25} {1:10} {2:15}" # column widths
	#config.templateTwo = "{0:30} {1:10}" # column widths
	#TODO: Make the file name more dynamic between scripts
	
	#create class instance
	wobj = wapf.wapf(config.baseUrl, config.browser) #init config.baseUrl and config.browser
	
	#check for clean log file
	logCleanFileCheck = os.path.exists(logPath + logCleanFile + '.txt')
	
	#Remove all duplicate links from file
	if(logCleanFileCheck != True):
		removeDuplicateLines = wobj.removeLineDups(logRawFile, logCleanFile)
	else:
		print 'Clean file already exists ['+logCleanFile+'.txt]'
	
	
	#Opening clean file
	print 'Opening ... ['+logCleanFile+'.txt]'
	f3 = open( logPath +logCleanFile+'.txt', "r")
	
	count = 1
	size_list = []
	
	for link in f3:
	    #if blank link strip-it!
	    if not link.strip():
	    	continue
	    else:
		    link = link[:-1]
		    status = str(wobj.statusCode(link))
		    #check status
		    if(status == '200'):
			    #get http transfer in bytes
			    transfer_size = int(wobj.httpSize(link))
			    #append to list to be counted
			    size_list.append(transfer_size)
			    total_transfer_size = str(sum(size_list))
			    pageLinks = wobj.getAllUniqueLinks(link)
			    linksCount = str(len(pageLinks))
			    
			    #Get seperate the head and body
			    headContent = wobj.getContentFrom(link, 'head')
			    bodyContent = wobj.getContentFrom(link, 'body')
				
				#Strip HTML shit!
				
				#Remove js
			    p = re.compile(r'<(script).*?</\1>(?s)')
			    bodyContent = p.sub('', bodyContent)
			    #Remove css
			    p = re.compile(r'<(style).*?</\1>(?s)')
			    bodyContent = p.sub('', bodyContent)
	    		#Remove all other html tags
			    p = re.compile(r'<.*?>')
			    bodyContent = p.sub('', bodyContent)		    
			    p = re.compile(r'&nbsp;')
			    bodyContent = p.sub('', bodyContent)			    
			    #Remove all whitespace
			    bodyContent = bodyContent.replace("\n", " ")
			    bodyContent = bodyContent.replace("\r", " ")
			    bodyContent = " ".join(bodyContent.split())
			    		    
				#get meta keyword from page		    
			    getMeta = re.search( "<meta name=\"keywords\".*?content=\"([^\"]*)\"", headContent).group( 1 )
			    metaList = string.split(getMeta, ',')
			    
			    #Count words on page (Needs work)
			    frequencies = {}
			    freq_count = 1
			    for c in re.split('\W+', bodyContent):
			    	for num in range(65, 91): # A to Z
			    		capLetter = chr(num)
			    		#Check if first letter is capital	or if the word is in the meta keyword list	    				    		
			    		if capLetter in c[:1] or c in metaList:
			    			frequencies[c] = (frequencies[c] if frequencies.has_key(c) else 0) + 1
			    			freq_count = freq_count + 1
			    			
			    result = frequencies
			    totalWords = float(freq_count)
			    #Strip white space
			    pageTitle = wobj.getPageTitle(link).strip()
			    		    		
			 	#display data
			    print wobj.lineset(1)
			    print 'Link: ' + link
			    print wobj.lineset(1)
			    print config.templateTwo.format('Page Title:', pageTitle)
			    print config.templateTwo.format('Total Pages Indexed:', str(count))
			    print config.templateTwo.format('Total Links on Page:', linksCount)
			    print config.templateTwo.format('Total Word Count:', str(totalWords))
			    print config.templateTwo.format('Total Bytes Transferred:', total_transfer_size + ' bytes')
			    print config.templateTwo.format('Page Request Sent:', wobj.httpRequestSend(link))
			    print config.templateTwo.format('Page Reponse Received:', wobj.httpReponseReceived(link))
			    print config.templateTwo.format('Page Content Transferred:', wobj.httpContentTransferred(link))
			    print wobj.lineset(1)
			    
			    #TODO: Write stuff below to csv file
	
			    print config.template.format("KEYWORD", "COUNT", "PERCENTAGE") # header		    
			    #sorted by value in reverse order so big number are at the top
			    for word, freq in sorted(result.iteritems(), key=operator.itemgetter(1), reverse=True):
		    		percentage = (freq*100)/totalWords #Keyword density forumla
		    		if(freq > 1):	    					    	
			    		print config.template.format(word, str(freq), str(round(percentage, 4)) + '%')
			    	else:
			    		print config.template.format(word, str(freq), str(round(percentage, 4)) + '%')
			    		    		
			    print wobj.lineset(1)
			    
			    
			    print ' '
			    count =  count + 1
		    else:
		    	if(status == '404'):
		    		print '404 Response'
		    	else:
		    		print 'Error in this line of data'
    
    
    
    
    



