# -*- coding: utf-8 -*-
"""
Created on Tue Mar  6 15:01:02 2018

@author: 1804002
"""

from inout import InitIO
import io
import os

FILE_BEGIN_TAG  = b'FILEBEG0'
FILE_END_TAG    = b'FILEEND0'
FILE_SIZE_TAG   = b'FILESIZE'
FILE_NAME_TAG   = b'FILENAME'
FILE_CONTENT_TAG= b'FILEDATA'
FILE_BLOCKS_TAG = b'FILEBLKS'
FILE_SUCESS_TAG = b'FILEGOOD'
FILE_FAIL_TAG   = b'FILEFAIL'
FILE_ABORT_TAG  = b'FILEABRT'
FILE_TAG_SIZE   = len(FILE_BEGIN_TAG)



class NetAPI:
   

    def __init__(self, iHandle = None , oHandle = None):     
        if not iHandle:
            iHandle = b''
        if not oHandle:
            oHandle = iHandle
        self.iHandle = InitIO(iHandle)
        self.oHandle = InitIO(oHandle)
        self.savePath = 'C:\\'
        self.maxSize = 2147483647
        self.blockSize = 4096
        
        
    def recv_data(self):    return self.iHandle.read()
    def send_tag(self,tag) :     return self.oHandle.write_raw(tag)
    def send_data(self,data):    return self.oHandle.write(data)
    
    
    def send_file(self,path):  
        filename = '\t'.join(split_path(path))
        filesize = os.path.getsize(path)
        filedata = open(path,'rb').read()
        try: 
            self.send_tag(FILE_NAME_TAG)
            self.send_data(filename)
            self.send_tag(FILE_SIZE_TAG)
            self.send_data(filesize)
            self.send_tag(FILE_CONTENT_TAG)
            self.send_data(filedata)
            self.send_tag(FILE_END_TAG)
        except Exception as e:
            print(str(e))
            self.send_tag(FILE_ABORT_TAG)
            return False
        
    
    def recv_file(self):  
        result = {}
        while True:
            tag =self.recv_tag()
            if not tag or tag in [FILE_END_TAG, FILE_ABORT_TAG] : break
            data = self.recv_data()
            if not data : break
            if tag == FILE_NAME_TAG:
                namelist = data.split('\t')
                if '..' in namelist:
                    raise ValueError('Dangerous path')
                data = os.path.join(*namelist) 
            #print(tag,data)
            result[tag] = data
        return result
    


    def recv_tag(self):  return self.iHandle.read_raw(FILE_TAG_SIZE)
    
    def send_size(self,n):      pass
    def send_name(self,s):      pass
    def send_content(self,d):   pass

    def recv_size(self):        
        size = self.recv_data()
        if not isinstance(size,int):
            raise TypeError('Invalid size type &s' % type(size))
        return size
    
    def recv_name(self):        
        path = self.recv_data()
        if not isinstance(path,str):
            raise TypeError('Invalid name type &s' % type(path))
        namelist = path.split('\t')
        if '..' in namelist:
            raise ValueError('dangerous path')
        name = os.path.join(*namelist)
        return name
    
    def recv_content(self):     pass

    def send_success(self):     pass
    def send_fail(self):        pass
    def send_abort(self,n):     pass
















def split_path(path):
    result = []
    while True:
        head, tail = os.path.split(path)
        if tail:
            result.insert(0,tail)
            path = head
        else:   
            head = head.strip('/:\\')
            result.insert(0,head)
            break
    return result


























        
