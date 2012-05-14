#!/usr/bin/env python

################################################################################
## NAME: TESTER LIBRARY
## DATE: July 2011
## AUTHOR: Jason R Alexander
## MAIL: JasonAlexander@zumiez.com
## SITE: http://www.zumiez.com
## VERSION: For version information run 'version'
################################################################################

import sys
import urllib
import urllib2
import time
import datetime
from datetime import datetime
import json
import commands
import re
import os
import random
import httplib
import urlparse
import socket
import xml.etree.ElementTree as etree
import subprocess
import shlex
from termcolor import colored


#Check for BeautifulSoup module
try:
	from BeautifulSoup import BeautifulSoup
except Exception, err:
	print "This module requires the BeautifulSoup module (http://www.crummy.com/software/BeautifulSoup/)"
	sys.stderr.write('ERROR: %s\n' % str(err))
	sys.exit()
#Check to see if Selenium 2 is installed
try:
	from selenium import selenium
	from selenium import webdriver
	from selenium.common.exceptions import NoSuchElementException
except Exception, err: 
	print "This module requires the selenium webdriver to be installed (http://pypi.python.org/pypi/selenium/2.0.1) "
	sys.stderr.write('ERROR: %s\n' % str(err))
	sys.exit()



# MAIN CLASS
# --------------------------------------------------------------------------------------------------------------------------------------------------------------- # 

