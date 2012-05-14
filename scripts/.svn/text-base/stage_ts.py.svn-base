#!/usr/bin/env python

################################################################################
## NAME: TESTING STAGE
## DATE: July 2011
## AUTHOR: Jason R Alexander
## MAIL: JasonAlexander@zumiez.com
## SITE: http://www.zumiez.com
## KIND OF TEST: Testing Stage (For testing and configuring wapf)
################################################################################

import sys
import os
sys.path.append( os.path.join( os.getcwd(), '..' ) )
import wapf


baseUrl = 'http://www.zumiez.com/'
browser = 'firefox'
enableWrite = 0

#create class instance
tobj = wapf.wapf(baseUrl, browser) #init baseUrl and browser

import psutil

PROCNAME = "java"

for proc in psutil.process_iter():
    if proc.name == PROCNAME:
        print proc

