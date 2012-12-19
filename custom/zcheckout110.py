#!/usr/bin/env python

################################################################################
## NAME: TEST ZUMIEZ CHECKOUT
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
from termcolor import colored
sys.path.append( os.path.join( os.getcwd(), '..' ) )
#custom modules
import wapf
import config 


#MISC VALUES & FUNCTIONS
# --------------------------------------------------------------------------------------------------------------------------------------------------------

productClickList = []
shippingClickList = []
#container id of size div
sizeDivId = 'size-option-grid-values'
addToBagID = 'zumiez-add-to-bag'
viewBagText = 'View Bag'
cartCheckout = 'div.cart div.page-title button.button'
zcustomFileName = 'zumiez_checkout'
messageErrorClass = 'error-msg'
messageClass = 'ul.messages'
matchNoProductUrl = 'http://www.zumiez.com/catalogsearch/result'

def removeFromList(the_list, match):
	"""Used for removing color and size: tile- tags """
	newlist = []
	for item in the_list:
		if item.startswith(match):
			continue
		else:
			newlist.append(item)
	return newlist

def getSkusFromFile(file_name):
	"""Used to extract sku's line by line and put them into a list """
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
	return skuList
			
#Little list for simple testing
productSkuList = ['193824', '196553', '199084']
#Full list of skus from file
#productSkuList = getSkusFromFile("active_product_configurables")


#CHECKOUT STEP 1 VALUES & FUNCTIONS
# --------------------------------------------------------------------------------------------------------------------------------------------------------
firstName = 'John'
lastName = 'Developer'
company = 'Zumiez.com'
address = '123 Alpha Street'
city = 'Redmond'
state = 'Washington'
zipcode = '98052'
phone = '123-456-5656'
email = 'developer@zumiez.com'


#CHECKOUT STEP 2 VALUES & FUNCTIONS
# --------------------------------------------------------------------------------------------------------------------------------------------------------
shippingClickLibrary = {'tablerateeconomy_bestway': '/html/body/div[2]/div/div[2]/div/div[3]/form/table/tbody/tr[2]/td/input', 
									'tableratestandard_bestway':'/html/body/div[2]/div/div[2]/div/div[3]/form/table/tbody/tr[3]/td/input', 
									'tablerateexpress_bestway':'/html/body/div[2]/div/div[2]/div/div[3]/form/table/tbody/tr[4]/td/input', 
									'tableratenextday_bestway':'/html/body/div[2]/div/div[2]/div/div[3]/form/table/tbody/tr[5]/td/input'}


#CHECKOUT STEP 3 VALUES & FUNCTIONS
# --------------------------------------------------------------------------------------------------------------------------------------------------------
setPaymentOption = 'cc'
fullName = firstName + ' ' + lastName
cardSelectionID = "fieldset dl#checkout-payment-method-load.sp-methods dl#checkout-payment-method-load.sp-methods dt.p_method input#p_method_cybersource_soap.radio"
cardType = 'Visa'
cardNumber = '4111111111111111'
cardMonth = '12'
cardYear = '2014'
securityNumber = '111'

def creditcard():
	"""Used to fill out credit card form """
	#Full Name
	clearFN = browser.find_element_by_id("full_name").clear()
	fillFN = browser.find_element_by_id("full_name").send_keys(fullName)
	wobj.message('Inputing values: ' + fullName , config.customFileName + zcustomFileName)
	#Card number
	fillCN = browser.find_element_by_id("card_type").send_keys(cardType)
	wobj.message('Inputing values: ' + cardType , config.customFileName + zcustomFileName)
	#Card Number
	clearCN = browser.find_element_by_id("card_number").clear()
	fillCN = browser.find_element_by_id("card_number").send_keys(cardNumber)
	wobj.message('Inputing values: ' + cardNumber , config.customFileName + zcustomFileName)
	#Card Month
	fillCM = browser.find_element_by_id("card_month").send_keys(cardMonth)
	wobj.message('Inputing values: ' + cardMonth , config.customFileName + zcustomFileName)
	#Card Year
	fillCY = browser.find_element_by_id("card_year").send_keys(cardYear)
	wobj.message('Inputing values: ' + cardYear , config.customFileName + zcustomFileName)	
	#Card Code
	clearCT = browser.find_element_by_name("card_cvNumber").clear()
	fillCT = browser.find_element_by_name("card_cvNumber").send_keys(securityNumber)
	wobj.message('Inputing values: ' + securityNumber , config.customFileName + zcustomFileName)	

