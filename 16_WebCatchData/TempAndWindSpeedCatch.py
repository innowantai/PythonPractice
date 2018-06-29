


import requests  
from bs4 import BeautifulSoup
import os

def DownLoad_suv(Time,mon):
    url = "http://e-service.cwb.gov.tw/HistoryDataQuery/DayDataController.do?command=viewMain&station=C0D660&stname=%25E6%2596%25B0%25E7%25AB%25B9%25E5%25B8%2582%25E6%259D%25B1%25E5%258D%2580&datepicker="

    
    print("---- 開始下載 ")
    Result = []
    AllDay = day[int(mon)-1]
    for ii in range(1,day[int(mon)-1]+1):
        dd = '{:02d}'.format(ii)  
        url2 = url + Time + '-' + dd
        html = requests.get(url2)
        html.encoding = 'utf-8'
        sp = BeautifulSoup(html.text,'html.parser') 
        AllData = sp.find_all('tr')
        kk = 0
        for vv in AllData:
            if kk >= 3:
               # print(vv)
                data1 = vv.find_all('td')  
                temp = data1[3]
                wind = data1[6] 
                try:
                    temp = float(temp.getText())
                except:
                    temp = 0 
                
                try:
                    wind = float(wind.getText())
                except:
                    wind = 0 
                Result.append(str(temp) + ',' + str(wind)) 
            kk += 1  
        progress = '{:0.1f}'.format(ii/AllDay*100) 
        print("---- 下載進度 : " + progress + "%") 
    
    saveName = Time + '.txt'
    fp = open(saveName,'w')
    for vv in Result:
        fp.writelines(vv + "\n")
    fp.close()
    print("---- 下載完成 ")
    os.system("pause") 
    





Time = input("輸入起始日期(ex:2018-01) : ")
End = 1
while End:    
    
    Error = 0 
    if Time.find('-') != -1 and len(Time) == 7:
        AllTime = Time.split('-')
        yy = AllTime[0]
        mon = AllTime[1]
        if len(yy) != 4:
            Error = 1
        if len(mon) != 2 or int(mon) > 12 or int(mon) < 1:
            Error = 1 
    else:
        Error = 1 
        
        
    
    
    if Error == 0:
        if int(yy)%4 == 0:
            day = [31,28,31,30,31,30,31,31,30,31,30,31]
        else:
            day = [31,28,31,30,31,30,31,31,30,31,30,31]
        DownLoad_suv(Time,mon)
        End = 0
    else:
        print("---- 日期輸入有誤 ")
        Time = input("輸入起始日期(ex:2018-01) : ")













