from pytube import YouTube 
import win32ui
import os

 


def LoadAllUrl(fileName):
    fp = open(fileName,"+r")
    line = fp.readline()
    AllUrl = [];
    while line:
        AllUrl.append(line);
        line = fp.readline();
        #print(line)    
    fp.close;
    print("---- 所有網址讀取完畢,總共有 " + str(len(AllUrl))+ " 筆")
    return AllUrl

def ytDownLoad(url,SavePath):        
    yt = YouTube(url)
    streamsType = yt.streams.filter(file_extension='mp4').all() 
    SaveName = yt.title
    print(" " + SaveName + CreatBlock(60-len(SaveName)),end = '')
    
     
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
        downLoadStreams.download(SavePath)    
        print(" ---- " + "下載完成")
           
        

 
def main_DownLoad(AllUrl,SavePath):
    kk = 0
    for v in AllUrl:
        try:
            kk += 1 
            print("---- 第" + str(kk) + "首 : " ,end = '')
            ytDownLoad(v,SavePath) 
        except:
            print(" " + CreatBlock(60) + " ---- 下載失敗" )
        
def CreatDir():
    try:
        os.mkdir('0_AllVideo')
    except:
        pass
 
def CreatBlock(num):
    kk = ''
    for i in range(0,num):
        kk = kk + ' '
    return kk


  

 
Inp = input('---- 輸入任意健開始執行 : ')
print("---- 開始執行")
path = os.getcwd() 
listdir = os.listdir(path)
for dd in listdir:
    if dd.find('.txt') != -1:
        FileName = dd
        CreatDir()
        SavePath = path + '\\0_AllVideo'
        AllUrl = LoadAllUrl(FileName) 
        main_DownLoad(AllUrl,SavePath)  
print(" ")  
print(" ")  
while 1:
    key = input("---- 檔案下載結束 輸入quit 結束程式 : ")
    if key == 'quit':
        exit() 
      
         



        
 
#main_DownLoad(AllUrl)   
        





 
#while 1:
   # Inp = input('輸入 path 來選擇txt檔 : ')
   # if Inp == 'path':
        #dlg = win32ui.CreateFileDialog(1) # 1表示打开文件对话框
        #dlg.SetOFNInitialDir() # 设置打开文件对话框中的初始显示目录
        #dlg.DoModal() 
        #filename = dlg.GetPathName() # 获取选择的文件名称
        #if filename[-4:] == '.txt':
            #lastPath,fileName = os.path.split(filename)
            #AllUrl = LoadAllUrl(fileName) 
            #print("讀檔完成 , 總共有 : " + str(len(AllUrl)) + "首歌")
        #print("asdasdasdasd")
        #os.system("pause")
          #  main_DownLoad(AllUrl)




















