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
from selenium import selenium
from threading import Thread
import subprocess
from Queue import Queue
sys.path.append( os.path.join( os.getcwd(), '..' ) )

import wapf
import config

wobj = wapf.wapf(config.baseUrl, config.browser)




num_threads = 4
queue = Queue()
ips = ["216.182.92.75", "216.182.92.76", "216.182.92.77", "216.182.92.78"]
#wraps system ping command
def pinger(i, q):
    """Pings subnet"""
    while True:
        ip = q.get()
        print "Thread %s: Pinging %s" % (i, ip)
        ret = subprocess.call("ping -c 1 %s" % ip,
                        shell=True,
                        stdout=open('/dev/null', 'w'),
                        stderr=subprocess.STDOUT)
        if ret == 0:
            print "%s: is alive" % ip
        else:
            print "%s: did not respond" % ip
        q.task_done()

#Spawn thread pool
for i in range(num_threads):

    worker = Thread(target=pinger, args=(i, queue))
    worker.setDaemon(True)
    worker.start()

#Place work in queue
for ip in ips:
    queue.put(ip)
#Wait until worker threads are done to exit    
queue.join()

