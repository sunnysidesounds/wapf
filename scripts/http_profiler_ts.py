#!/usr/bin/env python

################################################################################
## NAME: WEB PROFILER
## DATE: August 2011
## AUTHOR: Jason R Alexander
## MAIL: JasonAlexander@zumiez.com
## SITE: http://www.zumiez.com
## KIND OF TEST: Returning web page profiling data
################################################################################


import sys
import os
sys.path.append( os.path.join( os.getcwd(), '..' ) )
import wapf
import config


#baseUrl = 'http://www.zumiez.com'
#browser = 'firefox'
#enableWrite = 0

#create class instance
tobj = wapf.wapf(config.baseUrl, config.browser) #init baseUrl and browser

#Get all body links in selected url
#linksList = tobj.getAllUniqueLinks(config.baseUrl)

#Storefront url
linksList = ['http://www.zumiez.com/shoes.html/', 'http://www.zumiez.com/guys.html/', 'http://www.zumiez.com/girls.html/', 'http://www.zumiez.com/skate.html/', 'http://www.zumiez.com/boys.html/', 'http://www.zumiez.com/accessories.html/', 'http://www.zumiez.com/snow.html/', 'http://www.zumiez.com/pro-riders.html/', 'http://www.zumiez.com/brands.html/']



count = 1

#loop them out to log file (if enabled)
for link in linksList:
	message = tobj.setHeaderMessage('Web Profiling: (' + str(count) + ')' , config.enableWrite)
	profiler = tobj.runProfiler(link, '/', config.browser, config.enableWrite)
	count +=1

