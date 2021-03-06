
## WHAT IS WAPF?

Wapf is a web analyzing and profiling framework built with python and selenium. It allows you to test and extract many different kinds of data that can be used for a multitude of purposes. It can basically mimc a user (i.e. functional testing) while extracting other data such as speed metrics, keyword density, profiling information, w3c validation data and more. (See the feature section for a complete list) The framework was designed to make it easy to run multiple functional testing and data extracting commands all in a single command. (See the usage section on how to execute commands)
	

## FEATURES:
*	Multiprocessing recursive crawler
*	Multiprocess core and custom scripts
*	Custom configuration file management system
*	Validate using w3c validation
*	Profile web pages using selenium standalone server
*	Write functional tests (requires selenium module to be installed)
*	Parse and manipulate web pages using the BeauitifulSoup library (TODO: Update this library)
	*	Grab links, content, js, css and images and just about anything.
*	Take screenshots using firefox and chrome
*	Do a keyword density test
*	File manipulation and log file formatting
*	zip/unzip files
*	data conversions
*	HTTP analyzing
*	Custom utilities


## INSTALLATION/SETUP:
This framework has been tested on Ubuntu 11.10 Server and Mac OS X 10.6.8 and should work on any unix/linux distro. Windows has not been tested! 
	
### To setup the framework you have two choices:
#### 1) INSTALL IT ON YOUR OWN SYSTEM: 
  (Install from Git Source and installed the required linux packages): 

  
If using Ubuntu, don't forget to update:
	``` [sudo] aptitude update && [sudo] aptitude dist-upgrade ```
	
Unix/Linux Package:
*	Install python selenium webdriver 
	*	``` [sudo] easy_install selenium or [sudo] pip install selenium ```