class wapf(object):    
	""" This class runs functional tests with selenium 1 and 2 and BeautifulSoup """
	# --------------------------------------------------------------------------------------------------------------------------------------------------------------- #     
	def __init__(self, baseUrl, browser):
	    self.baseUrl = baseUrl
	    self.html_validator_url = 'http://validator.w3.org/check'
	    self.finalList = set()
	    self.browser = browser
	    #self.setBrowser(self.browser)
	
	# --------------------------------------------------------------------------------------------------------------------------------------------------------------- #
	def setBrowser(self, browser):
	    """This sets the webdriver browser to use """
	    if(browser == 'firefox'):
	        self.browserDriver = webdriver.Firefox()
	    elif(browser == 'chrome'):
	        self.browserDriver = webdriver.Chrome()
	    elif(browser == 'safari'):
	        self.browserDriver = webdriver.Safari()
	        sys.exit()
	    elif(browser == 'IE'):
	        self.browserDriver = webdriver.Ie()
	    elif(browser == 'opera'):
	        print 'Opera coming soon!'
	        sys.exit()
	    elif(browser == 'remote'):
	        print 'Enable remote'
	        #os.system("java -jar selenium-server-standalone-2.1.0.jar")
	        self.browserDriver =  webdriver.Remote(command_executor= 'http://127.0.0.1:4444/wd/hub', desired_capabilities={'browserName': 'firefox', 'version': '2', 'javascriptEnabled': True})
	    else:
	        print 'You haven\'t selected a browser driver!'
	        sys.exit()
	    
	    return self.browserDriver
	# --------------------------------------------------------------------------------------------------------------------------------------------------------------- #
	#def setRemote(self, ):

		
	# --------------------------------------------------------------------------------------------------------------------------------------------------------------- #
	def setHeaderMessage(self, kindOfTest, writeMessage = 0):
	    today = time.strftime("%m-%d-%Y at %H:%M")
	    self.printMessage('-------------------------------------------------------------------------------------------', writeMessage)
	    self.printMessage('TEST: ' + kindOfTest, writeMessage)
	    self.printMessage('Testing with ' + self.browser + ' on ' +str(today), writeMessage) 
	    self.printMessage('Base url for this test is: [' + self.baseUrl + ']', writeMessage)
	    self.printMessage('-------------------------------------------------------------------------------------------', writeMessage)
	
	# --------------------------------------------------------------------------------------------------------------------------------------------------------------- #
	def printMessage(self, message, write_message = 0):
	    """Instead of using print statement, This method give you the ability to write to a log file. (Creates multiple files with timestamp) """
	    if(write_message == 1):
	        today = time.strftime("%Y%m%d%H")
	        print >> fileWriter(sys.stdout, '../log/results_'+ today +'_'+self.browser+'.txt'), message
	    else:
	        print message
	
	# --------------------------------------------------------------------------------------------------------------------------------------------------------------- #     
	def rawMessage(self, message, file_name, write_message = 0):
	    """This prints out to a raw non-dated log file. (Creates a single file) """
	    if(write_message == 1):
	        print >> fileWriter(sys.stdout, '../log/'+file_name+'.txt'), message
	    else:
	        print message

	# --------------------------------------------------------------------------------------------------------------------------------------------------------------- #     
	def removeLineDups(self, raw_file, clean_file):
		"""Remove duplicate lines from a file """
		print 'Processing ... [Raw: '+raw_file+'.txt] ---> [Clean: '+clean_file+'.txt]'
		f = open('../log/'+raw_file+'.txt')
		f2 = open('../log/'+clean_file+'.txt', "w")
		uniquelines = set(f.read().split("\n"))
		f2.write("".join([line + "\n" for line in uniquelines]))		
		f2.close()
			
	# --------------------------------------------------------------------------------------------------------------------------------------------------------------- #     
	def message(self, msg, writeFile):
		"""Prints out validation errors """
		if(writeFile != ''):
			fileName = writeFile
			self.rawMessage(msg, fileName, 1)
		else:
			self.printMessage(msg, 1)
		
	# --------------------------------------------------------------------------------------------------------------------------------------------------------------- #
	def crawlSite(self, linksList, enableWrite = 0):
		"""This does a recursive crawl building a unique link list """			
		count = 0
		for link in linksList:
			if link not in self.finalList:
				#Remove query string urls
				if(self.searchUrlString(link, '?') == False):
					#Remove semi-colon
					if(self.searchUrlString(link, ';') == False):
						self.printMessage('Added ' + link, enableWrite)					
						self.finalList.add(link)
						childLinks = self.getAllUniqueLinks(link)
						length = len(childLinks)
						self.printMessage('Total links for this page: ' + str(length), enableWrite)
						self.printMessage('---------------------------------------------------------------------------', enableWrite)
						self.crawlSite(childLinks, enableWrite)
					else:
						print 'Not adding this link: ' + link		
				else: 
					print 'Not adding this link: ' + link
		crawlList = list(self.finalList)
		return crawlList

	# --------------------------------------------------------------------------------------------------------------------------------------------------------------- #
	def rawCrawler(self, linksList, enableWrite = 0):
		"""This does a recursive raw crawl"""			
		count = 0
		for link in linksList:
			if link not in self.finalList:
					if(self.searchUrlString(link, ';') == False):												
						self.printMessage('Added ' + link, enableWrite)					
						self.finalList.add(link)
						childLinks = self.getAllUniqueLinks(link)
						length = len(childLinks)
						self.printMessage('Total links for this page: ' + str(length), enableWrite)
						self.printMessage('---------------------------------------------------------------------------', enableWrite)
						self.crawlSite(childLinks, enableWrite)
					else:
						print 'Not adding this link: ' + link		
		crawlList = list(self.finalList)
		return crawlList
	
	# --------------------------------------------------------------------------------------------------------------------------------------------------------------- #
	def httpRequestProfiler(self, url):
		"""This return both HTTP request, response and transferrs """
		#Remove http:// from url
		formatUrl = url.split("/",2)		
		location = formatUrl[-1]
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
		
		out = ''		
		# output
		out += ' %.5f request sent \n' % (request_time - start)
		out += ' %.5f response received \n' % (response_time - start)
		out += ' %.5f content transferred (%i bytes)' % ((transfer_time - start), size)
		
		return out
	

	# --------------------------------------------------------------------------------------------------------------------------------------------------------------- #
	def convertBytes(self, bytes):
	    """Convert bytes to larger format """
	    bytes = float(bytes)
	    if bytes >= 1099511627776:
	        terabytes = bytes / 1099511627776
	        size = '%.2f tb' % terabytes
	    elif bytes >= 1073741824:
	        gigabytes = bytes / 1073741824
	        size = '%.2f gb' % gigabytes
	    elif bytes >= 1048576:
	        megabytes = bytes / 1048576
	        size = '%.2f mb' % megabytes
	    elif bytes >= 1024:
	        kilobytes = bytes / 1024
	        size = '%.2f kb' % kilobytes
	    else:
	        size = '%.2f b' % bytes
	    return size
	
	# --------------------------------------------------------------------------------------------------------------------------------------------------------------- #
	def httpSize(self, url):
		"""Return http size """
		formatUrl = url.split("/",2)		
		location = formatUrl[-1]
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
		
		conn = httplib.HTTPConnection(host)
		start = default_timer()  
		conn.request('GET', path)
		resp = conn.getresponse()
		size = len(resp.read())
		conn.close()     
		
		return size

	# --------------------------------------------------------------------------------------------------------------------------------------------------------------- #
	def httpRequestSend(self, url):
		"""Return http request send """
		formatUrl = url.split("/",2)		
		location = formatUrl[-1]
		if '/' in location:
		    parts = location.split('/')
		    host = parts[0]
		    path = '/' + '/'.join(parts[1:])
		else:
		    host = location
		    path = '/'
		    		
		if sys.platform.startswith('win'):
		    default_timer = time.clock
		else:
		    default_timer = time.time
		
		conn = httplib.HTTPConnection(host)
		start = default_timer()  
		conn.request('GET', path)
		request_time = default_timer()
		resp = conn.getresponse()
		conn.close()     
		response_times = (request_time - start)
		
		return response_times

	# --------------------------------------------------------------------------------------------------------------------------------------------------------------- #
	def httpReponseReceived(self, url):
		"""Return http response received """
		formatUrl = url.split("/",2)		
		location = formatUrl[-1]
		if '/' in location:
		    parts = location.split('/')
		    host = parts[0]
		    path = '/' + '/'.join(parts[1:])
		else:
		    host = location
		    path = '/'
		
		if sys.platform.startswith('win'):
		    default_timer = time.clock
		else:
		    default_timer = time.time
		
		conn = httplib.HTTPConnection(host)
		start = default_timer()  
		conn.request('GET', path)
		resp = conn.getresponse()
		response_time = default_timer()
		conn.close()     
		response_times = (response_time - start)
		
		return response_times

	# --------------------------------------------------------------------------------------------------------------------------------------------------------------- #
	def httpContentTransferred(self, url):
		"""Returns content transferred time """
		formatUrl = url.split("/",2)		
		location = formatUrl[-1]
		if '/' in location:
		    parts = location.split('/')
		    host = parts[0]
		    path = '/' + '/'.join(parts[1:])
		else:
		    host = location
		    path = '/'
		
		if sys.platform.startswith('win'):
		    default_timer = time.clock
		else:
		    default_timer = time.time
		
		conn = httplib.HTTPConnection(host)
		start = default_timer()  
		conn.request('GET', path)
		resp = conn.getresponse()
		conn.close()     
		transfer_time = default_timer()
		response_times = (transfer_time - start)
		
		return response_times
		
	# --------------------------------------------------------------------------------------------------------------------------------------------------------------- #
	def searchUrlString(self, string, character):
		"""SImple character search of a string """
		if character in string:
			return True
		else: 
			return False
			
	# --------------------------------------------------------------------------------------------------------------------------------------------------------------- #     	
	def validateUrl(self, filename, writeFile = ''):
		#writeFile = default or raw
		"""Validates given urls with the w3c-validator  """
		quoted_filename = urllib.quote(filename)
		if filename.startswith('http://'):
			cmd = ('curl -sG -d uri=%s -d output=json %s'
					% (quoted_filename, self.html_validator_url))
		else:
			cmd = ('curl -sF "uploaded_file=@%s;type=text/html" -F output=json %s'
					% (quoted_filename, self.html_validator_url))
		#verbose(cmd)
		status,output = commands.getstatusoutput(cmd)
		if status != 0:
			raise OSError (status, 'failed: %s' % cmd)
		#verbose(output)
		try:
			result = json.loads(output)
		except ValueError:
			result = ''
		time.sleep(2)   # Be nice and don't hog the free validator service.
		errors = 0
		warnings = 0
		#Loop out result
		for msg in result['messages']:
			#enable both errors and info
			#self.message('%(type)s: line %(lastLine)d: %(message)s' % msg, writeFile)		
			if msg['type'] == 'error':
				#Print only errors
				self.message(str(msg['type']).ljust(6) + '--> line: ' + str(msg['lastLine']).ljust(6) + ': ' + str(msg['message']).ljust(6), writeFile)
				errors += 1
			else:
				warnings += 1
		
	# --------------------------------------------------------------------------------------------------------------------------------------------------------------- #     
	def checkUrl(self, url): 
		"""Check for validate url """
		request = urllib2.Request(url)
		request.get_method = lambda : 'HEAD'
		try:
			response = urllib2.urlopen(request)
			return True
		except urllib2.HTTPError:
			return False
	
	# --------------------------------------------------------------------------------------------------------------------------------------------------------------- #
	def clickByLink(self, href, writeLog):
		self.browserDriver.find_element_by_css_selector("a[href='"+ href +"']").click()
		self.printMessage(' -Clicking: ' + href, writeLog)	
	
	# --------------------------------------------------------------------------------------------------------------------------------------------------------------- #
	def clickByXPath(self, xpath, writeLog):
		self.browserDriver.find_element_by_xpath(xpath).click()
		self.printMessage(' -Clicking: ' + xpath, writeLog)
	
	# --------------------------------------------------------------------------------------------------------------------------------------------------------------- #
	def clickByID(self, id, writeLog):
		self.browserDriver.find_element_by_id(id).click()
		self.printMessage(' -Clicking: ' + id, writeLog)
	
	# --------------------------------------------------------------------------------------------------------------------------------------------------------------- #
	def fillInputByID(self, id, text, writeLog):
		fillInput = self.browserDriver.find_element_by_id(id)
		fillInput.send_keys(text)
		self.printMessage(' -Filling form values('+id+'): ' + text, writeLog)
	
	# --------------------------------------------------------------------------------------------------------------------------------------------------------------- #
	def fillInputByName(self, name, text, writeLog):
		fillInput = self.browserDriver.find_element_by_name(name)
		fillInput.send_keys(text)
		self.printMessage(' -Filling form values('+name+'): ' + text, writeLog)
	
	# --------------------------------------------------------------------------------------------------------------------------------------------------------------- #
	def statusCode(self, url):
	    statusCode = urllib.urlopen(url).getcode()
	    return statusCode
	
	# --------------------------------------------------------------------------------------------------------------------------------------------------------------- #
	def waitForCondition(self, js_cmd):
	    # Selenium 2 no longer has a wait_for_condition, so we have to create our own polling routine.
	    for i in xrange(30):
	        ret = self.browserDriver.execute_script(js_cmd)
	        if ret is True:
	            return True
	        time.sleep(.25)
	    if ret is False:
	        print "JavaScript command %s did not finish completing (ret_val=%s)" % (js_cmd, ret)
	        #raise Exception
	
	# --------------------------------------------------------------------------------------------------------------------------------------------------------------- # 
	def formattedScreenshot(self, url, folderName, writeLog):
		uniqueFilename = self.getUrlEnding(url)
		#set a default
		if len(uniqueFilename) == 0:
			uniqueFilename = '_baseurl'
		else:
			uniqueFilename = uniqueFilename
		self.getScreenshot(uniqueFilename, folderName)
		self.printMessage('	-Screenshot Name: ' + uniqueFilename, writeLog)
		
	# --------------------------------------------------------------------------------------------------------------------------------------------------------------- # 
	def getScreenshot(self, fileMessage, folderName = ''):
	    """Get screenshot of the given page """
	    today = time.strftime("%m%d%Y")
	    folder = folderName + '_' + str(today)
	    exists = os.path.exists('../screenshots/' + folder)
	    if(exists != True):
	        self.makeFolder('../screenshots/' + folder)
	    self.browserDriver.get_screenshot_as_file('../screenshots/'+ folder +'/screenshot_'+self.browser+'_'+fileMessage+'.png')
	
	# --------------------------------------------------------------------------------------------------------------------------------------------------------------- # 
	def runProfiler(self, site, path, browser, writeFile = ''):  
	    '''This profiles web pages with selenium standalone server '''
	    sel = selenium('127.0.0.1', 4444, browser, site)
	    
	    print sel
	    
	    try:
	        sel.start('captureNetworkTraffic=true')
	    except socket.error:
	        print 'ERROR - Selenium Standalone not running. Run shell script in /selenium_standalone/start_selenium.sh (./start_selenium.sh)'
	        sys.exit(1)
	        
	    sel.open(path)
	    sel.wait_for_page_to_load(60000)   
	    end_loading = datetime.now()
	    
	    raw_xml = sel.captureNetworkTraffic('xml')
	                
	    sel.stop()
	    
	    traffic_xml = raw_xml.replace('&', '&amp;').replace('=""GET""', '="GET"').replace('=""POST""', '="POST"') # workaround selenium bugs
	    
	    nc = NetworkCapture(traffic_xml)
	    
	    #json_results = nc.get_json()
	    
	    num_requests = nc.get_num_requests()
	    total_size = nc.get_content_size()
	    status_map = nc.get_http_status_codes()
	    file_extension_map = nc.get_file_extension_stats()
	    http_details = nc.get_http_details()
	    start_first_request, end_first_request, end_last_request = nc.get_network_times()
	    
	    end_load_elapsed = self.getElapsedSecs(start_first_request, end_loading)
	    end_last_request_elapsed = self.getElapsedSecs(start_first_request, end_last_request)
	    end_first_request_elapsed = self.getElapsedSecs(start_first_request, end_first_request)
	    
	    self.message('', writeFile)	    
	    #self.message('results for %s' % site, writeFile)
	    
	    self.message('\ncontent size: %s kb' % total_size, writeFile)
	    
	    self.message('\nhttp requests: %s' % num_requests, writeFile)
	    for k,v in sorted(status_map.items()):
	        self.message('status %s: %s' % (k, v), writeFile)
	    
	    self.message('\nprofiler timing:', writeFile)

	    self.message('%.3f secs (page load)' % end_load_elapsed, writeFile)
	    self.message('%.3f secs (network: end last request)' % end_last_request_elapsed, writeFile)
	    self.message('%.3f secs (network: end first request)' % end_first_request_elapsed, writeFile)
	    
	    self.message('\nfile extensions: (count, size)', writeFile)
	    for k,v in sorted(file_extension_map.items()):
	        self.message('%s: %i, %.3f kb' % (k, v[0], v[1]), writeFile)
	        
	    self.message('\nhttp timing detail: (status, method, doc, size, time)', writeFile)
	    for details in http_details:
	        self.message('%i, %s, %s, %i, %i ms' % (details[0], details[1], details[2], details[3], details[4]), writeFile)
	
	# --------------------------------------------------------------------------------------------------------------------------------------------------------------- #
	def getElapsedSecs(self, dt_start, dt_end):
	    return float('%.3f' % ((dt_end - dt_start).seconds + 
	        ((dt_end - dt_start).microseconds / 1000000.0)))
		
	# --------------------------------------------------------------------------------------------------------------------------------------------------------------- #
	def getUrlEnding(self, url):
		"""This is to put the url in the filename """
		baseDomain = self.getBaseDomain(url)
		removeBaseDomain = url.replace(baseDomain, '')
		removeHttp = removeBaseDomain.replace('http://', '')
		removeBackSlash = removeHttp.replace('/', '_')
		removeDashes = removeBackSlash.replace('-', '_')
		removePeriods = removeDashes.replace('.', '_')
		removeQuestionMark = removePeriods.replace('?', '')
		removeEqualSign = removeQuestionMark.replace('=', '')
		removeAmberSign = removeEqualSign.replace('&amp;', '')
		returnEnding = removeAmberSign	
		return returnEnding
	
	# --------------------------------------------------------------------------------------------------------------------------------------------------------------- #     
	def getRandomLink(self, baseUrl):
		"""Makes a unique list of url and randomly picks one """
		#TODO: Could add getAllUniqueLinks to do some of this work below
		#get all links in body tags
		#getBodyLinks = self.getLinksFrom(baseUrl, 'body')
		getBodyLinks = self.getVisibleLinks(baseUrl) 
		#remove all pound sign elements
		subList = self.removeFromList(getBodyLinks, '#')	
		#remove all non base url links
		mainList = self.removeNonBaseUrlLinks(subList)
		#remove all duplicates
		finalList = list(set(mainList))		
		#Strip out similar duplicates by removing all / from urls that need it
		masterList = set(map(lambda url: url.rstrip('/'), finalList))			
		#Get total number of links
		getTotalLinks = len(masterList)
		#Get a random Link to follow
		getRandomLink = random.randrange(0, getTotalLinks, 1)
		return mainList[getRandomLink]

	# --------------------------------------------------------------------------------------------------------------------------------------------------------------- #     
	def getAllUniqueLinks(self, baseUrl):
		"""Returns a unique list of urls """
		getBodyLinks = self.getVisibleLinks(baseUrl) 
		#remove all pound sign elements
		subList = self.removeFromList(getBodyLinks, '#')	
		#remove all non base url links
		mainList = self.removeNonBaseUrlLinks(subList)
		#remove all duplicates
		finalList = list(set(mainList))		
		#Strip out similar duplicates by removing all / from urls that need it
		masterList = set(map(lambda url: url.rstrip('/'), finalList))
		listOfLinks = list(masterList)
		return listOfLinks

	# --------------------------------------------------------------------------------------------------------------------------------------------------------------- #     
	def getPageTitle(self, url):
		p = re.compile(r'<.*?>')
		title = p.sub('', self.getContentFrom(url, 'title'))
		
		return title	

	# --------------------------------------------------------------------------------------------------------------------------------------------------------------- #     
	def isElementPresent(self, element, browser):
		"""This check is a element is present on the page """
		#browser attribute is the setBrowser instance
		try:
			browser.find_element_by_id(element)
			return True
		except:
			return False
		#return True
	
	# --------------------------------------------------------------------------------------------------------------------------------------------------------------- #     
	def getContentFrom(self,url, html_tag, attrib=None, attribName=None):
		"""Grabs blocks of html and it's content """
		contents = urllib.urlopen(url).read()
		soup = BeautifulSoup(contents)    
		if(attrib != None and attribName != None):
			#get content from id/class
			getBody = soup.find(html_tag, { attrib : attribName })
		elif(attrib == None and attribName != None or attrib != None and attribName == None):
			return 'all attribs not set (attrib:'+str(attrib)+', attribName:'+str(attribName)+')'
		else:
			#get all content of the html_tag
			getBody = soup.find(html_tag)    
		#convert to string
		cvtToString = str(getBody)
		return cvtToString
		
	
	# --------------------------------------------------------------------------------------------------------------------------------------------------------------- #     
	def getLinksFrom(self, url, html_tag, attrib=None, attribName=None):
		"""Get links from any div, table..etc. container """
		contents = urllib.urlopen(url).read()
		soup = BeautifulSoup(contents)    
		if(attrib != None and attribName != None):
			#get content from id/class
			getBody = soup.find(html_tag, { attrib : attribName })
		elif(attrib == None and attribName != None or attrib != None and attribName == None):
			return 'all attribs not set (attrib:'+str(attrib)+', attribName:'+str(attribName)+')'
		else:
			#get all content of the html_tag
			getBody = soup.find(html_tag)    		
		#convert to string
		cvtToString = str(getBody)		
		links = re.findall(r'href=[\'"]?([^\'" >]+)', cvtToString)		
		#return links array
		return links

	# --------------------------------------------------------------------------------------------------------------------------------------------------------------- #     
	def getVisibleLinks(self, url):
		"""This gets only visible clickable links """		
		contents = urllib.urlopen(url).read()		
		soup = BeautifulSoup(contents)
		getBody = soup.findAll('a')
		#convert to string
		cvtToString = str(getBody)		
		links = re.findall(r'href=[\'"]?([^\'" >]+)', cvtToString)				
		regex = re.compile('\.jpg$|\.gif$|\.png$|\.pdf$|\.zip$', re.IGNORECASE)
		finalList = filter(lambda url: not regex.search(url), links)
		
		return finalList

	# --------------------------------------------------------------------------------------------------------------------------------------------------------------- #     
	def getBaseDomain(self, url):
		"""Gets the base domain of the given url """
		return urlparse.urlparse(url).netloc
		  
	# --------------------------------------------------------------------------------------------------------------------------------------------------------------- #     
	def removeNonBaseUrlLinks(self, urlList):
		"""Remove all non-baseurl links from the list """
		newList = []
		for i in urlList:
			checkBaseUrl = self.getBaseDomain(i)	
			if(checkBaseUrl == self.getBaseDomain(self.baseUrl)):				
				newList.append(i)		
		return newList	
	
	# --------------------------------------------------------------------------------------------------------------------------------------------------------------- # 	
	def makeFolder(self, folder):
	    """Make a folder """
	    os.mkdir(folder)   
	
	# --------------------------------------------------------------------------------------------------------------------------------------------------------------- #     
	def lineset(self, set):
		"""Simple output formatting """
		if(set == 1):
			out = colored('------------------------------------------------------------------------------------------', 'white', attrs=['bold'])
		else:
			out = ''
		return out

	# --------------------------------------------------------------------------------------------------------------------------------------------------------------- #     
	def removeFromList(self, list, item):
		"""Remove a give value from a list """
		answer = []
		for i in list:
			if i!=item:
				answer.append(i)
		return answer
		

