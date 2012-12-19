#!/usr/bin/env python

################################################################################
## NAME: wapf Global Configuration File
## AUTHOR: Jason R Alexander
## MAIL: JasonAlexander@zumiez.com
## SITE: http://www.snippetboxx.com
## INFO: This script holds all the values you will run against the framework
################################################################################

#modules
import time


#global configuration varibles
#################################
baseUrl = 'http://staging11.zumiez.com/' #make sure you have the ending slash (important!)
browser = 'firefox'
enableWrite = 1
today = time.strftime("%m%d%Y")
systemDates = time.strftime("%Y-%m-%d %H:%M:%S")
wapfVersion = 'Version 1.1.0 alpha'
readmeDoc = 'https://github.com/sunnysidesounds/wapf/blob/master/README.md'
profilerFileFormat = 'csv' #options are text, csv

#File Related
#################################
crawlerFileName = 'crawler_results' + str(today)
w3cFileName = 'w3c_results_' + str(today) #if left blank it and today removed will use printMessage format (results_timestamp_browser.txt)
profilerFileName = 'profiler_results_' + str(today) #if left blank it and today removed will use printMessage format (results_timestamp_browser.txt)
profilerFileNameCSV = 'profiler_results_' + str(today) + '.csv'
screenshotFileName = 'screenshots'
customFileName = 'custom_test_'

#Data formatting
#################################
template = "{0:25} {1:10} {2:15}" # column widths
templateTwo = "{0:30} {1:10}" # column widths

#base scripts used to pool into data specific scripts
#################################
alphaList = [baseUrl + 'shoes.html', baseUrl + 'girls.html', baseUrl + 'skate.html', baseUrl + 'boys.html/', baseUrl + 'accessories.html/', baseUrl + 'snow.html/', baseUrl + 'pro-riders.html/', baseUrl + 'brands.html/']
betaList = [baseUrl + 'test-rob-snowchat-1', baseUrl + 'test-rob-snowchat-2']
gammaList = [baseUrl + 'shoes.html']
deltaList = []
epsilonList = []

#data lists for specific scripts
#################################
crawlerList = alphaList
profilerList = gammaList
w3cList = alphaList
screenshotList = alphaList


#server farm IPs
#################################
serverFarmMap = {'216.182.92.75' : 'web10', 
								'96.31.161.104':'web1', 
								'216.182.92.76':'web11', 
								'216.182.92.77':'web12',
								'216.182.92.78':'web13',
								'173.240.50.145':'web14',
								'173.240.50.146':'web15',
								'173.240.50.147':'web16',
								'173.240.50.151':'web17',
								'173.240.50.152':'web18',
								'173.240.50.153':'web19',
								'96.31.161.107':'web2',
								'173.240.50.154':'web20',
								'173.240.50.155':'web21',
								'173.240.50.156':'web22',
								'173.240.50.157':'web23',
								'173.240.50.158':'web24',
								'67.212.137.217':'web25',
								'67.212.137.219':'web26',
								'67.212.137.221':'web27',
								'67.212.137.222':'web28',
								'67.212.137.210':'web29',
								'96.31.161.117':'web3',
								'173.240.59.10':'web30',
								'173.240.59.11':'web31',
								'173.240.59.12':'web32',
								'173.240.59.13':'web33',
								'173.240.59.14':'web34',
								'173.240.59.15':'web35',
								'173.240.59.16':'web36',
								'173.240.59.17':'web37',
								'173.240.59.18':'web38',
								'96.31.160.52':'web4',
								'96.31.160.53':'web5',
								'216.182.92.71':'web6',
								'216.182.92.72':'web7',
								'96.31.161.119':'web8',
								'96.31.161.121':'web9',
								'173.240.59.21':'web41',
								'173.240.59.22':'web42',
								'173.240.59.23':'web43',
								'173.240.59.24':'web44',
								'173.240.59.25':'web45',
								'173.240.59.26':'web46',
								'173.240.59.27':'web47',
								'173.240.59.28':'web48',
								'173.240.59.35':'web49',
								'173.240.59.23':'web50',
								'173.240.59.39':'web51',
								'173.240.59.38':'web52',
								'173.240.59.37':'web53',
								'173.240.59.40':'web54',
								'173.240.59.41':'web55',
								'173.240.59.42':'web56',
								'173.240.59.43':'web57',
								'173.240.59.44':'web58'}




