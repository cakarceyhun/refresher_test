#!/usr/bin/python

import cgitb
import cgi
import os
import logging
import time

logging.basicConfig(filename="/tmp/test.log", level=logging.DEBUG)
logging.debug("Start")
cgitb.enable()

# Print necessary headers.
print("Content-Type: text/html")
print()

arguments = cgi.FieldStorage()
hash = arguments['hash'].value
filename = arguments['filename'].value
logging.debug("Start 2")

old_mtime = ''
logging.debug("Start 3")
try:
	f = open('/tmp/' + hash, 'r')
	old_mtime = f.read()
	f.close()
except FileNotFoundError:
	pass

new_mtime = str(os.path.getmtime(filename))
logging.debug("old=%s new=%s" % (old_mtime, new_mtime))

start = int(time.time())
while old_mtime == new_mtime:
	if int(time.time()) - start > 30:
		print('timeout')
		break
	new_mtime = str(os.path.getmtime(filename))
	time.sleep(0.1)
	logging.debug("while old=%s new=%s" % (old_mtime, new_mtime))
else:
	logging.debug("else old=%s new=%s" % (old_mtime, new_mtime))
	with open('/tmp/' + hash, 'w') as f:
		f.write(new_mtime)
		f.close()
	print('refresh')


