#!/usr/bin/env python

################################################################################
## NAME: TEST ZUMIEZ MY BAG
## DATE: Oct 2011
## AUTHOR: Jason R Alexander
## MAIL: sunnysidesounds@gmail.com
##INFO: This checks each store front left nav
################################################################################

import sys
import os
import re
import multiprocessing
import httplib
import time
from random import choice
sys.path.append( os.path.join( os.getcwd(), '..' ) )
#custom modules
import wapf
import config


#Values
# --------------------------------------------------------------------------------------------------------------------------------------------------------
zcustomFileName = 'zumiez_leftnav'

leftNavMastetList = {}


#create a wapf instance
wobj = wapf.wapf(config.baseUrl, config.browser)
#get out browser instance
#browser = wobj.setBrowser(config.browser)
wobj.message('Test date: ' + config.systemDates, config.customFileName + zcustomFileName)
wobj.message('Creating wapf and selenium instances...', config.customFileName + zcustomFileName)


if(config.baseUrl == 'http://www.zumiez.com/'):

	for pageLink in config.alphaList:
		if(pageLink == config.baseUrl + 'skate.html'):
			leftnavLinks = wobj.getLinksFrom(pageLink, 'div', 'id', 'skateLeftNav')
			#leftNavMastetList.append(leftnavLinks)
			leftNavMastetList[pageLink] = leftnavLinks
		elif(pageLink == config.baseUrl + 'pro-riders.html/'):
			leftnavLinks = wobj.getLinksFrom(pageLink, 'div', 'id', 'proRiderLeftNav')
			#leftNavMastetList.append(leftnavLinks)
			leftNavMastetList[pageLink] = leftnavLinks
		elif(pageLink == config.baseUrl + 'brands.html/'):
			leftnavLinks = wobj.getLinksFrom(pageLink, 'div', 'class', 'span-182 maxHeight BrandLeftSide')
			#leftNavMastetList.append(leftnavLinks)
			leftNavMastetList[pageLink] = leftnavLinks
		else:
			leftnavLinks = wobj.getLinksFrom(pageLink, 'div', 'class', 'sideNav')
			#leftNavMastetList.append(leftnavLinks)
			leftNavMastetList[pageLink] = leftnavLinks

elif(config.baseUrl == 'http://virtual.zumiez.com/'):
	for pageLink in config.alphaList:
		leftnavLinks = wobj.getLinksFrom(pageLink, 'div', 'class', 'sfLeftNav')
		#leftNavMastetList.append(leftnavLinks)
		leftNavMastetList[pageLink] = leftnavLinks

else:
	print 'Error in config.baseUrl!'
	
	
	
wobj.message('', config.customFileName + zcustomFileName)
for urlKey, linkList in leftNavMastetList.iteritems():
	status = wobj.statusCode(urlKey)
	#print urlKey + '\n'
	wobj.message('[BASEURL:'+str(status)+'] ---> ' + urlKey, config.customFileName + zcustomFileName)
	for link in linkList:
		status = wobj.statusCode(link)
		if(status == 200):
			wobj.message(' [STATUS:'+str(status)+'] --- [TITLE:'+ wobj.getPageTitle(link)+'] ---> ' + link, config.customFileName + zcustomFileName)
		else:
			wobj.message('', config.customFileName + zcustomFileName)
			wobj.message(' Page Not Found', config.customFileName + zcustomFileName)
			wobj.message(' [STATUS:'+str(status)+'] --- [TITLE:'+ wobj.getPageTitle(link)+'] ---> ' + link, config.customFileName + zcustomFileName)
			wobj.message('', config.customFileName + zcustomFileName)
			
	wobj.message('', config.customFileName + zcustomFileName)
	wobj.message('', config.customFileName + zcustomFileName)




