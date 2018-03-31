#!/usr/bin/python

import subprocess
import os

def get_ram():
    try:
        s = subprocess.check_output(["free","-m"])
        lines = s.split('\n')
        return ( int(lines[1].split()[1]), int(lines[2].split()[3]) )
    except:
        return 0

def get_processes_count():
    try:
        s = subprocess.check_output(["ps","-e"])
        return len(s.split('\n'))
    except:
        return 0

def get_temperature():
    try:
        s = subprocess.check_output(["/opt/vc/bin/vcgencmd","measure_temp"])
        return float(s.split('=')[1][:-3])
    except:
        return 0

def get_ip_address():
    arg='ip route list'
    p=subprocess.Popen(arg,shell=True,stdout=subprocess.PIPE)
    data = p.communicate()
    split_data = data[0].split()
    ipaddr = split_data[split_data.index('src')+1]
    return ipaddr

def get_cpu_speed():
    f = os.popen("/opt/vc/bin/vcgencmd get_config arm_freq")
    cpu = f.read()
    return cpu

print "Free RAM: "+str(get_ram()[1])+" "+str(get_ram()[0])
print "Nr. of processes: "+str(get_processes_count())
print "Temperature in C: "+str(get_temperature())
print "IP address: "+str(get_ip_address())
print "CPU speed: "+str(get_cpu_speed())