# HELPER CLASSES
# --------------------------------------------------------------------------------------------------------------------------------------------------------------- #     

class fileWriter:
	"""This is log file writing class """
	# --------------------------------------------------------------------------------------------------------------------------------------------------------------- #     
	def __init__(self, stdout, filename):
		self.stdout = stdout
		self.logfile = file(filename, 'a')
		
	# --------------------------------------------------------------------------------------------------------------------------------------------------------------- #     
	def write(self, text):
		self.stdout.write(text)
		self.logfile.write(text)
		
	# --------------------------------------------------------------------------------------------------------------------------------------------------------------- #  
	def close(self):
		self.stdout.close()
		self.logfile.close() 
		

class NetworkCapture(object): 
    """This is the class used with selenium standalone to web profile pages """
    # --------------------------------------------------------------------------------------------------------------------------------------------------------------- #
    def __init__(self, xml_blob):
        self.xml_blob = xml_blob
        self.dom = etree.ElementTree(etree.fromstring(xml_blob))
        
    # --------------------------------------------------------------------------------------------------------------------------------------------------------------- #
    def get_json(self):
        results = []
        for child in self.dom.getiterator():
            if child.tag == 'entry':
                url = child.attrib.get('url')
                start_time = child.attrib.get('start')
                time_in_millis = child.attrib.get('timeInMillis')
                results.append((url, start_time, time_in_millis))
        return json.dumps(results)               
                
    # --------------------------------------------------------------------------------------------------------------------------------------------------------------- #    
    def get_content_size(self):  # total kb passed through the proxy  
        byte_sizes = []
        for child in self.dom.getiterator():
            if child.tag == 'entry':
                byte_sizes.append(child.attrib.get('bytes'))
        total_size = sum([int(bytes) for bytes in byte_sizes]) / 1000.0
        return total_size
    
    # --------------------------------------------------------------------------------------------------------------------------------------------------------------- #
    def get_num_requests(self):
        num_requests = 0
        for child in self.dom.getiterator():
            if child.tag == 'entry':
                num_requests += 1
        return num_requests
    
    # --------------------------------------------------------------------------------------------------------------------------------------------------------------- #
    def get_http_status_codes(self):       
        status_map = {}
        for child in self.dom.getiterator():
            if child.tag == 'entry':
                try:
                    status_map[child.attrib.get('statusCode')] += 1
                except KeyError:
                    status_map[child.attrib.get('statusCode')] = 1
        return status_map
    
    # --------------------------------------------------------------------------------------------------------------------------------------------------------------- #
    def get_http_details(self):
        http_details = []
        for child in self.dom.getiterator():
            if child.tag == 'entry':
                url = child.attrib.get('url') + '?'
                url_stem = url.split('?')[0]
                doc = '/' + url_stem.split('/')[-1]
                status = int(child.attrib.get('statusCode'))
                method = child.attrib.get('method').replace("'", '')
                size = int(child.attrib.get('bytes'))
                time = int(child.attrib.get('timeInMillis'))
                http_details.append((status, method, doc, size, time))
        http_details.sort(cmp=lambda x,y: cmp(x[3], y[3])) # sort by size
        return http_details
        
    # --------------------------------------------------------------------------------------------------------------------------------------------------------------- #    
    def get_file_extension_stats(self):
        file_extension_map = {}  # k=extension v=(count,size) 
        for child in self.dom.getiterator():
            if child.tag == 'entry':
                size = float(child.attrib.get('bytes')) / 1000.0
                url = child.attrib.get('url') + '?'
                url_stem = url.split('?')[0]
                doc = url_stem.split('/')[-1]
                if '.' in doc:
                    file_extension = doc.split('.')[-1]
                else:
                    file_extension = 'unknown'
                try:
                    file_extension_map[file_extension][0] += 1
                    file_extension_map[file_extension][1] += size
                except KeyError:
                    file_extension_map[file_extension] = [1, size]
        return file_extension_map
        
    # --------------------------------------------------------------------------------------------------------------------------------------------------------------- #    
    def get_network_times(self):
        timings = []
        start_times = []
        end_times = []
        for child in self.dom.getiterator():
            if child.tag == 'entry':
                timings.append(child.attrib.get('timeInMillis'))
                start_times.append(child.attrib.get('start')) 
                end_times.append(child.attrib.get('end'))
        start_times.sort()
        end_times.sort()
        start_first_request = self.convert_time(start_times[0])
        end_first_request = self.convert_time(end_times[0])
        end_last_request = self.convert_time(end_times[-1])
        return (start_first_request, end_first_request, end_last_request)
        
    # --------------------------------------------------------------------------------------------------------------------------------------------------------------- #    
    def convert_time(self, date_string):
        if '-' in date_string: split_char = '-'
        else: split_char = '+'
        dt = datetime.strptime(''.join(date_string.split(split_char)[:-1]), '%Y%m%dT%H:%M:%S.%f')    
        return dt

