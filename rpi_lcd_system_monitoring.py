#!/usr/bin/python

import socket
from i2clibraries import i2c_lcd_smbus
import time
import subprocess
import os
import psutil
	
def get_temperature():
	try:
		s = subprocess.check_output(["/opt/vc/bin/vcgencmd","measure_temp"])
		return float(s.split('=')[1][:-3])
	except:
		return 0

def get_cpu_usage():
	try:
		return psutil.cpu_percent(interval = .5)
	except:
		return 0

lcd = i2c_lcd_smbus.i2c_lcd(0x27,1, 2, 1, 0, 4, 5, 6, 7, 3)
lcd.command(lcd.CMD_Display_Control | lcd.OPT_Enable_Display)
lcd.backLightOn()

while True:
	node = "#0"
	temperature = str(get_temperature()) + chr(223) + "C"
	cpu = str(get_cpu_usage()) + "%"
	lcd.setPosition( 1, 0 )
	lcd.writeString(node + " " + temperature + " " + cpu + " ")
	time.sleep(2)



