import tkinter as tk
import tkinter.filedialog as filedialog
import os
import requests
from bs4 import BeautifulSoup 
from pytube import YouTube 
import time
import threading


 
        



       
        
class GUI:
    
    def __int__(self,title,geo):
        self.title = title
        self.geo = geo
    
    def CreatGUI(self):
        ww = tk.Tk()
        ww.title( 'Youtube Downloader')
        ww.geometry('800x400')
        ww.resizable(0,0) 
        
        Fra_1 = tk.Frame(ww,width = 450)
        Fra_1.pack()
        
        labPath = tk.Label(Fra_1,text = '儲存路徑 : ')
        labPath.grid(row = 0 , column = 0,padx = 5, sticky = "w")
        
        
        txtPath = tk.Text(Fra_1,width = 80,height = 1,bg = 'white')
        txtPath.insert('insert',os.getcwd())
        
        txtPath.grid(row = 0 , column = 1,padx = 5, sticky = "w")
        txtPath.config(state = tk.DISABLED)
        
        btnPath = tk.Button(Fra_1,text = '選擇路徑',width = 8,height = 1,command = btn_SelectPath)
        btnPath.grid(row = 0 , column = 2,padx = 5, sticky = "w")
        
         
        txtShow = tk.Text(ww ,width = 100,height = 25,bg = 'white')
        txtShow.pack(pady = 5)
        
        btnStart = tk.Button(ww,text = '執行',width = 8,height = 1,command = btn_StartDownLoad)
        btnStart.place(relx = 0.858, rely = 0.91)
        ww.mainloop() 


    def ytDownLoad(url):        
        yt = YouTube(url)
        streamsType = yt.streams.filter(file_extension='mp4').all() 
        SaveName = yt.title
        String = " " + SaveName + CreatBlock(60-len(SaveName))
        txtShow.insert('insert',String)  
        
        
         
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
            downLoadStreams.download(os.getcwd() + '\\0_AllVideo' )    
            String = "  下載完成\n"
            txtShow.insert('insert',String)  
               
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
                String = "---- 第" + str(kk) + "首 : "
                txtShow.insert('insert',String)  
                ytDownLoad(v) 
            except:
                String = CreatBlock(61) +  "  下載失敗\n" 
                txtShow.insert('insert',String)  
    
    
            
            
    def btn_SelectPath():
        filepath = filedialog.askdirectory()
        if filepath:
            txtPath.config(state = tk.NORMAL)
            txtPath.delete(1.0,tk.END)
            txtPath.insert('insert',filepath)
            txtPath.config(state = tk.DISABLED)
        else:
            filepath = os.getcwd()
    
    def btn_StartDownLoad():
        
        try:
            pa = txtPath.get(0.0,tk.END) 
            os.mkdir(pa.split('\n')[0] + '\\0_AllVideo') 
        except:
            pass
        
        fileName = findTxtFile()
        listUrl = loadTxt(fileName)
        String = '---- 總共有 ' + str(len(listUrl)) +' 個播放清單 \n'
        txtShow.insert('insert',String) 
        kk = 0
        for vv in listUrl:
            kk += 1
            AllUrl = GetYoutubeListUrl(vv)
            String = '---- 正在處理第 ' + str(kk) +' 個播放清單\n'
            txtShow.insert('insert',String) 
            String = '---- 第'+ str(kk) + '個播放清單有 : ' + str(len(AllUrl)) + '首\n'
            txtShow.insert('insert',String)  
            time.sleep(10)
            #break
            #main_DownLoad(AllUrl)
            aa = threading.Thread(target =  main_DownLoad(AllUrl))
            aa.start()
            









gg = GUI()
gg.CreatGUI()








