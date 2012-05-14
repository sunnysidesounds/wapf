#!/usr/bin/env python

################################################################################
## NAME: GIFT CARD PAGE PROFILING
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


baseUrl = 'http://www.zumiez.com/'
browser = 'firefox'
enableWrite = 1

#create class instance
tobj = wapf.wapf(baseUrl, browser) #init baseUrl and browser



profilerGC = tobj.runProfiler('http://www.zumiez.com/giftcard/index/buy/', '/', browser, enableWrite)


