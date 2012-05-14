#!/usr/bin/env python

################################################################################
## NAME: MULTI-THREAD PROCESSING EXAMPLE
## DATE: Oct 2011
## AUTHOR: Jason R Alexander
## MAIL: JasonAlexander@zumiez.com
## SITE: http://www.zumiez.com
################################################################################

import multiprocessing

def crawl(result_queue):
    import urllib2
    data = urllib2.urlopen("http://news.ycombinator.com/").read()

    print "Requested..."

    if "result found (for example)":
        result_queue.put("result!")

    print "Read site."

processs = []
result_queue = multiprocessing.Queue()

for n in range(4): # start 4 processes crawling for the result
    process = multiprocessing.Process(target=crawl, args=[result_queue])
    process.start()
    processs.append(process)

print "Waiting for result..."

result = result_queue.get() # waits until any of the proccess have `.put()` a result

for process in processs: # then kill them all off
    process.terminate()

print "Got result:", result