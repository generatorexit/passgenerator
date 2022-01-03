import random
from string import digits
from string import punctuation
from string import ascii_letters
import os

reset = '\033[0m'
green = '\033[92m'
yellow = '\033[93m'
cyan = '\033[96m'

symb = ascii_letters + digits + punctuation

banner = cyan + """
----------------------------
Random Password Generator
coded by mksec
generatorexit@gmail.com
----------------------------

type 'q' to close the program.

""" + reset

def clear():
	if os.name == "nt":
		os.system("cls")
	else:
		os.system("clear")

def createpass():
	while True:
		try:
			ui = input(yellow + "Add title.(Github, Twitter etc...)>> "+ reset)
			if ui == "q":
				break
			secure_pass = random.SystemRandom()
			passwd = "".join(secure_pass.choice(symb) for i in range(18))
			print(cyan + f"[+] Your {ui} password is: " + green + passwd + reset)
			with open("passwords.txt", 'a') as passlist:
				passlist.write(f"Your {ui} password is: " + passwd + "\n")
		except:
			break
clear()
print(banner)
createpass()