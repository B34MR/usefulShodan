# usefulShodan.py

				  ___          ___      
				/'___\        /\_ \     
	 __  __    ____     __ /\ \__/  __  __\//\ \    
	/\ \/\ \  /',__\  /'__`\ \ ,__\/\ \/\ \ \ \ \   
	\ \ \_\ \/\__, `\/\  __/\ \ \_/\ \ \_\ \ \_\ \_ 
	 \ \____/\/\____/\ \____\\ \_\  \ \____/ /\____\
	  \/___/  \/___/  \/____/ \/_/   \/___/  \/____/
	 ____    __                  __                      
	/\  _`\ /\ \                /\ \                     
	\ \,\L\_\ \ \___     ___    \_\ \     __      ___    
	 \/_\__ \\ \  _ `\  / __`\  /'_` \  /'__`\  /' _ `\  
	   /\ \L\ \ \ \ \ \/\ \L\ \/\ \L\ \/\ \L\.\_/\ \/\ \ 
	   \ `\____\ \_\ \_\ \____/\ \___,_\ \__/.\_\ \_\ \_\
	    \/_____/\/_/\/_/\/___/  \/__,_ /\/__/\/_/\/_/\/_/

	Description: Parses Shodan data from a list of IP addresses and saves output to an XLSX file.
	Created by: Nick Sanzotta / @beamr
	Version: usefulShodan.py v 1.10072016
***  
Installation:

		usefulShodan.py requires the Shodan Command-Line Interface (CLI). 
		To install Shodan CLI execute: easy_install shodan
	
		To upgrade Shodan CLI: easy_install -U shodan
	
		Shodan CLI supports both free and paid API Keys.
		Initialize the environment with your API key using shodan init: shodan init YOUR_API_KEY


***
Usage:

	Usage: ./usefulShodan.py <OPTIONS>
 	Example: ./usefulShodan.py -i /client/scope.txt

 	Supports Single IP Address and CIDR format.

 	Input file example:

	 	root@beamr:~# more /scope.txt
	 	210.11.101.0/25
	 	216.11.101.0/28
		 10.10.10.10
		 20.20.20.20

 	Parsed data is saved in an XLSX format. (Filter and sort data for desired results.)
 	Output path: shodan/shodan-data/shodan_timestamp.xlsx 

	 -i <input>		Inputs file containing a list of IP addresses.
	 -h <help>		Prints this help menu.
