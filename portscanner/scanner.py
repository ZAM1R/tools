#!/bin/python3

import sys
import socket
from datetime import datetime

#shity scanner! :D

#Define our target
if len(sys.argv) == 2:
	target = socket.gethostbyname(sys.argv[1])
else:
	print("Invalid arguments.")
	sys.exit()

print("*" * 50)
print(f"Scanning: {target}")
print(f"Time started:{str(datetime.now())}")
print("*" * 50)

try:
	for port in range(70,100):
		s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		socket.setdefaulttimeout(1)
		result = s.connect_ex((target, port))
		print(f"Checking {port} port")
		if result == 0:
			print(f"The {port} is open.")
		s.close()
except KeyboardInterrupt:
	print("\n Exiting program.")
	sys.exit()

except socket.gaierror:
	print("Hostname could not be resolved.")
	sys.exit()

except socket.error:
	print("Could not connect to server.")
	sys.exit()
