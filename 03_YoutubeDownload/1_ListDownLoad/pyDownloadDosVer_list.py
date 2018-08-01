# -*- coding: utf-8 -*-
"""
Created on Fri Mar 23 13:19:30 2018

@author: 1804002
"""

# -*- coding: utf-8 -*-
"""
Created on Fri Mar 23 07:55:05 2018

@author: 1804002
"""

 
 
def ytDownLoad(url):        
    yt = YouTube(url)
    streamsType = yt.streams.filter(file_extension='mp4').all() 
    SaveName = yt.title
    print(" " + SaveName + CreatBlock(60-len(SaveName)) ,end = '')
    
     
    Res = ["1080p" ,"720p", "480p", "360p"]
    Target = {"1080p":"" , "720p":"" , "480p":"" , "360p":"" } 
    flag = 0 
    kk = 0
    for v in streamsType:
        index = str(v)
            # print(index)
        for ii in range(0,4):     
            if index.find(Res[ii]) != -1 and index.find("mp4a.") != -1 and v.includes_audio_track: 
               flag = 1
               Target[Res[ii]] = kk 
        kk += 1 
    
    if flag != 0: 
        for ii in range(0,4):
            if Target[Res[ii]] != "":
                downLoadStreams = streamsType[Target[Res[ii]]]
                #fileList = [Res[ii],str(downLoadStreams.fps)]
                break 
        downLoadStreams.download(os.path.join(os.getcwd(), '0_AllVideo' ))    
        print("  下載完成")
           
def findTxtFile():    
    filelist =  os.listdir()
    fileName = ''
    for vv in filelist:
        if '.txt' in vv:
            fileName = vv;
            break
    return fileName

def loadTxt(fileName): 
    fp = open(fileName,'r')
    data = fp.readline()
    url = []
    while data: 
        url.append(data.rstrip('\n'))
        data = fp.readline()
    return url
        
def GetYoutubeListUrl(url): 
    html = requests.get(url)
    html.encoding = 'utf-8'
    sp = BeautifulSoup(html.text,'html.parser')  
    data2 = sp.find_all('a',{'class':' spf-link playlist-video clearfix yt-uix-sessionlink spf-link '}) 
    
    UrlAll = []
    for vv in data2:
        urlIndex = "https://www.youtube.com" + vv.get('href')
        UrlAll.append(urlIndex) 
    return UrlAll

def CreatBlock(n):
    vv = ''
    for i in range(0,n+1):
        vv += ' '
    return vv
    
    
def main_DownLoad(AllUrl):
    kk = 0
    for v in AllUrl:
        try:
            kk += 1 
            print("---- 第" + str(kk) + "首 : " ,end = '')
            ytDownLoad(v) 
        except:
            print(CreatBlock(61) +  "  下載失敗" ) 
 




from pytube import YouTube 
import os
import requests
from bs4 import BeautifulSoup 
 

 
try:
    os.mkdir('0_AllVideo')
except:
    pass
    

fileName = findTxtFile()
listUrl = loadTxt(fileName)
 


    
Inp = input('---- 輸入任意鍵開始執行 : ')
print('---- 總共有 ' + str(len(listUrl)) +' 個播放清單')
kk = 0
for vv in listUrl:
    kk += 1
    AllUrl = GetYoutubeListUrl(vv)
    print('---- 正在處理第 ' + str(kk) +' 個播放清單')
    print('---- 第'+ str(kk) + '個播放清單有 : ' + str(len(AllUrl)) + '首')
    main_DownLoad(AllUrl)
         
    
#os.system("pause")

        





 





















