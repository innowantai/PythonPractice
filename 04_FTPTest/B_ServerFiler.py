# -*- coding: utf-8 -*-
"""
Created on Mon Mar 26 13:30:10 2018

@author: 1804002
"""

import socket
import time


ser = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
ser.bind((socket.gethostname(),1234))
ser.listen(5)


def getFileName(conn):  
    try:
        Name = conn.recv(1024).decode() 
        conn.send(b'RcvOK')  
    except:
        Name = ''
        conn.send(b'RecNG')  
    return Name
    

recSize = 1024
while True:
    conn , addr = ser.accept()
    fileName = getFileName(conn)
    print(addr)
    try: 
        if fileName != '' :
            fileName = "ABC" + fileName
            print(fileName)
            with open(fileName,'wb') as fp:
                data = conn.recv(recSize)   
                kk = 0
                while data != b'':
                    fp.write(data) 
                    data = conn.recv(recSize)   
                    #conn.send(b'igotit')
                   # print( len(data))
                   # kk = kk + 1
                    
            
    except:
        pass
    













