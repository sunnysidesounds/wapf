#!/usr/bin/env python

#Used to extract mdesgin images from photo site.

import urllib2
import re
from os.path import basename
from urlparse import urlsplit

url = "http://nicoleraine.photoshelter.com/gallery/Margaret-Mitacek-Interior-Design-LLC/G0000P7ziSBdEuGE/"
urlContent = urllib2.urlopen(url).read()
# HTML image tag: <img src="url" alt="some_text"/>
imgUrls = re.findall('img .*?src="(.*?)"', urlContent)

# download all images
for imgUrl in imgUrls:
    try:
        imgData = urllib2.urlopen(imgUrl).read()
        
        baseUrl = 'http://cdn.c.photoshelter.com/img-get/I0000Y3.7Ve9xWbk/s/650/650/'
        fileName = basename(urlsplit(imgUrl)[2])
        
        extractionUrl = baseUrl + fileName
        print extractionUrl
        os.system("wget " + extractionUrl + "")
        

        

    except:
        pass

