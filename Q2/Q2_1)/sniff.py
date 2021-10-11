#!/bin/ python3
import os

os.sys.path.append('/home/eternity/.local/lib/python3.8/site-packages')
from scapy.all import *

def print_pkt(pkt):
  pkt.show()
  
pkt = sniff(filter='icmp', prn=print_pkt)
