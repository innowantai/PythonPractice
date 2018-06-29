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


def send_fileName(fileName,cli):
    cli.send(fileName.encode())
    flag = cli.recv(1024).decode()
    return flag
    
    

fileName = 'text.txt'
fileName = 'TranTest.7z'
transSize = 1024*1024*1024

flag = send_fileName(fileName,cli)
print(flag)
fileSize = os.path.getsize(fileName)
with open(fileName,'rb') as fp:
    data = fp.read(transSize)
    ss = transSize
    while data != b'':
        cli.send(data)
        print(str(ss) + '/' +  str(fileSize))
        ss += transSize
        data = fp.read(transSize)  
        input('keep going')
        
    fp.close()


