# usefulShodan2.py

	UsefulShodan2: An over engineered for-loop for the Shodan-cli.

***  
Installation:

		usefulShodan2.py requires the Shodan Command-Line Interface (CLI). 
		To install Shodan CLI execute: easy_install shodan
	
		To upgrade Shodan CLI: easy_install -U shodan
	
		Shodan CLI supports both free and paid API Keys.
		Initialize the environment with your API key using shodan init: shodan init YOUR_API_KEY

		For more information visit: https://cli.shodan.io
***
Usage:

	Usage: python3 usefulShodan2.py [FILEPATH]
 	Example: python3 usefulShodan2.py targets.txt

 	Filepath - supports single IP addresses per line.

 	Input file example:

		# cat targets.txt
		 10.10.10.10
		 20.20.20.20
