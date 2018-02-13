#!/usr/bin/python
import itertools
for item in itertools.permutations('1udl1udl', 8):
	print("?" + "?".join(item))
	# if you want this output to go into a batch file use the following:
	#print("hashcat64.exe -m %1 %2 -w 2 -a 3 -1 fivespecials.hcchr " + "?" + "?".		join(item))
