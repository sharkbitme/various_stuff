#!/usr/bin/env python
"""
This script attempts to enumerate cold fusion administrative interfaces
probably poorly, ill bet this thing is slow, will improve it eventually
usage: python cf_enum.py <file> where file is standard list of ip
addresses or names. 

"""
import requests
from requests.exceptions import ConnectionError
import sys
if len(sys.argv) != 2:
	print("Input file not specified! Usage: python cf_enum.py <target_filename>")
	sys.exit(0)
target_file = sys.argv[1]
f = open(target_file, 'r')
cfide_admin_path = '/CFIDE/administrator/index.cfm'
for host in f:
    host = host.rstrip('\n')
    r = 'http://' + host + cfide_admin_path
    try:
        results=requests.get(r, allow_redirects=True, verify=False, timeout=0.5)
        #print(results.url)
        if results.status_code == 200:
            print(results.url)
        else:
            continue
    except requests.exceptions.RequestException as e:
	    print e
            continue
