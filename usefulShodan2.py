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

	def __init__(self, cmd='shodan host --format tsv'):
		self.cmd = cmd
		self.filepath = None
		self.ipaddress = None


	def run():
		''' '''
		pass


	def scan_host(self, ipadress):
		''' '''

		cmd = self.cmd.split(' ')
		cmd.append(ipadress)

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
				return None
			else:
				# Define stdout as lst
				mylst = proc.stdout.split()

				# Convert lst:strs to lst:tuples ie, (port, protocol).
				port_protocol = [(mylst[i], mylst[i+1]) for i in range(0, len(mylst), 2)]

				return cmd[4], port_protocol



	def read_ipaddress(self, filepath):
		''' '''

		with open(self.filepath, 'r') as f:
			lines = f.readlines()
			# remove \n from lst.
			self.ipaddress = list(map(lambda s: s.strip(), lines))


	def read_file(self, filepath):
		''' '''

		if os.path.isfile(filepath):
			self.filepath = filepath

			self.read_ipaddress(self.filepath)
		else:
			return False


	def save_xlxs(self):
		''' '''
		pass


	def save_txt(self):
		''' '''
		pass


	def print_table(self):
		''' '''
		pass

	
	def print_version(self):
		''' '''
		pass



def main():
	''' Main func '''

	usefulshodan = UsefulShodan()

	usefulshodan.read_file('scope2.txt')
	print(usefulshodan.filepath)
	print(usefulshodan.ipaddress)

	# for line in lines:
	# 	try:
	# 		ip = line.strip('\n')
	# 		result = usefulshodan.scan_host(ip)
	# 	except Exception as e:
	# 		print(e)
	# 		# raise e
	# 		pass
	# 	else:
	# 		if result != None:
	# 			console.log(f'{result}')


if __name__ == '__main__':
	main()
