#!/bin/ python3
import os

os.sys.path.append('/home/eternity/.local/lib/python3.8/site-packages')
from scapy.all import *

def print_pkt(pkt):
  pkt.show()
  
pkt = sniff(filter='tcp and src host 10.0.2.4 and dst port 23', prn=print_pkt)
