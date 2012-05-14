#!/usr/bin/env python

################################################################################
## NAME: SITE MONITOR EXAMPLE 2
## DATE: Nov 2011
## AUTHOR: Jason R Alexander
## MAIL: sunnysidesounds@gmail.com
################################################################################

 
import time
import urllib2
import pynotify

someurl = 'http://www.zumiez.com'
vresps = [200, 301, 302]
retryinterval = 10

def checkWeb(checkurl, httptimeout=None, validHTTPResponseCodes=None):
    if httptimeout is None:
        httptimeout = 10
    if validHTTPResponseCodes is None:
        validHTTPResponseCodes = [200, 301, 302]

    try:
        myresp = urllib2.urlopen(checkurl, timeout=int(httptimeout))
    except (urllib2.URLError, urllib2.HTTPError), e:
        return False, e

    respcode = myresp.getcode()
    if respcode in validHTTPResponseCodes:
        return True, respcode
    else:
        return False, respcode

while 1:
    ok = checkWeb(someurl, retryinterval, vresps)
    if ok[0] is True:
        print 'HTTP Code:', ok[1], time.asctime(time.localtime(time.time()))
    else:
        n = pynotify.Notification("Site down!", someurl + '\nResponse: ' + str(ok[1]) + '\n' + time.asctime(time.localtime(time.time())), "dialog-warning")
        n.set_urgency(pynotify.URGENCY_CRITICAL)
        # n.set_timeout(pynotify.EXPIRES_NEVER) # optional, makes the alert never go away automatically
        n.show()
        print ok[1], time.asctime(time.localtime(time.time()))

    time.sleep(int(retryinterval))
