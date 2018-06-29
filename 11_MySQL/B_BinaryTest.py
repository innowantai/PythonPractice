import sqlite3 as lite
import numpy as np
import PIL
import cv2
import os


def ImgProcess(FilePath):
    test = []
    img = PIL.Image.open(FilePath).convert('RGB')
    img_array = np.array(img) 
    img_gray = cv2.cvtColor(img_array,cv2.COLOR_BGR2GRAY) 
    _, thresh = cv2.threshold(img_gray,230,255,1) 
    return thresh
    

def SaveToBinart(FilePath): 
    with open(FilePath,'rb') as ff:
        data = ff.read()  
    return data
 

  

 
con = lite.connect('Test.sqlite') 
Names = con.execute('select name from Docs')
test = con.execute('select Data from Docs')
row = test.fetchall()
Names = Names.fetchall()
path = os.path.join(os.getcwd(),'testFolder')
for ii,data in enumerate(row):  
    print(ii,len(row))
    path2 = os.path.join(os.getcwd(),'testFolder',Names[ii][0])
    with open(path2,'wb') as ff:
        ff.write(data[0])










