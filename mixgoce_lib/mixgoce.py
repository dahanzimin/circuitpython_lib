# Paste mixgoce.py
# Optimize requests  	—— dahanzmin 2205012

import board
from rtc import RTC
from busio import I2C

def do_connect(username, password):
	import wifi
	from time import sleep
	
	wifi.radio.connect(ssid=username.encode(), password=password.encode())
	while not wifi.radio.ipv4_address:
		sleep(0.1)
	print("Wi-Fi connected!")
	return wifi.radio

rtc_clock = RTC()

try:
	i2c = I2C(board.IO41, board.IO42,frequency=400000)
	while not i2c.try_lock():
		pass
	if 0x6a in i2c.scan():
		version = 99
	elif 0x15 in i2c.scan():
		version = 1
	else:
		version = 0
		
	i2c.unlock()
	
	if version == 99:
		i2c.deinit()
	elif version:#new
		import mxc6655xa
		acc = mxc6655xa.MXC6655XA(i2c)
	
		def get_temperature():
			return acc.get_temperature()
	else:#old
		import msa301
		acc = msa301.MSA301(i2c)
		
except Exception as e:
	print(e)

ADDITIONAL_TOPIC = 'b640a0ce465fa2a4150c36b305c1c11b'
WILL_TOPIC = '9d634e1a156dc0c1611eb4c3cff57276'

def requests_init():
	import ssl
	import wifi
	import socketpool
	import adafruit_requests
	pool = socketpool.SocketPool(wifi.radio)
	requests = adafruit_requests.Session(pool, ssl.create_default_context())
	return requests

requests=None
	
def ntp(url='http://mixio.mixly.org/time.php'):
	global requests
	if requests is None:
		requests=requests_init()	
	try:
		response = requests.get(url)
	except Exception as e:
		raise RuntimeError("Maybe WiFi is not connected",e)	
	return tuple(response.text.split(","))
	
def analyse_sharekey(url):
	import json
	global requests
	if requests is None:
		requests=requests_init()
	try:
		response = requests.get(url)
	except Exception as e:
		raise RuntimeError("Maybe WiFi is not connected",e)
	if response.text == '-1':
		raise RuntimeError('Invalid share key')
	else:
		result = json.loads(response.text)
		return (result['0'], result['1'], result['2'])