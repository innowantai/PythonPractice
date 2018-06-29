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
        
        self.Fra_1 = tk.Frame(ww,width = 450)
        self.Fra_1.pack()
        
        self.labPath = tk.Label(self.Fra_1,text = '儲存路徑 : ')
        self.labPath.grid(row = 0 , column = 0,padx = 5, sticky = "w")
        
        
        self.txtPath = tk.Text(self.Fra_1,width = 80,height = 1,bg = 'white')
        self.txtPath.insert('insert',os.getcwd())
        
        self.txtPath.grid(row = 0 , column = 1,padx = 5, sticky = "w")
        self.txtPath.config(state = tk.DISABLED)
        
        self.btnPath = tk.Button(self.Fra_1,text = '選擇路徑',width = 8,height = 1,command = self.btn_SelectPath)
        self.btnPath.grid(row = 0 , column = 2,padx = 5, sticky = "w")
        
         
        self.txtShow = tk.Text(ww ,width = 100,height = 25,bg = 'white')
        self.txtShow.pack(pady = 5)
        
        btnStart = tk.Button(ww,text = '執行',width = 8,height = 1,command = self.btn_StartDownLoad)
        btnStart.place(relx = 0.858, rely = 0.91)
        ww.mainloop() 
    
            
      
    def btn_SelectPath(self):
       filepath = filedialog.askdirectory()
       if filepath:
           self.txtPath.config(state = tk.NORMAL)
           self.txtPath.delete(1.0,tk.END)
           self.txtPath.insert('insert',filepath)
           self.txtPath.config(state = tk.DISABLED)  
       else:
           filepath = os.getcwd()
        
    def btn_StartDownLoad(self):       
        try:
            pa = self.txtPath.get(0.0,tk.END) 
            os.mkdir(pa.split('\n')[0] + '\\0_AllVideo')  
            aa = threading.Thread(target = self.run())
            aa.start()
        except:
            pass
    
    def run(self):
        kk = 0
        while kk < 500:
            a = 1000*1000
            self.txtShow.insert('insert',str(kk) + '\n')
            kk+=1
        
            


 


gg = GUI()
gg.CreatGUI()








