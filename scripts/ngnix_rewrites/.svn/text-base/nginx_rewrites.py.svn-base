#!/usr/bin/env python

################################################################################
## NAME: NGINX REWRITE SCRIPT
## DATE: Oct 2011
## AUTHOR: Jason R Alexander
## MAIL: JasonAlexander@zumiez.com
## SITE: http://www.zumiez.com
################################################################################

import os
import json
import socket
import sys
import time
import urlparse
import urllib
import re
import xml.etree.ElementTree as etree
from datetime import datetime
import os
from subprocess import *

from selenium import selenium
from selenium import webdriver
sys.path.append( os.path.join( os.getcwd(), '..' ) )
import testerLib



#General values
baseUrl = 'http://www.zumiez.com/'
browser = 'firefox'
enableWrite = 1
productList = []

#Beauitful Soup values
bsTag = 'h2'
bsAttribute = 'class'
bsAttributeName = 'pdp-product-detail-name-productname'


#create class instance
tobj = testerLib.testerLib(baseUrl, browser) #init baseUrl and browser


f = open("ngnix_product_ids.txt", "r")
count = 0

for line in f:
    line = line[:-1]
    #build url
    productUrl = baseUrl +'catalog/product/view/id/'+line+'/category/*'
	#get product title from page
    title = tobj.getContentFrom(productUrl, bsTag, bsAttribute, bsAttributeName)
    p = re.compile(r'<.*?>')
    #strip html tags
    cleanTitle = p.sub('', title)
    #all string lowercase
    lowercaseTitle = cleanTitle.lower()
    #replace whitespace and certain other symbols and characters.
    dashesTitle = lowercaseTitle.replace (" ", "-")    
    astropheTitle = dashesTitle.replace("'", "")
    doublequoteTitle = astropheTitle.replace('"', '')
    andTitle = doublequoteTitle.replace("&", "and")
    periodTitle = andTitle.replace(".", "-")
    slashTitle = andTitle.replace("/", "-")    
    #Build final url    
    relHtmlTitle = slashTitle + '.html'
    htmlTitle = baseUrl + relHtmlTitle
	
    status = tobj.statusCode(productUrl)    
    #check for valid link
    if(str(status) == '200'):
    	print str(count) + ') [' + productUrl + '] redirects to [' + htmlTitle + ']'
    	print '---------------------------------------------------------------------------------------------------------------------------- '
    	
    	#build Ngnix values
    	ngnixComments = '# redirect product_id: '+ line +' with any catagory to the SEO friendly url'
    	ngnixLine1 = 'location /catalog/product/view/id/'+line+'/category/* {'
    	ngnixLine2 = '		rewrite ^(/catalog/product/view/id/'+ line +'/category/*)$ /'+relHtmlTitle+';'
    	ngnixLine3 = '		return 403;'
    	ngnixLine4 = '}'
    	ngnixLine5 = ' ' 
    	
    	#Write to file
    	tobj.printMessage(ngnixComments, enableWrite)
    	tobj.printMessage(ngnixLine1, enableWrite)
    	tobj.printMessage(ngnixLine2, enableWrite)
    	tobj.printMessage(ngnixLine3, enableWrite)
    	tobj.printMessage(ngnixLine4, enableWrite)
    	tobj.printMessage(ngnixLine5, enableWrite)
    	   	
    	count = count + 1
    	
    	
    	
    	
    	
    	
    	
