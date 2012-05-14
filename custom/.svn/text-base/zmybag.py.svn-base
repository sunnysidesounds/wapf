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


#MISC VALUES & FUNCTIONS
# --------------------------------------------------------------------------------------------------------------------------------------------------------
productSkuList = ['188028']
productClickList = []
shippingClickList = []
#container id of size div
sizeDivId = 'pdp-detail-size-select'
addToBagID = 'pdp-add-to-bag-button'
viewBagText = 'View Bag'
cartCheckout = '#cart-group-links > a > img.hover'
zcustomFileName = 'zumiez_checkout'
messageErrorClass = 'error-msg'
messageClass = 'ul.messages'

def removeFromList(the_list, match):
	newlist = []
	for item in the_list:
		if item.startswith(match):
			continue
		else:
			newlist.append(item)
	return newlist



#START TESTS
# --------------------------------------------------------------------------------------------------------------------------------------------------------

#Loop out each product
for productSku in productSkuList:

	#create a wapf instance
	wobj = wapf.wapf(config.baseUrl, config.browser)
	#get out browser instance
	browser = wobj.setBrowser(config.browser)
	wobj.message('Test date: ' + config.systemDates, config.customFileName + zcustomFileName)
	wobj.message('Creating wapf and selenium instances...', config.customFileName + zcustomFileName)
	#get base url from config
	browser.get(config.baseUrl)
	wobj.message('Checking base url...', config.customFileName + zcustomFileName)
	#get search box element
	browser.find_element_by_name("q").clear()
	#enter our product id
	#TODO: Add full string search
	browser.find_element_by_name("q").send_keys(productSku) #TODO: Change these productSku
	wobj.message('Searching for product with sku: ' + productSku, config.customFileName + zcustomFileName)
	#Click submit
	browser.find_element_by_css_selector("input.hover").click()
	wobj.message('Submitting search... ', config.customFileName + zcustomFileName)
	
	currentUrl = browser.current_url
	wobj.message('Going to system url: ' + currentUrl, config.customFileName + zcustomFileName)
	wobj.message('Getting product: ' + wobj.getPageTitle(currentUrl), config.customFileName + zcustomFileName)
	
	#Verify that the size div id is visble on the page.
	wobj.message('Verifing if size element is present... ', config.customFileName + zcustomFileName)
	if(wobj.isElementPresent(sizeDivId, browser)):	
		wobj.message('Size element is present!', config.customFileName + zcustomFileName)
		#get all size links
		linkIDs = browser.find_elements_by_class_name("tile")
		wobj.message('Determining what sizes we have...', config.customFileName + zcustomFileName)
		for link in linkIDs:
			#get the id's of these class
			getIDs = link.get_attribute('id')
			#add them to a list
			productClickList.append(getIDs)	
		#remove first item as it's the color attribute
		filterProductClickList = removeFromList(productClickList, "tile-000")
		productClickList = filterProductClickList
		#display all link id for size, for easy debugging	
		formatList = ', '.join(productClickList)
		wobj.message('We have the following size link id(s): ' + formatList, config.customFileName + zcustomFileName)
		
		if(len(productClickList) != 1):	
			randomLinkID = choice(productClickList)	
						
			try:
				wobj.message('Picking a random size value, it\'s link id is: ' + randomLinkID, config.customFileName + zcustomFileName)
				#click a random size link
				clickRandomLink = browser.find_element_by_id(randomLinkID).click()
			except:
				wobj.message('Error with picking this size value: ' + randomLinkID, config.customFileName + zcustomFileName)
				randomLinkIDs = choice(productClickList)
				wobj.message('Picking another random size, it\'s link id is: ' + randomLinkIDs, config.customFileName + zcustomFileName)
				clickRandomLink = browser.find_element_by_id(randomLinkIDs).click()
			
			
			wobj.message('Click size link...', config.customFileName + zcustomFileName)
			#Clearing product size list for next pass of loop
			productClickList[:] = []		
		else:
			wobj.message('We only have one size...', config.customFileName + zcustomFileName)
			
	#else if there is no size div id
	else:
		wobj.message('Size element is not present, try to add product to bag...', config.customFileName + zcustomFileName)
	
	#add it to bag
	clickAddToBag = browser.find_element_by_id(addToBagID).click()
	wobj.message('Adding product to My Bag...', config.customFileName + zcustomFileName)
	#Let's wait for the dropdown slider to be visible before we click ...
	browser.implicitly_wait(10)
	
	#click view bag
	try:
		clickViewBag = browser.find_element_by_link_text(viewBagText).click()
		wobj.message('Clicking View Bag from the dropdown slider...', config.customFileName + zcustomFileName)
	except:
		wobj.message('Error with clicking View Bag from the dropdown slider...', config.customFileName + zcustomFileName)
		wobj.message('Trying to click View Bag again from the dropdown slider...', config.customFileName + zcustomFileName)
		clickViewBag = browser.find_element_by_link_text(viewBagText).click()
	
	
	
	
	wobj.message('Product in My Bag: [sku:' + productSku + '] ' + wobj.getPageTitle(currentUrl), config.customFileName + zcustomFileName) #TODO: Change these productSku
	#click "Checkout" from My Bag
	
	#add some ending space
	wobj.message(' ', config.customFileName + zcustomFileName)
#	browser.close()



