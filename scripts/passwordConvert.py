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
import base64

password = 'rbUcC7sQ7Rkx'

encodedPassword = base64.b64encode(password)
decodedPassword = base64.b64decode(encodedPassword)



print 'Encoded Password: ' + str(encodedPassword)
print 'Decoded Password: ' + str(decodedPassword)