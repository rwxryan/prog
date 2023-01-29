#!/bin/python3

import sys
import socket
from datetime import datetime

#First, we define the target
if len(sys.argv) == 2:
	target = socket.gethostbyname(sys.argv[1]) #translate hostname to IPV4
else:
	print("Invalid amount of arguments.")
	print("Syntax: python3 scanner.py <ip>")

#The above is saying we need 2 arguments (using argv) (comeback to define sys)
#If it doesn't meet this number of arguments it will return the custom error message defined in the print statements
#eg. if 1 argument (eg. python scanner.py) is given, it will break. If 3 arguments are given (eg. python3 scanner.py 127.1.1.1 scan), it will also break
#This doesn't account for things like not putting in a valid hostname or IP address though, so we need to figure that out.
#This isn't great logic, but it works for this proof of concept
#So we need to make sure that it accepts only valid IP addresses
#We need to think about how a user could break this while running it

#Adding a pretty banner
print ("-" * 50) #This prints 50 dashes
print ("Scanning target: "+target) #This prints the target defined in the target variable on line 9, the translated IPV4 IP address
print ("Time started: "+str(datetime.now())) #This prints the time that the scan started by calling the date and time and making it a string as we can't concatenat strings
print ("-" * 50) #This prints 50 dashes

#Use the try command

try:
	for port in range(50,85): #We are defining a for loop to scan only ports 50 through to 85 as it is not a threaded scanner and will probably run slow. These port numbers we choosen as we will attempt to scan our home router and DNS is usally open plus port 80
		s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #This sets a variable of s to equal the IP address - AF_INET, and the port we are trying to connect to - SOCK_STREAM
		socket.setdefaulttimeout(1) #This sets the default timeout to 1 sec. IF the port doesn't respond, the script should move on to the next
		result = s.connect_ex((target,port)) #defines the variable result as the target variable (supplied by us when running the script) and the variable port that we are declaring on this line. It is picked up in the for loop on line 31 and limited to the range given on the same line. The s.connect_ex is an error indicator. If the port is open it will return a 0, if it is closed it will return a 1.
		if result == 0: #So this tells the script what to do when the port is open
			print(f"Port {port} is open") #prints the string and lists the port thats open
		s.close() #if it's closed, we are going to close the loop here and get the script to go back through the for loop. How does this close the loop and how does the script know to iterate to the next port number?

#before we can run this we need to write in some exceptions that could break the script

#So we can hit Ctrl+C (close) and exit the program while it's running in our command line

except KeyboardInterrupt:
	print("\nExiting program.") #Prints the string on a newline
	sys.exit() #allows us to exit gracefully. Figure out what this means

except socket.gaierror: #Figure out what this means. Something to do with hostname not resolving
	print("Hostname could not be resolved.") #eg. python3 scanner.py gergeber can't be resolved
	sys.exit()

except socket.error:
	print("Couldn't connect to the server.")
	sys.exit()

#Right now I can't get it to return any open ports against what i think is my home router as suggested the the TCM video
#This video is on Youtube.com/watch?v=3FNYvj2UOHM between timecodes 5:23:11-5:41:44

#To do: is it possible to add something that prints to screen when it is iterating through each port number so you can identify where the scanner is a in its process?
#This may help with troubleshooting  

#My bad, it is just very slow. Took approx 3mins to return two open ports then the scan was finished.

#To do: Add an print statement for when the scanner finishes
#To do: Check and make sure the exceptions work properly
