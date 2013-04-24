#!/usr/bin/env python

################################################################################
## NAME: TEST ZUMIEZ MY BAG
## DATE: Oct 2011
## AUTHOR: Jason R Alexander
## MAIL: sunnysidesounds@gmail.com
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
import csv
import itertools
from datetime import datetime, timedelta


from selenium.webdriver.support.ui import WebDriverWait
from BeautifulSoup import BeautifulSoup


#MISC VALUES & FUNCTIONS
# --------------------------------------------------------------------------------------------------------------------------------------------------------

reviewXpath = '/html/body/div[4]/div/div[3]/div/div/form/div[2]/div/div[2]/ul/li[3]/a'
gigyaDivContainer = 'commentsDiv_Products'

gigyaStarRatingClass = 'gig-comments-rating'



# --------------------------------------------------------------------------------------------------------------------------------------------------------------- #
def getLinksFromCsv(file_name):
	"""Used to extract sku's from a csv file """
	attList = []
	logPath = '../log/'
	attFile = file_name
	reader = csv.reader(open(logPath +attFile+'.csv', "rb"))
	for row in reader:
		att = row[0]
		attList.append(att)
	return attList

# --------------------------------------------------------------------------------------------------------------------------------------------------------------- #
def getGIgyaContent(tag, attribute, attribute_name):
	listd = soup.findAll(tag, {attribute : attribute_name})
	dataList = []
	for data in listd:
		d = re.compile(r'<.*?>')
		value = d.sub('', str(data))
		dataList.append(value)
	return dataList



#START TESTS
# --------------------------------------------------------------------------------------------------------------------------------------------------------


linksList = getLinksFromCsv('local_links')


for links in linksList:

	#create a wapf instance
	wobj = wapf.wapf(config.baseUrl, config.browser)
	#get out browser instance
	browser = wobj.setBrowser(config.browser)

	#get base url from config
	#browser.get(links)
	browser.get('http://www.julep.com/shop/nail-color/alfre.html')
	#click the reviews link.
	reviewLinkClick = browser.find_element_by_xpath(reviewXpath).click()
	#user webdriver wait, to wait for the javascript returning html code.
	WebDriverWait(browser, timeout=10).until(
	    lambda x: x.find_element_by_id(gigyaDivContainer))
	#Get the page source
	page_source = browser.page_source
	soup = BeautifulSoup(page_source)


	titleList = getGIgyaContent("div", "class", "gig-comments-title")
	usernameList = getGIgyaContent("span", "class", "gig-comments-username gig-comments-comment-username")
	descriptionList = getGIgyaContent("div", "class", "gig-comments-comment-body")
	recommendedList = getGIgyaContent("div", "class", "gig-comments-vote-value")
	dateList = getGIgyaContent("span", "class", "gig-comments-comment-time")


	#gig-comments-comment-time

	#Get the title value of the rating div
	starList = soup.findAll("div", {"class" : "gig-comments-rating"})
	starNewList = []
	for star in starList:
		starNewList.append(str(star['title']))


	fbIDList = soup.findAll("div", {"class" : "gig-comments-photoImageSmall gig-comments-comment-photoImageSmall"})
	fbList = []
	for fbID in fbIDList:
		imgURL = fbID.find('img')['src']
		imgURL = imgURL.replace("http://graph.facebook.com/", "") 
		imgURL = imgURL.replace("/picture?type=square", "") 
		fbList.append(str(imgURL))


	sortList = list(zip(titleList, usernameList, descriptionList, starNewList, fbList, recommendedList, dateList))
	

	print "[title, username, description, star, fbID, recommend]"
	for data in sortList:
		print data


	"""
            <Review id="11" removed="false">
                <ModerationStatus>APPROVED</ModerationStatus>
                <UserProfileReference id="miketester112">
                    <ExternalId>miketester112</ExternalId>
                    <DisplayName>supermike</DisplayName>
                    <Anonymous>false</Anonymous>
                    <HyperlinkingEnabled>false</HyperlinkingEnabled>
                </UserProfileReference>
                <Title>Best product ever!</Title>
                <ReviewText>This product truly changed my life; I don't know what I'd do without it.</ReviewText>
                <Rating>5</Rating>
                <Recommended>true</Recommended>
                <ReviewerLocation>Austin, TX</ReviewerLocation>
                <SubmissionTime>2012-01-23T12:59:25.000-06:00</SubmissionTime>
                <Featured>false</Featured>
            </Review>
	"""	



	browser.close()

	sys.exit()




