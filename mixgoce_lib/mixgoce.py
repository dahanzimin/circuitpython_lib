# Paste mixgoce.py

import board
from rtc import RTC
from busio import I2C

rtc_clock = RTC()

try:
	i2c = I2C(board.IO41, board.IO42,frequency=400000)
	while not i2c.try_lock():
		pass
		
	_scan=i2c.scan()
	if 0x15 in _scan:
		version = 1
	elif 0x26 in _scan:
		version = 0
	else:
		raise AttributeError("There is a problem with ACC")
	
finally:
	i2c.unlock()

if version:#new
	import mxc6655xa
	acc = mxc6655xa.MXC6655XA(i2c)

else:#old
	import msa301
	acc = msa301.MSA301(i2c)

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
