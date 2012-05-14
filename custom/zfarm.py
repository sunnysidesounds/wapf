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
from threading import Thread
import subprocess
from Queue import Queue
sys.path.append( os.path.join( os.getcwd(), '..' ) )
#custom modules
import wapf
import config 


print 'Test Server Farm'
wobj = wapf.wapf(config.baseUrl, config.browser)


num_threads = 1
queue = Queue()
ips = config.serverFarmMap
#wraps system ping command
def pinger(i, q):
    while True:
        ip = q.get()
        ret = subprocess.call("ping -c 1 %s" % ip,
                        shell=True,
                        stdout=open('/dev/null', 'w'),
                        stderr=subprocess.STDOUT)
        if ret == 0:
        	output = config.serverFarmMap[ip] + " ---> " + ip + " is alive"
        	output = output.rstrip("\n")
        	print output 
        	
        	#Mini Load Test
        	try:
        		loadTest = wobj.httpRequestProfiler('http://' + ip)
        		print loadTest
        	except:
        		print 'Load test unavailable!'
        	
    		
    		
        else:
        	print config.serverFarmMap[ip] + " ---> " + ip + " did not respond"
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