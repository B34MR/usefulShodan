#!/usr/bin/env python3

import sqlite3

# Database init.
conn = sqlite3.connect('database.db')

# Database cursor.
c = conn.cursor()

# Database Table init.
try:
	with conn:
		c.execute("""CREATE TABLE Hosts(
			IP Address text,
			Port text,
			Protocol text
			)""")
except sqlite3.OperationalError: 
    pass


def insert_result(ipaddress, port, protocol):
	''' Insert result [(IP, Port, Protocol)] '''
	with conn:
		c.execute("INSERT INTO Hosts VALUES (:ipaddress, :port, :protocol)",
		 {'ipaddress': ipaddress, 'port': port, 'protocol': protocol})

