#!/usr/bin/env python3

from rich.console import Console
from rich.logging import RichHandler
from rich.table import Table
from rich import box
from rich.theme import Theme
import logging


# Rich console and theme init.
themefile = './utils/theme.ini'
mytheme = Theme().read(themefile)
console = Console(theme=mytheme)

# logger - Rich
logging.basicConfig(
	# filename='',
	level='WARNING',
	format='%(message)s',
	datefmt='[%X]',
	handlers=[RichHandler(console=console, rich_tracebacks=True)]
	)
logging = logging.getLogger('rich')