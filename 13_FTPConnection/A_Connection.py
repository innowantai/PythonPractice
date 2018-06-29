import os
import re
from ftplib import FTP
from firebase import firebase

# =============================================================================
# with open('0_Account.txt','r') as f:
#     data = f.read().split(',') 
# IP       = data[0]
# ACCOUNT  = data[1]
# PASSWORD = data[2]
# PORT     = data[3]
# =============================================================================
    
url = 'https://savetrying.firebaseio.com/'
fb = firebase.FirebaseApplication(url,None)
Data = fb.get('/FTP',None)


IP       = Data['IP']
ACCOUNT  = Data['Account']
PASSWORD = Data['PassWord']
PORT     = Data['Port']



url = 'https://savetrying.firebaseio.com/Time1/'
fb = firebase.FirebaseApplication(url,None)
 






ftp = FTP(IP, ACCOUNT, PASSWORD)
ftp.encoding = 'utf-8'
path = '/imc Raw Data/中部科學園區管理局 結構監測系統'
rr = r'-'

 
print('---- 連至地震中心 FTP 下載監測資料')
print('---- 持續偵測 FTP 是否有新增資料並自動下載')
AfterDate = input("---- 輸入日期(格式如 20180520)針對此日期之後資料夾進行下載 : ")
#AfterDate = '20180501'
kk = 0
while 1:
    kk += 1
    try:        
        ftp.cwd(path)
        TopFolder = ftp.nlst() 
        for FOLDER in TopFolder:
            if len(re.findall(rr,FOLDER)) == 4:            
                Num = int(FOLDER[0:4] + FOLDER[5:7] + FOLDER[8:10])         
                if Num >= int(AfterDate):             
                    RawPath = os.path.join(path,FOLDER)
                    ftp.cwd(RawPath)
                    RawFiles = ftp.nlst()
                    
                    if not os.path.exists(FOLDER):
                        os.mkdir(FOLDER)  
                    
                    for file in RawFiles:
                        kk += 1
                        SavePath = os.path.join(os.getcwd(),FOLDER,file) 
                        if not os.path.exists(SavePath) or os.path.getsize(SavePath) < 1400000 :                         
                            print('\n---- 正在下載 ',FOLDER,file, end = '')
                            with open(SavePath,'wb') as F:
                                filename = 'RETR ' + file      
                                ftp.retrbinary(filename,F.write)                                    
                            print(' 下載完成 ----',end = '')
                            kk = -2
                        else:
                            if kk == -1:
                                print('  ')
                            elif kk % 5 == 0:    
                                print('\r---- Waitting                                                                 ', end = '')                            
                            elif kk % 5 == 1:    
                                print('\r---- Waitting .                                                               ', end = '')                            
                            elif kk % 5 == 2:    
                                print('\r---- Waitting ..                                                              ', end = '')                            
                            elif kk % 5 == 3:                            
                                print('\r---- Waitting ...                                                             ', end = '')                         
                            elif kk % 5 == 4:                            
                                print('\r---- Waitting ....                                                            ', end = '')
                            
            print('\r---- Waitting                                                                                    ', end = '')
                    
    except:
        ftp = FTP(IP, ACCOUNT, PASSWORD)
        ftp.encoding = 'utf-8'
        path = '/imc Raw Data/中部科學園區管理局 結構監測系統'
        #print('Connection Error : Re-Connect\n\n\n')






# Num = int(FOLDER[0:4] + FOLDER[5:7] + FOLDER[8:10] + FOLDER[11:13] + FOLDER[14:16] + FOLDER[17:18])


