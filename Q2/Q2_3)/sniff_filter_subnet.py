#!/bin/ python3
import os

os.sys.path.append('/home/eternity/.local/lib/python3.8/site-packages')
from scapy.all import *

def print_pkt(pkt):
  pkt.show()
  
pkt = sniff(filter='net 128.230.0.0/16', prn=print_pkt)
