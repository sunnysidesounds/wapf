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
import datetime
from random import choice
sys.path.append( os.path.join( os.getcwd(), '..' ) )
#custom modules
import wapf
import config
import csv
import itertools
from lxml import etree


from selenium.webdriver.support.ui import WebDriverWait
from BeautifulSoup import BeautifulSoup


#MISC VALUES & FUNCTIONS
# --------------------------------------------------------------------------------------------------------------------------------------------------------

reviewXpath = '/html/body/div[4]/div/div[3]/div/div/form/div[2]/div/div[2]/ul/li[3]/a'
gigyaDivContainer = 'commentsDiv_Products'
xmlFile = '../log/julep_reviews.xml'


# --------------------------------------------------------------------------------------------------------------------------------------------------------------- #
def cleanString(string):
    """This strips out all non-alphanumberic, html tags. Basically will leave just text """
    string = re.sub(r'[^\w\s]','', string)
    string = re.sub( '\s+', ' ', string ).strip()
    return string

# --------------------------------------------------------------------------------------------------------------------------------------------------------------- #
def utlFileExists(filepath):
    """Checks to see if a file exists """
    fileExists = os.path.exists(filepath)
    if(fileExists == True):
        os.remove(filepath)
        file_create = open(filepath, 'w')
        file_create.write('')
        file_create.close()
    else:
        #Create a blank file.
        file_create = open(filepath, 'w')
        file_create.write('')
        file_create.close()


# --------------------------------------------------------------------------------------------------------------------------------------------------------------- #
def getLinksFromCsv(file_name):
	"""Used to extract sku's from a csv file """
	attList = []
	logPath = '../log/'
	attFile = file_name
	reader = csv.reader(open(logPath +attFile+'.csv', "rb"))
	for row in reader:
		attList.append(row)
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



# EXTRACT PAGE DATA AND BUILD XML
# --------------------------------------------------------------------------------------------------------------------------------------------------------

start_script = datetime.datetime.now()

utlFileExists(xmlFile)


feed = etree.Element("Feed")
feed.set("name", "Julep")
feed.set("extractDate", str(start_script.isoformat()))
feed.set("xmlns", "http://www.bazaarvoice.com/xs/PRR/StandardClientFeed/5.6")

count = 0
linksList = getLinksFromCsv('utility_links')
for d in linksList:

	pid = d[0] # Our product / entity_id
	purl = d[1] # Our product url

	#create a wapf instance
	wobj = wapf.wapf(config.baseUrl, config.browser)
	#get out browser instance
	browser = wobj.setBrowser(config.browser)

	#get base url from config
	browser.get(purl)
	#browser.get('http://www.julep.com/intro-box-it.html')
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

	#Get the title value of the rating div
	starList = soup.findAll("div", {"class" : "gig-comments-rating"})
	starNewList = []
	for star in starList:
		starNewList.append(str(star['title']))

	#Get facebook ID's
	fbIDList = soup.findAll("div", {"class" : "gig-comments-photoImageSmall gig-comments-comment-photoImageSmall"})
	fbList = []
	for fbID in fbIDList:
		imgURL = fbID.find('img')['src']
		imgURL = imgURL.replace("http://graph.facebook.com/", "") 
		imgURL = imgURL.replace("/picture?type=square", "") 
		fbList.append(str(imgURL))

	sortList = list(zip(titleList, usernameList, descriptionList, starNewList, fbList, recommendedList, dateList))
	
	if(len(sortList) != 0):
		print "EXTRACTING REVIEW DATA FROM: " + purl + " (" + str(len(sortList)) + ")"

		product = etree.SubElement(feed, "Product")
		product.set("id", pid)
		external_id = etree.SubElement(product, "ExternalId")
		external_id.text = pid

		reviews = etree.SubElement(product, "Reviews")
		review_id = 1
		for data in sortList:
			
			rtitle = data[0]
			rusername = data[1]
			rdescription = data[2]
			rstar = data[3]
			rfb = data[4]
			rrecommend = data[5]

			review = etree.SubElement(reviews, "Review")
			review.set("id", str(review_id))
			review.set("removed", "false")
			moderation_status = etree.SubElement(review, "ModerationStatus")
			moderation_status.text = "APPROVED"
			user_profile_reference = etree.SubElement(review, "UserProfileReference")
			user_profile_reference.set("id", rfb)
			user_external_id = etree.SubElement(user_profile_reference, "ExternalId")
			user_external_id.text = rfb
			display_name = etree.SubElement(user_profile_reference, "DisplayName")
			display_name.text = cleanString(rusername)
			anonymous = etree.SubElement(user_profile_reference, "Anonymous")
			anonymous.text = "false"
			hyper_linking_enabled = etree.SubElement(user_profile_reference, "HyperlinkingEnabled")
			hyper_linking_enabled.text = "false"

			review_title = etree.SubElement(review, "Title")
			review_title.text = etree.CDATA(cleanString(rtitle))
			review_text = etree.SubElement(review, "ReviewText")
			review_text.text = etree.CDATA(cleanString(rdescription))
			ratings = etree.SubElement(review, "Rating")
			ratings.text = rstar

			recommended = etree.SubElement(review, "Recommended")
			
			if(rrecommend == '0'):
				recommended_value = "false"
			else:
				recommended_value = "true"
			recommended.text = recommended_value

			featured = etree.SubElement(review, "Featured")
			featured.text = "false"

			review_id = review_id + 1


		
		count = count + 1
		browser.close()
	else:
		print "NO REVIEW DATA FROM: " + purl
		count = count + 1
		browser.close()
		continue


print "WRITING XML FILE: " + xmlFile

with open(xmlFile,'w') as f:
	f.write(etree.tostring(feed, pretty_print=True, xml_declaration=True, encoding="utf-8"))


"""
	# QUERY TO GRAB ID AND PRODUCT URL
            SELECT cpe.entity_id as external_id,CONCAT('http://www.julep.com/', cpev_purl.value) as product_page_url
            FROM catalog_product_entity cpe
            LEFT JOIN cataloginventory_stock_status css  ON cpe.entity_id = css.product_id            
            LEFT JOIN catalog_product_entity_varchar cpev_purl ON cpe.entity_id = cpev_purl.entity_id AND cpev_purl.attribute_id = 98 AND cpev_purl.store_id = 0
            LEFT JOIN catalog_category_product cpee ON cpe.entity_id = cpee.product_id
            LEFT JOIN catalog_product_entity_int cpei_status ON cpe.entity_id = cpei_status.entity_id AND cpei_status.attribute_id = 96
            LEFT JOIN catalog_product_entity_int cpei_vis ON cpe.entity_id = cpei_vis.entity_id AND cpei_vis.attribute_id = 102
            WHERE css.stock_status = 1 AND cpei_status.value = 1 AND cpei_vis.value = 4 GROUP BY cpe.entity_id;

"""





