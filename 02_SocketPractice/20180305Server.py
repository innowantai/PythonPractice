# -*- coding: utf-8 -*-
"""
Created on Mon Mar  5 10:37:40 2018

@author: 1804002
"""

import socket

serverSocket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
serverSocket.bind((socket.gethostname(),1234,))
serverSocket.listen(5)



serverSocket.close()






























































 