import os
import argparse
import hashlib 

# ANSI Colors
class Color:
	# If you wish to use custom colors add them here and change the varibles below
    PURPLE = '\033[95m'
    CYAN = '\033[96m'
    DARKCYAN = '\033[36m'
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    BLINKING = '\033[5m'
    RESET = '\033[0m'

ActiveColor = Color.GREEN
QuestionColor = Color.BOLD+Color.YELLOW
ErrorColor = Color.RED
NumColor = Color.PURPLE+Color.BOLD
NotificationColor = Color.CYAN
RESET = Color.RESET


# Setting Up Arguments 
parser = argparse.ArgumentParser()
parser.add_argument("File",help="File to pass into the Verify Function")
parser.add_argument("Hash",help="Hash of the File to Verify")
Arguments = parser.parse_args()


# MD5 Verification Script

def GetHash(FileName):
	MD5 = hashlib.md5() 
	with open(FileName,"rb") as f:
	    for Block in iter(lambda: f.read(4096),b""):
	        MD5.update(Block)
	return(MD5.hexdigest())

def CompareHashes(HashAttempt,AuthHash):
	print(f"{ActiveColor}\nStarting Hash Comparison \n{RESET}")
	if HashAttempt == AuthHash: 
		print(f"{ActiveColor}Hashes Are Identical{RESET}")
	else: 
		print(f"{ErrorColor}Hashes Are Different\n\nCalculated : {HashAttempt}\nProvided : {AuthHash}{RESET}")

HashAttempt = GetHash(Arguments.File)
CompareHashes(HashAttempt,Arguments.Hash)
