#!/usr/bin/env python3

from utils import richard as r
from utils import sqlite as db
from utils import shodan
from utils import arguments
import sys


def main():
	''' Main func '''

	# Arguments init.
	args = arguments.parse_args()

	# Args filepath
	FILE = args.filepath

	# Args drop table.
	if args.drop:
		db.drop_table()

	# Args verbose.
	vverbose = False
	if args.verbose >=2:
		vverbose = True
	verbose = False
	if args.verbose >=1:
		verbose = True

	# Database init.
	db.create_table()
	# UsefulShoand class instance init.
	usefulshodan = shodan.UsefulShodan()
	# Read file and store ipaddresses to instance.
	usefulshodan.read_file(FILE)
	# Retrieve ipaddressees from instance.
	ipaddresses = usefulshodan.ipaddresses

	# Table title.
	table = r.Table(title="[t.title]UsefulShodan2.py", box=r.box.DOUBLE_EDGE, style='table')
	# Table Columns.
	table.add_column("IP Address", justify="left", no_wrap=True, style='t.col1')
	table.add_column("Port", justify="left", no_wrap=True,  style='t.col2')
	table.add_column("Protocol", justify="left", no_wrap=True, style='t.col3')

	# Header
	r.console.print(f'\n[i]UsefulShodan2', style='header')
	r.console.print(f'[i]A Python3 for-loop wrapper for the [url][link=https://cli.shodan.io/]Shodan CLI.', style='header')
	r.console.print('\n')

	try:
		for ip in ipaddresses:
			with r.console.status(spinner='bouncingBar', status=f'[status.text]Shodan.io: [white]{ip}') as status:
				# Scan IP address against Shodan's database.
				results = usefulshodan.scan_ip(ip)
				# Unpack results:lst.
				for result in results:
					# Very-verbose print, include console print and 'None' type results. 
					if vverbose == True:
						r.console.log(f'{result}')
						# Insert ipaddress, port, protocol into database.
						db.insert_result(result[0], result[1], result[2])
						# Print Rich Table.
						table.add_row(f'{result[0]}', f'{result[1]}', f'{result[2]}')
					# Verbose print, include 'None' type results.
					elif verbose == True:
						# Insert ipaddress, port, protocol into database.
						db.insert_result(result[0], result[1], result[2])
						# Print Rich Table.
						table.add_row(f'{result[0]}', f'{result[1]}', f'{result[2]}')
					# Standard print.
					else:
						if result[1] is None:
							pass
						else:
							# Insert ipaddress, port, protocol into database.
							db.insert_result(result[0], result[1], result[2])
							# Print Rich Table
							table.add_row(f'{result[0]}', f'{result[1]}', f'{result[2]}')

	except KeyboardInterrupt:
		print(f'\nQuit: detected [CTRL-C]')
	
	# Render table.
	r.console.print('\n')
	r.console.print(table)
	r.console.print('\n')


if __name__ == '__main__':
	main()
