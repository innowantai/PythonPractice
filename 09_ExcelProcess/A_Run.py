import pandas as pd
import numpy as np
import xlrd
import xlwt
import re
import os

def Loading(FileName):
    data=xlrd.open_workbook(FileName) 
    sheets = data.sheet_names() 
    return sheets

def ResultProcess(Index_work,Index_hour):
    AllName = []
    
    for ii in Index_work.keys():
        if ii not in AllName:
            AllName.append(ii)
    AllName = sorted(AllName)
    result = ''
    for ii in AllName:
        ww = Index_work.get(ii)
        hh = Index_hour.get(ii)
        if ww == 0:
            ww = ''
        if hh == 0: 
            if ww != '':
                result += ii + "{:.0f}".format(ww)  
            else:
                result = ''
            
        else:
            result += ii + "{:.0f}".format(ww) + '+' + str(hh) + 'h'
         
    return result

def WorkAndHourProcess(txt,oriData,AllWork,AllHour):
    r1 = r'\(';r2 = r'\)'
    pp1 = [c.end() for c in re.finditer(r1,txt)]
    pp2 = [c.start() for c in re.finditer(r2,txt)]
    
    result = '';    result_ori = '' 
    T_work = 0 ;    T_hour = 0 
    Index_work = dict();    Index_hour = dict()
   # print(txt)
    for i, p1 in enumerate(pp1):
        cmpName = ''
        data1 = txt[pp1[i]:pp2[i]]   
        r3 = r'\D*' ;    r4 = r'\d*[\+].*'; r5 = b'[\W]*' ;  
        for ii in re.findall(r5,data1.encode('utf-8')):
            if ii.decode() != '' and ii.decode() != '+' and ii.decode() != '-' : 
                cmpName = ii.decode()   
        
        cmpName = cmpName.replace('+','') 
        
        #cmpName = re.findall(r3,data1)[0] 
        #cmpName = cmpName.replace('+','')
        ### Process Detail
        if cmpName != '' :
            if data1.find('+') != -1:
                Detail = re.findall(r4,data1)[0]
                work = Detail[:Detail.find('+')]
                hour = Detail[Detail.find('+')+1:-1]
                if work == '':
                    work = 0 
            else: 
                Detail = data1[len(cmpName):] 
                work = Detail
                if work == '':
                    work = 0 
                hour = 0           
            
            T_work += int(work)
            T_hour += float(hour)
            AllWork = AllWorkAndHourProcess(AllWork,work,cmpName)
            AllHour = AllWorkAndHourProcess(AllHour,hour,cmpName)
            Index_work = AllWorkAndHourProcess(Index_work,work,cmpName)
            Index_hour = AllWorkAndHourProcess(Index_hour,hour,cmpName) 
         
        #print(Index_work,work)
        
    diffWork = oriData[0] - T_work
    diffHour = oriData[1] - T_hour 
    cmpName = '利晉'
    if diffHour == 0:
        result_ori = '利晉' + str(diffWork)
    else:
        result_ori = '利晉' + str(diffWork) + '+' + str(diffHour) + 'h'
    if diffWork+diffHour <=0:
        result_ori = '' 
    
    result = result_ori + ResultProcess(Index_work,Index_hour)
    AllWork = AllWorkAndHourProcess(AllWork,diffWork,cmpName)
    AllHour = AllWorkAndHourProcess(AllHour,diffHour,cmpName)
    return AllWork,AllHour,result
    

def AllWorkAndHourProcess(AllData,addData,cmpName):
    if AllData.get(cmpName) == None:
        AllData[cmpName] = float(addData)
    else:
        AllData[cmpName] += float(addData)
    return AllData
    

def SaveToExcel(data,sheets,savePath,FileName):
    Ndata=xlwt.Workbook()
    table=Ndata.add_sheet(sheets)
    data = data.fillna(value = '')
    for i in range(data.shape[0]):
        for j in range(data.shape[1]):
            table.write(i,j,data.iloc[i,j])
    Ndata.save(savePath + '\\Result_' + FileName)
 
    
