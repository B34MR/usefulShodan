![Supported Python versions](https://img.shields.io/badge/python-3.9-green.svg)

# UsefulShodan2
A Python3 for-loop wrapper for the Shodan Command-Line Interface (CLI).

**Requirements :**

Shodan CLI installation. 
```
easy_install shodan
```

API key Initialization (free and paid API keys supported).
```
shodan init [API-KEY]
```
For more information visit: 
```
https://cli.shodan.io
```

**Installation :**
```
git clone https://github.com/B34MR/usefulShodan.git
cd usefulShodan
python3 -m pip install -r requirements.txt
```    

**Menu :**
```
Usage:
    python3 usefulShodan2.py <inputfile>
    python3 usefulShodan2.py <inputfile> -d
    python3 usefulShodan2.py <inputfile> -v
    python3 usefulShodan2.py <inputfile> -vv

Positional argument(s):
    [inputfile]: Input from list of IP addresses (supports one IP address per line).

Optional argument(s):
    [-d, --drop]: Drop existing data and launch with a clean database.
    [-v, --verbose]: Increase verbosity level (Include results 'None').
    [-vv, --verbose --verbose]: Increase verbosity level (Include results 'None' and print results in real-time).
```

**Standard Output :**
```
# python3 usefulShodan2.py targets.txt

         UsefulShodan2.py
╔═══════════════╤══════╤══════════╗
║ IP Address    │ Port │ Protocol ║
╟───────────────┼──────┼──────────╢
║ 127.0.0.1   	│ 445  │ TCP      ║
║ 127.0.0.2 	│ 161  │ UDP      ║
╚═══════════════╧══════╧══════════╝
```

**Verbose Output :**
```
Verbose output will include IP addresses with no results. I.e 'None'

# python3 usefulShodan2.py targets.txt -v

         UsefulShodan2.py
╔═══════════════╤══════╤══════════╗
║ IP Address    │ Port │ Protocol ║
╟───────────────┼──────┼──────────╢
║ 127.0.0.0   	│ None │ None     ║
║ 127.0.0.1  	│ 445  │ TCP      ║
╚═══════════════╧══════╧══════════╝
```

**Very Verbose Output :**
```
Very Verbose output will include IP addresses with no results and display them in real-time.

# python3 usefulShodan2.py targets.txt -vv

[08:01:03] ('127.0.0.0', None,None)
[08:01:04] ('127.0.0.1', 445,TCP)

         UsefulShodan2.py
╔═══════════════╤══════╤══════════╗
║ IP Address    │ Port │ Protocol ║
╟───────────────┼──────┼──────────╢
║ 127.0.0.0   	│ None │ None     ║
║ 127.0.0.1  	│ 445  │ TCP      ║
╚═══════════════╧══════╧══════════╝
```

**Results to Database:**
```
Results are saved to the SQLite3 database 'database.db' in the main directory. 
Viewing the database with 3rd party software such as 'DB Browser for SQLite' is recommended.

.
..
database.db
README.md
requirements.txt
usefulShodan2.py
utils
```

**Delete Results in Database:**
```
To delete saved results stored in the database, launch usefulShodan2 with the [-d, --drop] flag. 
This will purge all existing data and allow usefulShodan to start with a fresh database.

# python3 usefulShodan2.py targets.txt -d
# python3 usefulShodan2.py targets.txt -vv -d
```
