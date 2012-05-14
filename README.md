
## WHAT IS WAPF?

Wapf is a web analyzing and profiling framework built with python and selenium. It allows you to test and extract many different kinds of data that can be used for a multitude of purposes. It can basically mimc a user (i.e. functional testing) while extracting other data such as speed metrics, keyword density, profiling information, w3c validation data and more. (See the feature section for a complete list) The framework was designed to make it easy to run multiple functional testing and data extracting commands all in a single command. (See the usage section on how to execute commands)
	

## FEATURES:
-Multiprocessing recursive crawler
-Validate using w3c validation
-Profile web pages using selenium standalone server
-Write functional tests (requires selenium module to be installed)
-Parse and manipulate web pages using the BeauitifulSoup library
	-Grab links, content, js, css and images
-Take screenshots using firefox and chrome
-Do a keyword density test
-File manipulation and log file formatting
-zip/unzip files
-data conversions
-HTTP analyzing

	
## INSTALLATION/SETUP:
This framework has been tested on Ubuntu 11.10 and Mac OS X 10.6.8 and should work on any unix/linux distro. Windows has not been tested! 
	
### To setup the framework you have two choices:
#### 1) INSTALL OWN YOUR OWN SYSTEM: 
  (Install from SVN/Git Source and installed the required linux packages): 

  
If using Ubuntu, don't forget to update: [sudo] aptitude update && [sudo] aptitude dist-upgrade
===
	
 Unix/Linux Package:
	-Install python selenium webdriver 
		-> [sudo] easy_install selenium or [sudo] pip install selenium
	-Install Firefox and other packages to run headless:
		-> [sudo] sudo apt-get install firefox
		-> [sudo] apt-get install xvfb
		-> [sudo] apt-get install xfonts-cyrillic (This is to fix this error when starting firefox (Missing fonts): Xlib:  extension "RANDR" missing on display ":99".`)
	-Install Java for headless 
		-> [sudo] apt-get install openjdk-6-jre-headless
	-Install curl for w3c validator 
		-> [sudo] apt-get install curl
	-Install termcolor for terminal color
		-> [sudo] pip install termcolor
	
 Running in Headless:
	If you want to run selenium in the background and in headless mode on start-up. Added these commands to /etc/rc.local
	
	Xvfb :4444 -ac -screen 0 1024x768x8 > /tmp/xvfb.log 2>&1 &
	export DISPLAY=localhost:4444.0 && java -jar /home/dev/wapf/selenium_standalone/selenium-server-standalone-2.13.0.jar  > /tmp/selenium_server.log 2>&1 &
	
	(Note: Adjust your path if need be. /wapf/selenium_standalone might not be in /home/dev/)
	
	I also added this command " export DISPLAY=:99 " to my .profile (or .bash_profile) so the firefox will work headless. If you don't add this to .profile file on start-up you'll have to manually execute that command.
	


#### 2) DOWNLOAD AND USE VM: (Download and use the Wapf Ubuntu VM)
	
 I have created a VM (with VMware) that has everything already setup and ready to run out of the box. If you decide to use this option. Just download and install the VMware image. 
	
 Start up the VM and login with:
 Username: dev
 Password 2%Milk
	

## USAGE:
The basic:

	-Everything runs through the runWAPF.py script. This allows for you to utilize all of wapf's features. Here is the basic syntax for running a basic command:
	
		python runWAPF.py <command>
	
	
	There are 3 main mode that wapf has currently:
	
	Mode 1: Multiprocessing using global configuration 
	
	Mode 2: Single processing using custom configuration 
	
	Mode 3: Single processing utility scripting
	
	
More details coming soon….

 
 


