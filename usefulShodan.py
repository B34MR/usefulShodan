#!/usr/bin/python
# Nick Sanzotta (@Beamr)
# Description: Parses Shodan data from a list of IP addresses and saves output to an XLSX file.
import os, sys, getopt,xlsxwriter, time
from sys import argv 

timestr = time.strftime("%Y%m%d-%H%M")
curr_time = time.time()

class colors:
   white = "\033[1;37m"
   normal = "\033[0;00m"
   red = "\033[1;31m"
   blue = "\033[1;34m"
   green = "\033[1;32m"

banner = '\n ' + "-" * 85 + colors.green + '\n  usefulShodan.py v1.0 - Shodan Parser, Nick Sanzotta (@Beamr)\n ' + colors.normal + "-" * 85 + "\n"
def cls():
    os.system('cls' if os.name == 'nt' else 'clear')

def usefulShodan(inputfile):
	# Create a workbook and add a worksheet.
	workbook = xlsxwriter.Workbook('usefulShodan-data/shodan'+'_'+timestr+'.xlsx')
	worksheet = workbook.add_worksheet()
	# Add a bold format to use to highlight cells.
 	bold = workbook.add_format({'bold': True})
 	# Write some data headers.
	worksheet.write('A1', 'Ports - SSL Versions:', bold)
	worksheet.write('B1', 'IP Addresses:', bold)
	# Start from the first cell. Rows and columns are zero indexed.
	row = 1
	col = 0
	#Import IP Addresses from file
	with open(inputfile, 'rb') as f1:
			output1 = f1.read().splitlines()
	for host in output1:
		shodan = os.system('shodan host '+host+ '> /tmp/shodan.txt')
		with open('/tmp/shodan.txt', 'rb') as f2:
				output2 = f2.read()
		try:
			shodanList = output2.splitlines()
			ipaddress  = shodanList[0]
			servicesListening = shodanList[7::]
			servicesListening = [x.strip(' ') for x in servicesListening] #Removes white spaces for each item in list
			print ipaddress
			for item in servicesListening:
				item = item.replace('|-- ', '')
				print item.strip()
				worksheet.write(row, col,     item.strip())
				worksheet.write(row, col + 1, ipaddress)
				row += 1
			print("\n")
		except IndexError:
			print("\n")
	workbook.close()


def help():
    print banner
    print " Usage: ./usefulShodan.py <OPTIONS> \n"
    print " Example: ./usefulShodan.py -i /opt/clients/scope.txt\n"
    print " Parsed data is saved in an XLSX format. (Filter and sort data for desired results.)"
    print " Output path: shodan/shodan-data/shodan_timestamp.xlsx \n"
    print "\t -i <input>\t\tInputs file containing a list of IP addresses."
    print "\t -h <help>\t\tPrints this help menu."
    print """
    \nInstallation:
		usefulShodan.py requires the Shodan Command-Line Interface (CLI). 
		To install Shodan CLI execute: easy_install shodan
	
		To upgrade Shodan CLI: easy_install -U shodan
	
		Shodan CLI supports both free and paid API Keys.
		Initialize the environment with your API key using shodan init: shodan init YOUR_API_KEY
	"""
		
    sys.exit(2)
    
def main(argv):
    if len(argv) < 1:
        help()
    try:
        opts, args = getopt.getopt(argv, 'i:c:h',['input=','help'])
    except getopt.GetoptError:
        help()
        sys.exit(2)
    
    if not os.path.exists("usefulShodan-data/"):
        os.mkdir("usefulShodan-data/") 
    
    inputfile= ''

    for opt, arg in opts:
        if opt in ('-h', '--help'):
            help()
            sys.exit(2)
        elif opt in ('-i', '--input'):
            inputfile = arg
        else:
            help()
            sys.exit(2)
    cls()
    usefulShodan(inputfile)

if __name__ == "__main__":
    main(argv[1:])
print "\nCompleted in: %.1fs\n" % (time.time() - curr_time)
