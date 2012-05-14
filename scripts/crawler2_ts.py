#!/usr/bin/env python

################################################################################
## NAME: MULTI-THREAD CRAWLER
## DATE: Oct 2011
## AUTHOR: Jason R Alexander
## MAIL: JasonAlexander@zumiez.com
## SITE: http://www.zumiez.com
## INFO: This is a basic multi-thread crawler recursive crawler 
################################################################################

import sys
import os
import re
import multiprocessing
import httplib
import time
sys.path.append( os.path.join( os.getcwd(), '..' ) )

import imports
import wapf


baseUrl = 'http://www.zumiez.com/'
browser = 'firefox'
enableWrite = 1
logFileName = 'zumiez_raw_links'

#create class instance
tobj = wapf.wapf(baseUrl, browser) #init baseUrl and browser
finalList = set()

linksList = tobj.getAllUniqueLinks(baseUrl)

categoryList1 = tobj.getAllUniqueLinks(baseUrl + 'shoes.html/')
categoryList2 = tobj.getAllUniqueLinks(baseUrl + 'guys.html/')
categoryList3 = tobj.getAllUniqueLinks(baseUrl + 'girls.html/')
categoryList4 = tobj.getAllUniqueLinks(baseUrl + 'skate.html/')
categoryList5 = tobj.getAllUniqueLinks(baseUrl + 'boys.html/')
categoryList6 = tobj.getAllUniqueLinks(baseUrl + 'accessories.html/')
categoryList7 = tobj.getAllUniqueLinks(baseUrl + 'snow.html/')
categoryList8 = tobj.getAllUniqueLinks(baseUrl + 'pro-riders.html/')
categoryList9 = tobj.getAllUniqueLinks(baseUrl + 'brands.html/')

categoryListNest = [categoryList1, categoryList2, categoryList3, categoryList4, categoryList5, categoryList6, categoryList7, categoryList8, categoryList9]


def bKrawler(linksList):
	for link in linksList:
		listPostion = list(linksList).index(link)
		status = str(tobj.statusCode(link))
		#Check HTTP Response
		if(status == '200'):		
			if link not in finalList:									
				#Write just links to file for later processing
				tobj.rawMessage(link, logFileName, 1)						
				finalList.add(link)
				try:
					childLinks = tobj.getAllUniqueLinks(link)	
					bKrawler(childLinks)
				except Exception, e:
					print "Thread finished crawl: " + str(e)
					pass						
		else:				
			print '404 Reponse ' + link					
	crawlList = list(finalList)
	return crawlList


#Non-multi-thread crawling
#generateList = bKrawler(linksList)


if __name__ == '__main__':
	jobs = []
	for category in categoryListNest:	    
		process = multiprocessing.Process(target=bKrawler, args=(category,))		
		jobs.append(process)
		process.start()
		
		#print 'PID: ' + str(process.pid)

	



"""

#Remove duplicate lines from a file
f = open("c:\\temp\\Original.txt")
f2 = open("c:\\temp\\Unique.txt", "w")
uniquelines = set(f.read().split("\n"))
f2.write("".join([line + "\n" for line in uniquelines]))
f2.close()


#!/usr/bin/env python
# Corey Goldberg - September 2009


import httplib
import sys
import time



if len(sys.argv) != 2:
    print 'usage:\nhttp_profiler.py \n(do not include http://)'
    sys.exit(1)

# get host and path names from url
location = sys.argv[1]
if '/' in location:
    parts = location.split('/')
    host = parts[0]
    path = '/' + '/'.join(parts[1:])
else:
    host = location
    path = '/'

# select most accurate timer based on platform
if sys.platform.startswith('win'):
    default_timer = time.clock
else:
    default_timer = time.time

# profiled http request
conn = httplib.HTTPConnection(host)
start = default_timer()  
conn.request('GET', path)
request_time = default_timer()
resp = conn.getresponse()
response_time = default_timer()
size = len(resp.read())
conn.close()     
transfer_time = default_timer()

# output
print '%.5f request sent' % (request_time - start)
print '%.5f response received' % (response_time - start)
print '%.5f content transferred (%i bytes)' % ((transfer_time - start), size)


"""






