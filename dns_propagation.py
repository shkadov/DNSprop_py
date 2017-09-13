#!/bin/python

import os
import socket
import time

host = 'FQDN'
a = socket.gethostbyname(host)
while(True):
    if a != 'target_ip':
        print("DNS has not been propagated yet")
        time.sleep(600)
    else:
        print("DNS has been propagated")
    break


