#!/usr/bin/env python3

import os
import subprocess

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
			print(f'{e}')
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


	def read_file(self, filepath):
		''' Raed file and store ipaddress to instancce. '''

		if os.path.isfile(filepath):
			self.filepath = filepath

			with open(self.filepath, 'r') as f:
				lines = f.readlines()
				# remove \n from lst.
				self.ipaddresses = list(map(lambda s: s.strip(), lines))
		else:
			return False