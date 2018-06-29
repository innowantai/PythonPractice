# -*- coding: utf-8 -*-
"""
Created on Tue Mar  6 15:39:38 2018

@author: 1804002
"""

import socket 
from netapi import NetAPI
import os

clientSocket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
clientSocket.connect((socket.gethostname(),1234))

handler = NetAPI(clientSocket)

path = os.getcwd()
fileName = '\\Testt.txt'
#fileName = '\\20170315.pptx'
handler.send_file(path + fileName)