def giftcard():
	"""Used to fill out gift card form """	
	print 'Execute Gift Card'

def paypal():
	"""Used to fill out paypal form """
	print 'Execute Paypal'

#Payment function list
paymentOptionList = {"gift":giftcard, "cc": creditcard, "pp": paypal}


#START TESTS
# --------------------------------------------------------------------------------------------------------------------------------------------------------

#TODO: Make this loop better
#Loop out each product
for productSku in productSkuList:
	#get random product from list
	productSku = choice(productSkuList)

	#create a wapf instance
	wobj = wapf.wapf(config.baseUrl, config.browser)
	#get out browser instance
	browser = wobj.setBrowser(config.browser)
	print colored('TESTING CHECKOUT WITH PRODUCT SKU: ' + productSku, 'blue', attrs=['bold'])
	print ''
	wobj.message('Test date: ' + config.systemDates, config.customFileName + zcustomFileName)
	wobj.message('Creating wapf and selenium instances...', config.customFileName + zcustomFileName)
	#get base url from config
	browser.get(config.baseUrl)
	wobj.message('Checking base url...', config.customFileName + zcustomFileName)
	
	wobj.message("Getting base url metrics: " + config.baseUrl, config.customFileName + zcustomFileName)
	wobj.message(wobj.httpRequestProfiler(config.baseUrl), config.customFileName + zcustomFileName)
	
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
	wobj.message('Going to system url...', config.customFileName + zcustomFileName)
	#Product Page metrics
	wobj.message("Getting system url metrics: " + currentUrl, config.customFileName + zcustomFileName)
	wobj.message(wobj.httpRequestProfiler(currentUrl), config.customFileName + zcustomFileName)		
	wobj.message('Getting product: ' + wobj.getPageTitle(currentUrl), config.customFileName + zcustomFileName)

	wobj.message('Verifing sizes are element is present... ', config.customFileName + zcustomFileName)
	if(wobj.isElementPresent(sizeDivId, browser)):
		wobj.message('Size element is present!', config.customFileName + zcustomFileName)
		linkIDs = browser.find_elements_by_class_name("select-grid-value")
		wobj.message('Determining what sizes we have...', config.customFileName + zcustomFileName)
		for link in linkIDs:
			#get the id's of these class
			getIDs = link.get_attribute('id')
			productClickList.append(getIDs)

		#display all link id for size, for easy debugging	
		formatList = ', '.join(productClickList)
		wobj.message('We have the following size link id(s): ' + formatList, config.customFileName + zcustomFileName)
		#Check for multiple sizes
		if(len(productClickList) != 1):	
			randomLinkID = choice(productClickList)	
						
			try:
				wobj.message('Picking a random size value, it\'s link id is: ' + randomLinkID, config.customFileName + zcustomFileName)
				#click a random size link
				clickRandomLink = browser.find_element_by_id(randomLinkID).click()
			except:
				wobj.message('Error with picking this size value: ' + randomLinkID, config.customFileName + zcustomFileName)
				randomLinkIDs = choice(productClickList)
				try:
					wobj.message('Picking another random size, it\'s link id is: ' + randomLinkIDs, config.customFileName + zcustomFileName)
					clickRandomLink = browser.find_element_by_id(randomLinkIDs).click()
				except:
					wobj.message('Error with trying to pick a random size for the second time...', config.customFileName + zcustomFileName)
					errorUrl = browser.current_url
					wobj.message('Error page: ' + errorUrl, config.customFileName + zcustomFileName)
					wobj.message('Starting over...', config.customFileName + zcustomFileName)
					print colored('Failed!  [' + productSku + ']', 'red', attrs=['bold']) 
					wobj.message(' ', config.customFileName + zcustomFileName)
					browser.close()
					continue					
			
			wobj.message('Click size link...', config.customFileName + zcustomFileName)
			#Clearing product size list for next pass of loop
			productClickList[:] = []		
		else:
			wobj.message('We only have one size...', config.customFileName + zcustomFileName)	
	else:
		wobj.message('Size element is not present, try to add product to bag...', config.customFileName + zcustomFileName)
		
	
	try:
		#add it to bag
		clickAddToBag = browser.find_element_by_id(addToBagID).click()
		wobj.message('Adding product to My Bag...', config.customFileName + zcustomFileName)
		#Let's wait for the dropdown slider to be visible before we click ...	
		browser.implicitly_wait(10)
	except:
		wobj.message('Error with trying to add this product to My Bag...', config.customFileName + zcustomFileName)
		errorUrl = browser.current_url
		if(errorUrl.startswith(matchNoProductUrl)):
			wobj.message('Error: "There are no products matching the selection" ', config.customFileName + zcustomFileName)
		else:
			wobj.message('Error/Known Bug: "Returns bad formatted url, missing /catalogsearch/result from url" ', config.customFileName + zcustomFileName)
		
		wobj.message('Error page: ' + errorUrl, config.customFileName + zcustomFileName)
		wobj.message('Starting over...', config.customFileName + zcustomFileName)
		print colored('Failed!  [' + productSku + ']', 'red', attrs=['bold'])
		wobj.message(' ', config.customFileName + zcustomFileName)
		browser.close()
		continue

	#click view bag
	try:
		clickViewBag = browser.find_element_by_link_text(viewBagText).click()
		wobj.message('Clicking View Bag from the dropdown slider...', config.customFileName + zcustomFileName)
	except:
		wobj.message('Error with clicking View Bag from the dropdown slider...', config.customFileName + zcustomFileName)
		try:
			wobj.message('Trying to click View Bag again from the dropdown slider...', config.customFileName + zcustomFileName)
			clickViewBag = browser.find_element_by_link_text(viewBagText).click()
		except:
			wobj.message('Error with trying to click View Bag for the second time...', config.customFileName + zcustomFileName)
			errorUrl = browser.current_url
			wobj.message('Error page: ' + errorUrl, config.customFileName + zcustomFileName)
			wobj.message('Starting over...', config.customFileName + zcustomFileName)
			print colored('Failed!  [' + productSku + ']', 'red', attrs=['bold'])
			wobj.message(' ', config.customFileName + zcustomFileName)
			browser.close()
			continue	

	#running profiler on my bag
	currentUrlBag = browser.current_url	
	wobj.message("Getting My Bag url metrics: " + currentUrlBag, config.customFileName + zcustomFileName)
	wobj.message(wobj.httpRequestProfiler(currentUrlBag), config.customFileName + zcustomFileName)	

	wobj.message('Product in My Bag: [sku:' + productSku + '] ' + wobj.getPageTitle(currentUrl), config.customFileName + zcustomFileName) #TODO: Change these productSku

	#click "Checkout" from My Bag
	clickCartCheckout = browser.find_element_by_css_selector(cartCheckout).click()
	wobj.message('Clicking checkout button from My Bag...', config.customFileName + zcustomFileName)

	wobj.message('Starting ONEPAGE checkout process...', config.customFileName + zcustomFileName)
	

	#STEP 1
	#let's fill out step 1 of checkout
	print colored('STEP 1 Billing Information', 'blue', attrs=['bold'])
	wobj.message('Filling out Billing Information of ONEPAGE checkout...', config.customFileName + zcustomFileName)
	#First Name
	clearFirst = browser.find_element_by_id("billing:firstname").clear()
	fillFirst = browser.find_element_by_id("billing:firstname").send_keys(firstName)
	wobj.message('Inputing values: ' + firstName , config.customFileName + zcustomFileName)
	#Last Name
	clearLast = browser.find_element_by_id("billing:lastname").clear()
	fillLast = browser.find_element_by_id("billing:lastname").send_keys(lastName)
	wobj.message('Inputing values: ' + lastName , config.customFileName + zcustomFileName)
	#Company
	clearCompany = browser.find_element_by_id("billing:company").clear()
	fillCompany = browser.find_element_by_id("billing:company").send_keys(company)
	wobj.message('Inputing values: ' + company , config.customFileName + zcustomFileName)
	#Address
	clearAddress = browser.find_element_by_id("billing:street1").clear()
	fillAddress = browser.find_element_by_id("billing:street1").send_keys(address)
	wobj.message('Inputing values: ' + address , config.customFileName + zcustomFileName)
	#City
	clearCity = browser.find_element_by_id("billing:city").clear()
	fillCity = browser.find_element_by_id("billing:city").send_keys(city)
	wobj.message('Inputing values: ' + city , config.customFileName + zcustomFileName)
	#State (select)
	fillState = browser.find_element_by_id("billing:region_id").send_keys(state)
	wobj.message('Inputing values: ' + state , config.customFileName + zcustomFileName)
	#Zip
	clearZip = browser.find_element_by_id("billing:postcode").clear()
	fillZip = browser.find_element_by_id("billing:postcode").send_keys(zipcode)
	wobj.message('Inputing values: ' + zipcode , config.customFileName + zcustomFileName)
	#phone
	clearPhone = browser.find_element_by_id("billing:telephone").clear()
	fillPhone = browser.find_element_by_id("billing:telephone").send_keys(phone)
	wobj.message('Inputing values: ' + phone , config.customFileName + zcustomFileName)
	#email
	clearEmail = browser.find_element_by_id("billing:email").clear()
	fillEmail = browser.find_element_by_id("billing:email").send_keys(email)
	wobj.message('Inputing values: ' + email , config.customFileName + zcustomFileName)
	#Next button
	browser.find_element_by_css_selector("button#step1SubmitButton.button").click()
	wobj.message('Click Continue button, Please wait...' , config.customFileName + zcustomFileName)


	#STEP 2
	#let's fill out step 2 of checkout
	print colored('STEP 2 Shipping Information:', 'blue', attrs=['bold'])
	wobj.message('Filling out Shipping Information of ONEPAGE checkout...', config.customFileName + zcustomFileName)
	browser.implicitly_wait(10)
	

	#STEP 3
	#let's fill out step 3 of checkout
	print colored('STEP 3 Shipping Method:', 'blue', attrs=['bold'])
	wobj.message('Filling out Shipping Method of ONEPAGE checkout...', config.customFileName + zcustomFileName)
	browser.find_element_by_css_selector("input#s_method_matrixrate_matrixrate_1681.radio").click()
	wobj.message('Picking Standard Shipping... ', config.customFileName + zcustomFileName)
	#Next button
	browser.find_element_by_css_selector("div#shipping-method-buttons-container.buttons-set button.button").click()
	wobj.message('Click Continue button, Please wait...' , config.customFileName + zcustomFileName)
	browser.implicitly_wait(10)

	#STEP 4
	#let's fill out step 4 of checkout
	print colored('CHECKOUT STEP 3:', 'blue', attrs=['bold'])
	wobj.message('Filling out step 3 of checkout...', config.customFileName + zcustomFileName)
	wobj.message('Filling out Payment Information of ONEPAGE checkout...', config.customFileName + zcustomFileName)
	browser.implicitly_wait(10)
	
	browser.find_element_by_css_selector(cardSelectionID).click()
	wobj.message('Picking Credit Card for payment method', config.customFileName + zcustomFileName)
	
	#Credit Card (select)
	fillState = browser.find_element_by_id("cybersource_soap_cc_type").send_keys(cardType)
	wobj.message('Inputing values: ' + cardType , config.customFileName + zcustomFileName)
	#Credit Card Number
	fillState = browser.find_element_by_id("cybersource_soap_cc_number").send_keys(cardNumber)
	wobj.message('Inputing values: ' + cardNumber , config.customFileName + zcustomFileName)
	#Credit Card Expire Month
	fillState = browser.find_element_by_id("cybersource_soap_expiration").send_keys(cardMonth)
	wobj.message('Inputing values: ' + cardMonth , config.customFileName + zcustomFileName)
	#Credit Card Expire Year
	fillState = browser.find_element_by_id("cybersource_soap_expiration_yr").send_keys(cardYear)
	wobj.message('Inputing values: ' + cardYear , config.customFileName + zcustomFileName)
	#Credit Card Code
	fillState = browser.find_element_by_id("cybersource_soap_cc_cid").send_keys(securityNumber)
	wobj.message('Inputing values: ' + securityNumber , config.customFileName + zcustomFileName)
	#Next button
	browser.find_element_by_css_selector("div#payment-buttons-container.buttons-set button.button").click()
	wobj.message('Click Continue button, Please wait...' , config.customFileName + zcustomFileName)
	browser.implicitly_wait(10)
	#Place Order
	browser.find_element_by_css_selector("div#review-buttons-container.buttons-set button.button").click()
	wobj.message('Placing order now... ', config.customFileName + zcustomFileName)
	browser.implicitly_wait(20)

	#add some ending space
	wobj.message(' ', config.customFileName + zcustomFileName)
	#browser.close()


	sys.exit()

