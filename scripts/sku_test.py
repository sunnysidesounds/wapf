#!/usr/bin/env python

################################################################################
## NAME: SKU TEST
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


def getSkusFromFile(file_name):
	skuList = []
	skuFile = file_name
	logPath = '../log/'
	#Opening clean file
	f3 = open( logPath +skuFile+'.txt', "r")
	
	for sku in f3:
		if not sku.strip():
			continue
		else:
			sku = sku[:-1]
			skuList.append(sku)



skuList = []
skuFile = 'active_configurables'
logPath = '../log/'

#Opening clean file
f3 = open( logPath +skuFile+'.txt', "r")

for sku in f3:
	if not sku.strip():
		continue
	else:
		sku = sku[:-1]
		skuList.append(sku)



print skuList