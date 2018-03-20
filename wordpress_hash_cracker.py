#!/usr/bin/python
#--------------------------------------------------------
#~Wordpress Hash Cracker
#~By Cyb3rw0rM
#~Visit us on facebook for more scripts: https://www.facebook.com/BackTrack.Fan.Page
#~We love Pentesting
#--------------------------------------------------------
from passlib.hash import phpass
import time
import sys
import threading
#--------------------------------------------------------
class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
#--------------------------------------------------------
def logo():
    print bcolors.WARNING+ '''        


   ______      __   _____               ____       __  ___
  / ____/_  __/ /_ |__  /______      __/ __ \_____/  |/  /
 / /   / / / / __ \ /_ </ ___/ | /| / / / / / ___/ /|_/ / 
/ /___/ /_/ / /_/ /__/ / /   | |/ |/ / /_/ / /  / /  / /  
\____/\__, /_.___/____/_/    |__/|__/\____/_/  /_/  /_/   
     /____/                                               
         	Wordpress Hash Cracker
		     By Cyb3rw0rM 
	       #BackTrack Linux Fan Page
'''
logo()
#--------------------------------------------------------
hash =  raw_input("Hash > ") #~exemple : $P$BNUagMlYbp6Zr.yCTsszsPhco663Wf0
passl = "wordlist.txt" #~change it by wordlist name
threads = 1
try:
    plist = open(passl).readlines()
except:
    print bcolors.FAIL + "| We cant find 1 required list !"
#--------------------------------------------------------
def crack(password):
    hashed = phpass.verify(password, hash)
    hashedpass = str(hashed) + ":" + str(password)
    if hashedpass == "True:" + password :
	    print bcolors.OKGREEN + "+---------------------------------------+"
	    print bcolors.OKGREEN + "| Operation Completed !"
	    print bcolors.OKGREEN + "| HASH > " + " " + hash
	    print bcolors.OKGREEN + "| password >" + " " + password
	    print bcolors.OKGREEN + "+---------------------------------------+"
	    sys.exit(1)
#--------------------------------------------------------
print bcolors.OKBLUE + "+---------------------------------------+"
print bcolors.OKBLUE + "| Cracking Please Wait ..."
print bcolors.OKBLUE + "| Loaded %s passwords !" % len(plist) 
print bcolors.OKBLUE + "+---------------------------------------+"
for password in plist :
    password = password.rstrip()
    for i in xrange(threads):
        t = threading.Thread(target=crack(password))
        t.start()
#--------------------------------------------------------
