#!/usr/bin/env python

################################################################################
## NAME: CRAWLER TEST
## DATE: July 2011
## AUTHOR: Jason R Alexander
## MAIL: JasonAlexander@zumiez.com
## SITE: http://www.zumiez.com
## KIND OF TEST: Test different crawler algorythums
################################################################################

import sys
import os
sys.path.append( os.path.join( os.getcwd(), '..' ) )
import wapf


baseUrl = 'http://www.zumiez.com/'
browser = 'firefox'
enableWrite = 1
crawlerView = 'write'
logFileName = 'zumiez_raw_links'

#create class instance
tobj = wapf.wapf(baseUrl, browser) #init baseUrl and browser
finalList = set()

linksList = tobj.getAllUniqueLinks(baseUrl)

def bKrawler(linksList):

	for link in linksList:
		listPostion = list(linksList).index(link)
		status = str(tobj.statusCode(link))
		#Check HTTP Response
		if(status == '200'):
		
			if link not in finalList:									
				print '------------------------------------------------------------------------------------------------------------------------------------------'
				tobj.rawMessage(link, logFileName, 1)
				p = re.compile(r'<.*?>')
				title = p.sub('', tobj.getContentFrom(link, 'title'))
				print '[Title: '+ title +' ] --- [Status: '+ status +' ] --- [File: ' + logFileName + '.txt ] --- [Indexed: ' + str(len(finalList)) + ' ]'
				print '------------------------------------------------------------------------------------------------------------------------------------------'
				print ''
						
				finalList.add(link)
				childLinks = tobj.getAllUniqueLinks(link)		
				bKrawler(childLinks)							
		else:				
			print '404 Reponse ' + link
					
	crawlList = list(finalList)
	return crawlList




generateList = bKrawler(linksList, crawlerView)

