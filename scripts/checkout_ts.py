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
sys.path.append( os.path.join( os.getcwd(), '..' ) )

import wapf

#TODO: Implement validation per page
#TODO: Implement a bettwe screenshot feature
#TODO: Make this more dynamic, this is pretty much a static function


#Config Values
browser = 'firefox'
baseUrl = 'http://www.zumiez.com'
enableScreenshot = 0
enableWrite = 1
enableMultiple = 1

#The Step Through Values - 1 Item
step1 = 'http://www.zumiez.com/shoes/guys-shoes/adidas-ciero-black-and-white-shoe.html' #select a shoe
step2 = 'tile-455' # selecting size 7
step3 = 'pdp-add-to-bag-button' # Add to cart
step4 = 'http://www.zumiez.com/checkout/cart/' #Go to your cart
step5 = 'https://www.zumiez.com/modcheckout/multipage/step1' #checkout step1
step6 = 'https://www.zumiez.com/modcheckout/multipage/step1Post/' # Fill out contact information and submit
step7 = '/html/body/div[2]/div/div[2]/div/div[3]/form/table/tbody/tr/td/input' #select free shipping
step8 = '/html/body/div[2]/div/div[2]/div/div[4]/div/div/div[2]/input' #Submit free shipping
step9 = 'https://www.zumiez.com/modcheckout/multipage/step3'  #Fill out credit card information
step10 = '/html/body/div[2]/div/div[2]/div/div[4]/div/div[3]/div[5]/input' #Submit credit card information

#The Step Through Values - Multiple Items


#The Form Values
firstName = 'Jason'
lastName = 'Alexander'
company = 'Zumiez Web Team'
addressOne = '6300 Merrill Creek'
city = 'Everett'
state = 'Washington'
zip = '98052'
phone = '415-690-3590'
email = 'JasonAlexander@zumiez.com'
ccName = 'Jason R Alexander'
ccNumber = '4111111111111111'
ccType = 'Visa'
ccMonth = '12'
ccYear = '2014'
ccCode = '111'


#create class instance
tobj = wapf.wapf(baseUrl, browser) #init baseUrl and browser
#get browser driver
dvr = tobj.setBrowser(browser)


if(enableMultiple == 1):
    ### LOGIC - Multiple Items ###
    tobj.setHeaderMessage('Checkout Test - Multiple Items', enableWrite)
    
    
    

else:
    ### LOGIC - 1 Items ###
    tobj.setHeaderMessage('Checkout Test - 1 Items', enableWrite)
    
    #STEP 1
    dvr.get(step1)
    tobj.printMessage(' -Getting: ' + step1, enableWrite)
    
    if(enableScreenshot == 1):
        tobj.formattedScreenshot(step1, 'checkout_one_item', enableWrite)
    
    #STEP 2
    tobj.clickByID(step2, enableWrite)
    #STEP 3
    tobj.clickByID(step3, enableWrite)
    
    #STEP 4
    tobj.printMessage(' -Waiting for element to become visible.', enableWrite)
    #Let's wait for the element to become visible
    tobj.browserDriver.implicitly_wait(10)
    
    getLink = None
    #Wait for link to become visible
    while(getLink is None):
        try:
            getLink = tobj.clickByLink(step4, enableWrite)
            if(enableScreenshot == 1):
                tobj.formattedScreenshot(step4, 'checkout_one_item', enableWrite)
            break
        except:
            tobj.printMessage(' -Waiting for element to become visible.', enableWrite)
            pass
    
    #STEP 5
    tobj.clickByLink(step5, enableWrite)
    if(enableScreenshot == 1):
        tobj.formattedScreenshot(step5, 'checkout_one_item', enableWrite)
    
    #STEP 6
    tobj.fillInputByID("first_name", firstName, enableWrite)
    tobj.fillInputByID("last_name", lastName, enableWrite)
    tobj.fillInputByID("company_name", company, enableWrite)
    tobj.fillInputByID("address1", addressOne, enableWrite)
    tobj.fillInputByID("city", city, enableWrite)
    tobj.fillInputByID("state", state, enableWrite)
    tobj.fillInputByID("postal_code", zip, enableWrite)
    tobj.fillInputByID("primary_phone", phone, enableWrite)
    tobj.fillInputByID("email", email, enableWrite)
    
    if(enableScreenshot == 1):
        tobj.formattedScreenshot(step6, 'checkout_one_item', enableWrite)
    tobj.clickByLink(step6, enableWrite)
    
    #This is to resolve a firefox bug
    dvr.switch_to_default_content()
    
    #STEP 7
    #Click radio button
    tobj.clickByXPath(step7, enableWrite)
    
    #STEP 8
    #Click next button
    tobj.clickByXPath(step8, enableWrite)
    
    #STEP 9
    #Fill out credit card
    tobj.fillInputByID("full_name", ccName, enableWrite)
    tobj.fillInputByID("card_type", ccType, enableWrite)
    tobj.fillInputByID("card_number", ccNumber, enableWrite)
    tobj.fillInputByID("card_month", ccMonth, enableWrite)
    tobj.fillInputByID("card_year", ccYear, enableWrite)	    
    tobj.fillInputByName("card_cvNumber", ccCode, enableWrite)
    
    if(enableScreenshot == 1):
        tobj.formattedScreenshot(step9, 'checkout_one_item', enableWrite)
    
    #Submit credit card
    tobj.clickByXPath(step10, enableWrite)
    tobj.printMessage('Done with testing Checkout!!', enableWrite)



