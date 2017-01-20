#!/usr/bin/env python
"""
This script attempts to enumerate cold fusion administrative interfaces
probably poorly, ill bet this thing is slow, will improve it eventually
usage: python cf_enum.py <file> where file is standard list of ip
addresses or names. 

"""
import requests
import sys
if len(sys.argv) != 2:
	print("Input file not specified! Usage: python cf_enum.py <target_filename>")
	sys.exit(0)
target_file = sys.argv[1]
f = open(target_file, 'r')
cfide_admin_path = '/CFIDE/administrator/index.cfm'

for host in f:
	host = host.rstrip('\n')
	r = requests.get('http://' + host + cfide_admin_path, allow_redirects=True, 
	verify=False)
	if r.status_code == 200:
		print(r.url)
	else:
		continue
