#!/usr/bin/env python3

from utils import richard as r
from utils import sqlite as db
from utils import shodan
import sys


def main():
	''' Main func '''

	# Table title.
	table = r.Table(title="[t.title]UsefulShodan2.py", box=r.box.DOUBLE_EDGE, style='table')
	# Table Columns.
	table.add_column("IP Address", justify="left", no_wrap=True, style='t.col1')
	table.add_column("Port", justify="left", no_wrap=True,  style='t.col2')
	table.add_column("Protocol", justify="left", no_wrap=True, style='t.col3')

	# User defined filepath
	FILE = sys.argv[1]
	# Create instance.
	usefulshodan = shodan.UsefulShodan()
	# Read file and store ipaddresses to instance.
	usefulshodan.read_file(FILE)
	# Retrieve ipaddressees from instance.
	ipaddresses = usefulshodan.ipaddresses

	# DEV: verbose flag.
	verbose = False

	# DEV: debug flag.
	debug = False

	# Header
	r.console.print(f'\nUsefulShodan2: [i]An over engineered for-loop for the Shodan-cli.', style='header')
	r.console.print(f'Shodan.io: [url][link=https://cli.shodan.io/]https://cli.shodan.io', style='header')
	r.console.print(f'Github.com: [url][link=https://github.com/NickSanzotta/usefulShodan/]https://github.com/NickSanzotta\n', style='header')

	try:
		for ip in ipaddresses:
			with r.console.status(spinner='bouncingBar', status=f'[status.text]Shodan.io: [white]{ip}') as status:
				# Scan IP address against Shodan's database.
				results = usefulshodan.scan_ip(ip)
				# Unpack results:lst.
				for result in results:
					# Non-verbose print, exclude 'None' type results.
					if verbose == False:
						if result[1] is None:
							pass
						else:
							# DEBUG print
							# r.console.log(f'[wheat4]{result}')

							# Insert ipaddress, port, protocol into database.
							db.insert_result(result[0], result[1], result[2])

							# DEV Rich Table
							table.add_row(f'{result[0]}', f'{result[1]}', f'{result[2]}')
					# Verbose print. include 'None' type results.
					else:
						# DEBUG print
						# r.console.log(f'[wheat4]{result}')

						# Insert ipaddress, port, protocol into database.
						db.insert_result(result[0], result[1], result[2])

						# Dev Rich Table.
						table.add_row(f'{result[0]}', f'{result[1]}', f'{result[2]}')
	except KeyboardInterrupt:
		print(f'\nQuit: detected [CTRL-C]')
	
	# Render table.
	r.console.print('\n')
	r.console.print(table)
	r.console.print('\n')


if __name__ == '__main__':
	main()
