#!/usr/bin/env python

################################################################################
## NAME: KEYWORD DENSITY TEST
## DATE: Nov 2011
## AUTHOR: Jason R Alexander
## MAIL: JasonAlexander@zumiez.com
## SITE: http://www.zumiez.com
## INFO: This takes the crawler file of links and analyzes each link for it's keyword density
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
import operator
import sgmllib


baseUrl = 'http://www.zumiez.com/'
browser = 'firefox'
enableWrite = 1



f = open("/Users/jasonalexander/Desktop/clean_google_map.csv")
f2 = open("/Users/jasonalexander/Desktop/final_google_map.csv", "w")
uniquelines = set(f.read().split("\n"))
f2.write("".join([line + "\n" for line in uniquelines]))		
f2.close()