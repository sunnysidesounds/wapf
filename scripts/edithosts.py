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
from selenium import selenium
from threading import Thread
import subprocess
from Queue import Queue
sys.path.append( os.path.join( os.getcwd(), '..' ) )

import wapf
import config

wobj = wapf.wapf(config.baseUrl, config.browser)

print 'edit hosts file'
