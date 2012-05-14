#!/usr/bin/env python

################################################################################
## NAME: EMAIL TEST EXAMPLE
## DATE: Nov 2011
## AUTHOR: Jason R Alexander
################################################################################


import sys
import os
import smtplib
import mimetypes
sys.path.append( os.path.join( os.getcwd(), '..' ) )
import wapf
import string
 
SUBJECT = "Test email from Python"
TO = "jasonralexander@gmail.com"
FROM = "developer@zumiez.com"
text = "blah blah blah"
BODY = string.join((
        "From: %s" % FROM,
        "To: %s" % TO,
        "Subject: %s" % SUBJECT ,
        "",
        text
        ), "\r\n")
server = smtplib.SMTP(HOST)
server.sendmail(FROM, [TO], BODY)
server.quit()






"""
def  emailAlert(message, status, fromEmail, toEmail):
	fromaddr = fromEmail
	toaddrs = toEmail

	# Credentials (if needed)
	username = 'sunnysidesounds'
	password = 'password'
    
	 # The actual mail send
	server = smtplib.SMTP('smtp.gmail.com:587')
	server.starttls()
	server.login(username,password)
	server.sendmail(fromaddr, toaddrs, 'Subject: %s\r\n%s' % (status, message))
	server.quit()



emailAlert('test', 'test', 'sunnysidesounds@gmail.com', '4156903590@txt.att.net')


"""





