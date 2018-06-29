# -*- coding: utf-8 -*-
"""
Created on Tue Mar  6 15:39:29 2018

@author: 1804002
"""

import socket



serverSocket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
serverSocket.bind((socket.gethostname(),1234,))
serverSocket.listen(5)


while True:
    conn , addr = serverSocket.accept()
    try:
        while conn:
            data = conn.recv(1024)
            print(data.decode())
            if data == b'':
                conn = False
    except:
        pass