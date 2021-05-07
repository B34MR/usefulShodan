#!/usr/bin/env python3

from rich.console import Console
from rich.logging import RichHandler
import os
import sys
import logging
import subprocess


# Init Rich console.
console = Console()

# logger - Rich
logging.basicConfig(
	# filename='',
	level='WARNING',
	format='%(message)s',
	datefmt='[%X]',
	handlers=[RichHandler(console=console, rich_tracebacks=True)]
	)
logging = logging.getLogger('rich')


class UsefulShodan():
	''' Shodan Cli Wrapper '''

	def __init__(self):
		self.filepath = None
		self.ipaddresses = None


	def scan_ip(self, ipaddress, cmd='shodan host --format tsv'):
		''' Process IP address against Shodan's database '''

		result = []
		# Shodan scan command.
		cmd = cmd.split(' ')
		cmd.append(ipaddress)

		try:
			proc = subprocess.run(cmd,
			shell=False, 
			check=False, 
			capture_output=True, 
			text=True)
		except Exception as e:
			# Set check=True for the exception to catch.
			logging.exception(f'{e}')
			pass # raise e
		else:
			if 'Error: No information available for that IP.' in proc.stderr:
				# Append ip and None values to result:lst.
				result.append((ipaddress, None, None))
			else:
				stdoutlst = proc.stdout.split()
				# Process scan results with multiple ports per ip. 
				# Dev-note used a lst-comprehension nested within a dict to simplify.
				resultdict = {ipaddress: [(stdoutlst[i], stdoutlst[i+1]) for i in range(0, len(stdoutlst), 2)]}
				# Apppend resultdic to result:lst.
				for k, v in resultdict.items():
					for i in v:
						# print(f'DEBUG: {k}, {i[0]}, {i[1]}')
						i = (k, i[0], i[1].upper())
						result.append(i)
			return result


	def read_ipaddress(self, filepath):
		''' '''

		with open(self.filepath, 'r') as f:
			lines = f.readlines()
			# remove \n from lst.
			self.ipaddresses = list(map(lambda s: s.strip(), lines))


	def read_file(self, filepath):
		''' '''

		if os.path.isfile(filepath):
			self.filepath = filepath

			self.read_ipaddress(self.filepath)
		else:
			return False


def main():
	''' Main func '''

	# DEV: Table
	from rich.table import Table
	from rich import box

	from rich.theme import Theme
	custom_theme = Theme({
		'status.spinner' :'orange1',
		'txt.spinner' : 'light_sky_blue3'
		})
	from rich.console import Console
	console = Console(theme=custom_theme)

	# Table title.
	table = Table(title="Shodan.io", box=box.DOUBLE_EDGE)
	# Columns defined.
	table.add_column("IP Address", justify="left", style="light_sky_blue3", no_wrap=True) #khaki3
	table.add_column("Port", justify="left", style="orange3", no_wrap=True)
	table.add_column("Protocol", justify="left", style="grey37", no_wrap=True)

	# Filepath arg value.
	FILE = sys.argv[1]
	# Create instance
	usefulshodan = UsefulShodan()
	# Read file from argv.
	usefulshodan.read_file(FILE)
	# Read IP addressees.
	ipaddresses = usefulshodan.ipaddresses

	# DEV: verbose flag
	verbose = False

	try:
		
		for ip in ipaddresses:
			with console.status(f'[txt.spinner]Scanning... [orange3]{ip}') as status:
				# Scan IP address against Shodan's database.
				results = usefulshodan.scan_ip(ip)
				for result in results:
					# Non-verbose print, exclude 'None' type results.
					if verbose == False:
						if result[1] is None:
							pass
						else:
							# console.log(f'[wheat4]{result}')
							# DEV - table
							table.add_row(f'{result[0]}', f'{result[1]}', f'{result[2]}')
					# Verbose print. include 'None' type results.
					else:
						# console.log(f'[wheat4]{result}')
						# DEV - table
						table.add_row(f'{result[0]}', f'{result[1]}', f'{result[2]}')
	except KeyboardInterrupt:
		print(f'\nQuit: detected [CTRL-C]')
	
	# DEV
	print('\n')
	console.print(table)
	console.print('\n[italic][deep_sky_blue4][link=https://www.shodan.io]https://www.shodan.io[/link]\n')


if __name__ == '__main__':
	main()
