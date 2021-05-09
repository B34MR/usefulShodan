#!/usr/bin/env python3

import sqlite3

# Database init.
conn = sqlite3.connect('database.db')

# Database cursor.
c = conn.cursor()


def create_table():
	''' Create table "Hosts" '''

	try:
		with conn:
			c.execute("""CREATE TABLE Hosts(
				IP Address text,
				Port text,
				Protocol text
				)""")
	except sqlite3.OperationalError: 
	    pass


def drop_table():
	''' Drop table "Hosts" '''
	
	try:
		with conn:
			c.execute(f"DROP TABLE Hosts")
	except sqlite3.OperationalError as e:
		pass


def insert_result(ipaddress, port, protocol):
	''' Insert result [(IP, Port, Protocol)] '''
	
	with conn:
		c.execute("INSERT INTO Hosts VALUES (:ipaddress, :port, :protocol)",
		 {'ipaddress': ipaddress, 'port': port, 'protocol': protocol})

