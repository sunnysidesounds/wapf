#!/usr/bin/env python

################################################################################
## NAME: SITE MONITOR EXAMPLE 2
## DATE: Nov 2011
## AUTHOR: Jason R Alexander
## MAIL: sunnysidesounds@gmail.com
################################################################################

 
#!/usr/bin/env python
# Corey Goldberg - October 2009



import httplib
import sys
import time



def main():
    if len(sys.argv) != 3:
        print 'usage:\nurl_timer.py <url> <interval>\n'
        sys.exit(1)
        
    url = sys.argv[1]
    interval = int(sys.argv[2])

    if url.startswith('https://'):
        location = url.replace('https://', '')
        use_ssl = True
    elif url.startswith('http://'):
        location = url.replace('http://', '')
        use_ssl = False
    else:
        location = url
        use_ssl = False
        
    if '/' in location:
        parts = location.split('/')
        host = parts[0]
        path = '/' + '/'.join(parts[1:])
    else:
        host = location
        path = '/'

    run(host, path, interval, use_ssl)



def run(host, path, interval, use_ssl=False):
    # select most accurate timer based on platform
    if sys.platform.startswith('win'):
        default_timer = time.clock
    else:
        default_timer = time.time

    request_sent_times = []
    response_received_times = []        
    content_transferred_times = []
    sizes = []

    print 'request sent'.ljust(20),
    print 'response received'.ljust(20),
    print 'content transferred'.ljust(20),
    print 'size'
    
    print '------------'.ljust(20),
    print '-----------------'.ljust(20),
    print '-------------------'.ljust(20),
    print '----'
    
    while True:
        start_run = default_timer()
        
        if use_ssl:
            conn = httplib.HTTPSConnection(host)
        else:
            conn = httplib.HTTPConnection(host)
        start = default_timer()  
        conn.request('GET', path)
        request_time = default_timer()
        resp = conn.getresponse()
        response_time = default_timer()
        size = len(resp.read())
        conn.close()     
        transfer_time = default_timer()
        
        request_sent_times.append(request_time - start)
        response_received_times.append(response_time - start)
        content_transferred_times.append(transfer_time - start)
        sizes.append(size)
        
        print '%.4f' % (request_time - start),
        print ('(%.4f)' % (sum(request_sent_times) / len(request_sent_times))).ljust(13),
        
        print '%.4f' % (response_time - start),
        print ('(%.4f)' % (sum(response_received_times) / len(response_received_times))).ljust(13),
        
        print '%.4f' % (transfer_time - start),
        print ('(%.4f)' % (sum(content_transferred_times) / len(content_transferred_times))).ljust(13),

        print '%i bytes' % size,
        print '(%.3f MB total)' % (sum(sizes) / 1000000.0)
        
        elapsed_time = default_timer() - start_run
        if interval > elapsed_time:
            time.sleep(interval - elapsed_time)



if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        sys.exit(0)

