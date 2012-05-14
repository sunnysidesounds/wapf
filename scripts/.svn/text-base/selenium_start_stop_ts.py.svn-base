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
import selenium
import socket
import subprocess
import shlex
import time
sys.path.append( os.path.join( os.getcwd(), '..' ) )
import wapf


baseUrl = 'http://www.zumiez.com/'
browser = 'firefox'
enableWrite = 0

#create class instance
tobj = wapf.wapf(baseUrl, browser) #init baseUrl and browser


# CHANGE path='/path/to/selenium-server.jar' AS NEEDED:
def start_server(path='../selenium_standalone/selenium-server-standalone-2.1.0.jar'):
    null=open('/dev/null')
    proc=subprocess.Popen(shlex.split('java -jar {p}'.format(p=path)),
                          stdout=null,stderr=null)
    return proc

def shutdown_server(sel):
    sel.shut_down_selenium_server()

def start_selenium(host="localhost",
                   port=4444,
                   browserStartCommand="*firefox",
                   browserURL="http://www.google.com/"):
    sel=selenium.selenium(host,port,browserStartCommand,browserURL)
    try:
        sel.start()
    except socket.error as err:
        proc=start_server()
        time.sleep(1)
        try:
            sel.start()
        except socket.error as err:
            sys.exit(err)
    return sel

if __name__=='__main__':
    sel=start_selenium()
    time.sleep(1)
    #Add action here
    sel.stop()
    shutdown_server(sel)

