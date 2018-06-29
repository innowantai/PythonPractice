# -*- coding: utf-8 -*-
"""
Created on Tue Mar  6 15:39:38 2018

@author: 1804002
"""

import socket 

import os
import time

cli = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
cli.connect((socket.gethostname(),1234))



while True:
    data = input('Input the words that you want to say :')
    cli.send(data.encode()) 
    if data == 'QUIT':
        break


