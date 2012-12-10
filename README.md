
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
#### 1) INSTALL OWN YOUR OWN SYSTEM: 
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
	
 I have created a VM (with VMware) that has everything already setup and ready to run out of the box. If you decide to use this option. Just email me and I'll give you a link to the download VMware image. 
 
 VM Link coming soon!

	
## USAGE:
#####	The basics:
Everything runs through the runWAPF.py script. This allows for you to utilize all of wapf's features. Here is the basic syntax for running a basic command:

    python runWAPF.py <command> <optional_config>
	
#####	There are 3 main mode that wapf has currently:
*	Mode 1: Multiprocessing using global configuration 
*	Mode 2: Single processing using custom configuration 
*	Mode 3: Single processing utility scripting
	
#####	 Helpful commands to get you started:

To list all current core commands (The command list growing):

*	``` python runWAPF.py list ``` ---> display list of all current core and custom commands.

*	``` python runWAPF.py version ``` ---> display framework version.

*	``` python runWAPF.py help ``` ---> display's how to install, run and setup wapf. (TODO: instead of reading.txt, we want to evenutally read README.md)

*	``` python runWAPF.py crawler ``` ---> This is the frameworks crawler command. By using the configuration file you can crawl a site extract multiple of stuff. This specific command extract just urls it finds in the page. But you could easily extent this to extract other things. Note all crawler data is logged to the crawler_results_<current_date> files in the log/ directory by default. You  can change this is need be. 

*	``` python runWAPF.py keyword ``` ---> This will do a keyword denstity test on any urls you specific in th configuration file.

*	``` python runWAPF.py screenshot ``` ---> This takes screenshots and stores them in the screenshots/ directory under the current date. Note, currently only works with the browser setting of 'firefox'

*	``` python runWAPF.py profiler ``` ---> This will return http requests, page timing, list of files used on page, request specific status-method-doc-size-time data. Note all profiler data is logged to the profiler_results_<current_date> files in the log/ directory by default. You  can change this is need be.  Also this command requires that the selenium standalone server by runnings. To start this server run ```cd selenium_standalone/ && ./start_selenium.sh ``` from the root of the Wapf directory.

*	``` python runWAPF.py w3c ``` ---> This runs a w3c validator on any select page. Note all profiler data is logged to the w3c_results_<current_date> files in the log/ directory by default. You  can change this is need be.

#####	 Configuration files (core/custom):

**CORE CONFIG:** One of the first things you should do when you're working with Wapf is to take a look at the config.py in the root directory. This configuration files is the heart of the framework. Below is a list of some of the core settings you should consider changing to meet your needs. 
*	baseUrl: Set the main url you will use to run your scans. 
*	browser: Set the browser your want selenium to use. Current options are: firefox, chrome. (chrome may have bugs)
*	enableWrite: Value is 1 or 0. This just turns on/off logging and writing of anything.
*	serverFarmMap: Set all host/ips of your app servers and run wapf commands on the farm. Current example can be found in the custom command zfarm (i.e. zfarm.py)

You also have the option to pool specific urls, or sub-urls to specific commands. As this is still in development. The basic idea is that you could run multiple commands at multiple urls simultaneously using the pythons multi-processing module.

**CUSTOM CONFIG:** Now take a look in the config/ directory. You will see a list of command-specifc-configuration files. These files work just as the core config. The only difference is if you want to run the command-specifc configuraiton file you'd run it using the second command option. An example would be:

    python runWAPF.py list config_list

The ability to use command-specific-configuration files allows you to scan multiple domains as sub-domains as well as hitting each app server in that domains farms. 


#####	**Mode 1:** Multiprocessing using global configuration:


 
 


