#!/usr/bin/env python
"""
This script attempts to enumerate cold fusion administrative interfaces
usage: python cf_enum.py <ip_addr> where ip_addr is ip address or hostname

"""
import requests
import sys
if len(sys.argv) != 2:
	print("Target not specified! Usage: python cf_enum.py <target_ip_addr>")
	sys.exit(0)
host = sys.argv[1]

cfide_admin_path = '/CFIDE/administrator/index.cfm'
r = requests.get('http://' + host + cfide_admin_path, allow_redirects=True, 
verify=False, timeout=3)
	#print(r.url)
if r.status_code == 200:
	print(r.url)