*	Install Firefox and other packages to run headless:
	*	``` [sudo] sudo apt-get install firefox ``` 
	*	``` [sudo] apt-get install xvfb ```
	*	``` [sudo] apt-get install xfonts-cyrillic ``` (This is to fix this error when starting firefox (Missing fonts): Xlib:  extension "RANDR" missing on display ":99".`)
*	Install Java for headless 
	*	``` [sudo] apt-get install openjdk-6-jre-headless ```
*	Install curl for w3c validator 
	*	```[sudo] apt-get install curl```
*	Install termcolor for terminal color
	*	```[sudo] pip install termcolor```
	
##### Running in Headless:
If you want to run selenium in the background and in headless mode on start-up. Added these commands to /etc/rc.local

    Xvfb :4444 -ac -screen 0 1024x768x8 > /tmp/xvfb.log 2>&1 &
    export DISPLAY=localhost:4444.0 && java -jar /home/dev/wapf/selenium_standalone/selenium-server-standalone-2.13.0.jar  > /tmp/selenium_server.log 2>&1 &
	
(Note: Adjust your path if need be. /wapf/selenium_standalone might not be in /home/dev/)
	
I also added this command " export DISPLAY=:99 " to my .profile (or .bash_profile) so the firefox will work headless. If you don't add this to .profile file on start-up you'll have to manually execute that command.
	


#### 2) DOWNLOAD AND USE VM: (Download and use the Wapf Ubuntu VM)
Below are the steps used to setup a VM of Wapf. Please email me and I will give you a link of where you can download the 5GB VM image. Note, these instruction are specific for Mac OS X and VMware fusions. 

1. Download the VM from the email I sent you.
2. Copy this VM into /Users/<your_username>/Documents/Virtual Machines.localized directory
3. Drag the Wapf virtual machine image from the finder window into the VMWare Fusion machine list and choose “Settings”.
4. Start the image and VMWare Fusion will ask you whether it was moved or copied, select the latter (copied) and continue as normal. This question will only occur once.
5. One you have the image setup, boot-up the image and enter username/password (dev, 2%Milk) 
6. Setup your github .ssh using these instruction --> https://help.github.com/articles/generating-ssh-keys
7. cd to /home/dev and pull down the repo by ```git clone git@github.com:sunnysidesounds/wapf.git``` It should make a directory in /home/dev called wapf. This is what we want. 
8. After the repo has been download we need to do a restart, run ```sudo shutdown -h now``` We need to do this as this VM on reboot will start some required Wapf services. This includes the selenium standalone server that starts on server start. 
9. Make sure the directories log, screenshots are writable. You shouldn't have to do anything. But if for some reason this is a directory write issues,  run these commands ```sudo chmod 777 /home/dev/wapf/log/``` and ```sudo chmod 777 /home/dev/wapf/screenshots/```
10. Your ready to look at thes Usage section.

## USAGE:
####	The basics:
Everything runs through the runWAPF.py script. This allows for you to utilize all of wapf's features. Here is the basic syntax for running a basic command:

    python runWAPF.py <optional_utility_trigger> <command> <optional_config>

	
####	There are 3 main mode that wapf has currently:
*	Mode 1: Multiprocessing using global configuration 
*	Mode 2: Single processing using custom configuration 
*	Mode 3: Single processing utility scripting

	
####	 Helpful commands to get you started:

To list all current core commands (The command list growing):

*	``` python runWAPF.py list ``` : display list of all current core and custom commands.

*	``` python runWAPF.py version ``` : display framework version.

*	``` python runWAPF.py help ``` : display's how to install, run and setup wapf.

*	``` python runWAPF.py crawler ``` : This is the frameworks crawler command. By using the configuration file you can crawl a site extract multiple of stuff. This specific command extract just urls it finds in the page. But you could easily extent this to extract other things. Note all crawler data is logged to the crawler_results_<current_date> files in the log/ directory by default. You  can change this is need be. 

*	``` python runWAPF.py keyword ``` : This will do a keyword denstity test on any urls you specific in th configuration file.

*	``` python runWAPF.py screenshot ``` : This takes screenshots and stores them in the screenshots/ directory under the current date. Note, currently only works with the browser setting of 'firefox'

*	``` python runWAPF.py profiler ``` : This will return http requests, page timing, list of files used on page, request specific status-method-doc-size-time data. Note all profiler data is logged to the profiler_results_<current_date> files in the log/ directory by default. You  can change this is need be.  Also this command requires that the selenium standalone server by runnings. To start this server run ```cd selenium_standalone/ && ./start_selenium.sh ``` from the root of the Wapf directory.

*	``` python runWAPF.py w3c ``` : This runs a w3c validator on any select page. Note all profiler data is logged to the w3c_results_<current_date> files in the log/ directory by default. You  can change this is need be.


####	 Configuration files (core/custom):

**CORE CONFIG:** One of the first things you should do when you're working with Wapf is to take a look at the config.py in the root directory. This configuration files is the heart of the framework. Below is a list of some of the core settings you should consider changing to meet your needs. 
*	baseUrl: Set the main url you will use to run your scans. 
*	browser: Set the browser your want selenium to use. Current options are: firefox, chrome. (chrome may have bugs)
*	enableWrite: Value is 1 or 0. This just turns on/off logging and writing of anything.
*	serverFarmMap: Set all host/ips of your app servers and run wapf commands on the farm. Current example can be found in the custom command zfarm (i.e. zfarm.py)

You also have the option to pool specific urls, or sub-urls to specific commands. As this is still in development. The basic idea is that you could run multiple commands at multiple urls simultaneously using the pythons multi-processing module.

**CUSTOM CONFIG:** Now take a look in the config/ directory. You will see a list of command-specifc-configuration files. These files work just as the core config. The only difference is if you want to run the command-specifc configuraiton file you'd run it using the second command option. An example would be:

    python runWAPF.py list config_list

The ability to use command-specific-configuration files allows you to scan multiple domains as sub-domains as well as hitting each app server in that domains farms. 


####	 Utility Scripts:
Utility scripts are any python script you want to add to the framework. By adding it to the framework your able to utilize many of the core features.  To get started, simply add your utility script to the utilities/ directory and run it with the framwork using this syntax:

    python runWAPF.py -u <name_of_script> <script_arguments>

An example to run a port scan on a domain you would run this command (Note. pscan is apart of the current utility script core):

    python runWAPF.py -u pscan http://www.<your_domain>.com

Replacing <your_domain> with the domain you want to scan. Note, the configuration file system hasn't been fully implemented. Evenutally you will be able to pass arguments to these utility scripts using either a core/custom configuration files. 

####	 Logging:
All logging happens in the /log directory. You can change the name of the logging files by viewing the core configuration files (config.py)

####	 Screenshots:
By running this commands ``` python runWAPF.py screenshot ``` you will take screenshots of any of the urls you put in your configuration files. See alphaLIst, betaList. Note all screenshots are stored in the screenshot/ directory under the current date. Also,  currently this features only works with the firefox browser. 

####	 Custom Commands (Setup, usage and examples):

**Usage / Examples:** Custom commands are located in the custom/ directory and are used for specific tasks that utilitize selenium and the Wapf framework. These custom commands use the same syntax as the core commands.The current scripts located in custom are related to a ecommerce website Zumiez.com. I left these scripts to give you some examples of what you can do. These are what these example scripts do:

*	``` python runWAPF.py zcheckout ``` : Picks a random sku (sourced: from a txt file of skus) and checkouts of the Zumiez.com ecommerce website. 
*	``` python runWAPF.py zcheckout110 ``` : Picks a random sku (sourced: from a txt file of skus) and checkouts of the new version (1.10) Zumiez.com ecommerce website. 
*	``` python runWAPF.py zfarm ``` : Checks all active app servers running Zumiez.com (Note: IP addresses have changed)
*	``` python runWAPF.py zleftbag ``` : Checks all left nav links on Zumiez.com storefronts for 404 links due to the use of Endeca. 
*	``` python runWAPF.py zmybag ``` : Checks the cart functionality. 

**New Script Setup:** Take a look at the current custom commands to see how to script a custom command. All custom command scripts should have at least these modules imported:

    import sys
    import os
    import re
    import multiprocessing
    import httplib
    import time
    import csv
    from random import choice
    from termcolor import colored
    sys.path.append( os.path.join( os.getcwd(), '..' ) )
    #custom modules
    import wapf
    import config 

The two most import modules you'll need are the wapf (core module) and config (configuration module) modules.


## TODOS:
Below is a list of current things still under development. 
*	Add configuration file system to utility scripts. 
*	Add safari and fix chrome browser bugs.
*	Add functionality to start selenium standalone by itself and run in the background. 
*	Add VM link








 
 


