#!/usr/bin/python

import sys

def utf8_print(string=''):
	sys.stdout.buffer.write(string.encode('utf8') + b'\n')

# Turn on debug mode.
import cgitb
cgitb.enable()

# Print necessary headers.
utf8_print("Content-Type: text/html")
utf8_print()


with open('index.template.html', 'r', encoding='utf-8') as template_file:
	template = template_file.read()
	template_file.close()

	utf8_print(template)

