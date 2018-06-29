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
 

 

# =============================================================================
# path = os.path.join(os.getcwd(),'train_set_6')
# files = os.listdir(path)
# cur = conn.cursor()
# for ii,ff in enumerate(files):
#     print(ii,len(files))
#     FilePath = os.path.join(path,ff)
#     tel = SaveToBinart(FilePath)
#     Open = 1
#     nn = 0;
#     while Open:
#         try:  
#             #sqlstr = "insert into table01 values({},{})".format(nn,sqlite3.Binary(tel))
#             sql ="INSERT INTO table01(tel) VALUES (?)" 
#             conn.execute(sql, (sqlite3.Binary(tel) ))
#             conn.execute(sql)
#             Open = 0
#         except:
#             nn += 1
#             print(nn)
#             sad
# =============================================================================
        


path = os.path.join(os.getcwd(),'train_set_6')
files = os.listdir(path)    
con = lite.connect('Test.sqlite') 

with con:
    for ii,ff in enumerate(files): 
        print(ii,len(files))
        FilePath = os.path.join(path,ff)
        data = SaveToBinart(FilePath)
        cur = con.cursor() 
# =============================================================================
#         cur.execute("CREATE TABLE IF NOT EXISTS Docs(Data BLOB)") 
#         sql ="INSERT INTO Docs(Data) VALUES (?)" 
#         cur.execute(sql, (lite.Binary(data),))
# =============================================================================
        
        cur.execute('CREATE TABLE IF NOT EXISTS Docs ("Data" BLOB,"name" TEXT)')
        sql ="INSERT INTO Docs(Data,name) VALUES (?,?)" 
        cur.execute(sql, (lite.Binary(data), ff, )) 
         

con = lite.connect('Test.sqlite') 
test = con.execute('select * from Docs')
row = test.fetchall()

# =============================================================================
# con.commit()
# con.close()
# =============================================================================
# =============================================================================
# cur.close()
# con.commit()
# con.close()
# =============================================================================
