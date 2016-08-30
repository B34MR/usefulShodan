# usefulShodan
Parses Shodan data from a list of IP addresses and saves output to an XLSX file.

#Usage:
Usage: ./usefulShodan.py <OPTIONS>
Example: ./usefulShodan.py -i /opt/scope.txt 
Parsed data is saved in an XLSX format. (Filter and sort data for desired results.)
Output path: shodan/shodan-data/shodan_timestamp.xlsx
 -i <input>\t\tInputs file containing a list of IP addresses.
 -h <help>\t\tPrints this help menu.

#Installation:
		usefulShodan.py requires the Shodan Command-Line Interface (CLI). 
		To install Shodan CLI execute: easy_install shodan
	
		To upgrade Shodan CLI: easy_install -U shodan
	
		Shodan CLI supports both free and paid API Keys.
		Initialize the environment with your API key using shodan init: shodan init YOUR_API_KEY
