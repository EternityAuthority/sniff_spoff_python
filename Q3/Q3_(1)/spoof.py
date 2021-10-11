#!/bin/ python3
import os

os.sys.path.append('/home/eternity/.local/lib/python3.8/site-packages')

from scapy.all import *

ip = IP()
ip.dst = '192.168.9.129'
ip.src = '8.8.8.8'

icmp = ICMP()

packet = ip/icmp

send(packet)
