#!/usr/bin/env python
#Author: infosecblay
#company: inveteck global
import re,sys
ipp = re.compile(r'(\d+).(\d+).(\d+).(\d+)')
try:
	def call(ip):
		mo = ipp.search(ip)
		v = int(mo.group(1)) * pow(2,24) + int(mo.group(2)) * pow(2,16) + int(mo.group(3)) * pow(2,8) + int(mo.group(4)) * pow(2,0)
		print ("Your ip int value is: "+str(v))
		print ("")

	ip=raw_input("Enter ip:")
	call(ip)
except KeyboardInterrupt:
	print("You entered an invalid key.Exitting...")
	sys.exit()
	