def Split(txt):
    rr = r'\d\.'
    po1 = []
    [po1.append(vv.start()) for vv in re.finditer(rr,txt)]
    po1.append(len(txt))
    Catch = []
    try:
        for ii in enumerate(po1): 
            Catch.append(txt[po1[ii[0]]:po1[ii[0]+1]])
    except:
        pass
    
    OutPut = []
    for vv in Catch:
        if vv.find('(') != -1 :
            vv = vv[vv.find('.')+1:]
            OutPut.append(vv)  
    return OutPut

def ProcessCase2(ts,A_Date,B_Content,txt):
    Time = str(ts.year-1911) + '.' + str(ts.month) + '.' + str(ts.day)
    cont = Split(txt)
    for vv in cont:
        A_Date.append(Time)
        B_Content.append(vv)
    return A_Date,B_Content

def SaveToExcel_Case2(data,savePath):
    savePath = savePath + '\\Result_WordText.xlsx'
    data.to_excel(savePath)
    
    


Files = os.listdir()
FileName = []
for vv in Files:
    if vv.find('.xls') != -1:
        FileName = vv

 
sheets = Loading(FileName)
num = len(sheets) 
data = pd.read_excel(FileName,num-1)
path = os.getcwd()
FolderName = '0_Result'
savePath = path + '\\' + FolderName
if not os.path.exists(savePath):
    os.mkdir(savePath)
    
    

AllWork = dict() 
AllHour = dict()
############################   Processing Table 1   ##################################
po1 = [c[0] for c in np.where(data == '日期')]
po2 = [c[0] for c in np.where(data == '工   作    內    容')]
po3 = [c[0] for c in np.where(data == '總計')]
tab1 = data.iloc[po1[0]:po3[0]+1,po1[1]:po2[1]+1]
index = []
B_Content = []
A_Date = []
rr1 = r'(\d\..*?\))'
for i in range(2,tab1.shape[0]-1):        
    txt = tab1.iloc[i,10]
    oriData = tab1.iloc[i,1:3] 
    ts = tab1.iloc[i,0]           
    
    try:        
        A_Date, B_Content = ProcessCase2(ts,A_Date,B_Content,txt) 
        AllWork,AllHour,result = WorkAndHourProcess(txt,oriData,AllWork,AllHour)
        index.append(result)
    except:
        pass
##################################################################################### 

po4 = [po2[0]+2,po2[1]-1]
po5 = [po3[0]+3 , 0]
po6 = [c[0] for c in np.where(data == '請購的加款金額')]
po6[0] += 2


for i,v in enumerate(index):
    data.iloc[po4[0]+i,po4[1]] = v

try:    
    i = 0
    v = '利晉'
    data.iloc[po5[0]+i,po5[1]] = v
    data.iloc[po5[0]+i,po5[1]+1] = AllWork[v]
    data.iloc[po5[0]+i,po5[1]+2] = AllHour[v]
except:
    i = 0
    
for v in AllWork:
    if v != '利晉':
        i += 1
        data.iloc[po5[0]+i,po5[1]] = v
        data.iloc[po5[0]+i,po5[1]+1] = AllWork[v]
        data.iloc[po5[0]+i,po5[1]+2] = AllHour[v]    

for i , v in enumerate(AllWork): 
    data.iloc[po6[0]+i,po6[1]] = v
    data.iloc[po6[0]+i,po6[1]+1] = AllWork[v]
    data.iloc[po6[0]+i,po6[1]+2] = AllHour[v]
    
Result2 = pd.DataFrame({'A_日期':A_Date,'B_扣款說明':B_Content})

sheets = sheets[num-1]
SaveToExcel(data,sheets,savePath,FileName)
SaveToExcel_Case2(Result2,savePath)

print('---------------------------------------')
print('---------------------------------------')
print(' 檔名  : ' + FileName )
print('工作表 : ' + sheets )
print(' 結果  : 處理完畢')
print('---------------------------------------')
print('---------------------------------------')

os.system('pause')







