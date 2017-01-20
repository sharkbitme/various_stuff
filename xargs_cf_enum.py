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
	print("Target not specified! Usage: python cf_enum.py <target_ip_addr>")
	sys.exit(0)
host = sys.argv[1]

cfide_admin_path = '/CFIDE/administrator/index.cfm'
r = requests.get('http://' + host + cfide_admin_path, allow_redirects=True, 
verify=False, timeout=5)
	#print(r.url)
if r.status_code == 200:
	print(r.url)