"""
today = time.strftime("%m-%d-%Y at %H:%M")
    writeMessage = enableWrite
    
    #The Step Through
    stepTh_1 = 'http://www.zumiez.com/kr3w-manchester-charcoal-and-black-jacket.html'
    stepTh_2 = 'tile-410'
    stepTh_3 = 'pdp-add-to-bag-button' # Global don't need to change
    stepTh_4 = 'http://www.zumiez.com/young-and-reckless-drama-beats-repeat-black-tee-shirt.html'
    stepTh_5 = 'http://www.zumiez.com/checkout/cart/'
    stepTh_6 = 'https://www.zumiez.com/modcheckout/multipage/step1'
    stepTh_7 = 'https://www.zumiez.com/modcheckout/multipage/step1Post/'
    shipping = '/html/body/div[2]/div/div[2]/div/div[3]/form/table/tbody/tr/td/input'
    nextShippingButton = '/html/body/div[2]/div/div[2]/div/div[4]/div/div/div[2]/input'
    placeOrderButton = '/html/body/div[2]/div/div[2]/div/div[4]/div/div[3]/div[5]/input'
    
    
    self.printMessage('Testing with ' + self.browser + ' on ' +str(today), writeMessage) 
    self.printMessage('Start url is: [' + baseUrl + ']', writeMessage)
    
    
    self.browserDriver.get(stepTh_1)
    self.printMessage(' -Getting: ' + stepTh_1, writeMessage)
    if(enableScreenshot == 1):
        self.formattedScreenshot(stepTh_4, 'checkout_multiple_test', writeMessage)
    
    self.clickByID(stepTh_2, writeMessage)
    self.clickByID(stepTh_3, writeMessage)
    
    self.printMessage(' -Waiting for element to become visible.', writeMessage)
    #Fix
    time.sleep(10)
    self.browserDriver.get(stepTh_4)
    
    self.clickByID(stepTh_2, writeMessage)
    self.clickByID(stepTh_3, writeMessage)
    
    self.printMessage(' -Waiting for element to become visible.', writeMessage)
    #Fix
    time.sleep(10)
    self.clickByLink(stepTh_5, writeMessage)
    self.clickByLink(stepTh_6, writeMessage)
    
    #Fill out form step 1
    self.fillInputByID("first_name", firstName, writeMessage)
    self.fillInputByID("last_name", lastName, writeMessage)
    self.fillInputByID("company_name", company, writeMessage)
    self.fillInputByID("address1", addressOne, writeMessage)
    self.fillInputByID("city", city, writeMessage)
    self.fillInputByID("state", state, writeMessage)
    self.fillInputByID("postal_code", zip, writeMessage)
    self.fillInputByID("primary_phone", phone, writeMessage)
    self.fillInputByID("email", email, writeMessage)
    
    self.clickByLink(stepTh_7, writeMessage)
    #This is to resolve a firefox bug
    self.browserDriver.switch_to_default_content()
    #Click radio button
    self.clickByXPath(shipping, writeMessage)
    #Click next button
    self.clickByXPath(nextShippingButton, writeMessage)
		"""


