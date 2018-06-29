import requests 
from bs4 import BeautifulSoup
import pandas as pd
import numpy as np
from openpyxl import load_workbook
import tkinter as tk
from  tkinter import ttk  #导入内部包  



class DictionaryProcess():    
    def __init__(self,search):
        self.url = 'https://tw.dictionary.search.yahoo.com/search;_ylt=AwrtXWlt9NNaUCYAfTt9rolQ;_ylc=X1MDMTM1MTIwMDM4MQRfcgMyBGZyAwRncHJpZAMEbl9yc2x0AzAEbl9zdWdnAzAEb3JpZ2luA3R3LmRpY3Rpb25hcnkuc2VhcmNoLnlhaG9vLmNvbQRwb3MDMARwcXN0cgMEcHFzdHJsAwRxc3RybAMxMQRxdWVyeQNyZWNvZ25pdGlvbgR0X3N0bXADMTUyMzg0MDIwNw--?p='+  search +  '&fr2=sb-top-tw.dictionary.search'
        self.res = requests.get(self.url)
        self.res.encoding = 'utf-8'
        self.sp = BeautifulSoup(self.res.text,'html.parser')
    
    def getExplain(self): 
        self.data = self.sp.find_all('div',{'class':'grp grp-tab-content-explanation tabsContent tab-content-explanation tabActived'})
        self.data2 = []
        flag = []
        if self.data != []:
            self.data2 = self.data[0].find_all('span',{'class':'fz-14'}) 
            flag = 1
        if self.data2 == [] and self.data != []:
            self.data = self.sp.find_all('div',{'class':'dd cardDesign dictionaryWordCard sys_dict_word_card'})
            self.data2 = self.data[0].find_all('div',{'class':' fz-16 fl-l dictionaryExplanation'})
            flag = 2
        return self.data2,flag
    
    def getKK(self):
        self.dataKK = self.sp.find_all('div',{'class':'dd cardDesign dictionaryWordCard sys_dict_word_card'})
        index = []
        if self.dataKK != []:
            self.dataKK2 = self.dataKK[0].find_all('span',{'class':'fz-14'})
            index = self.dataKK2[0].text  
            index = index.replace('KK','')
        return index
     
        
def combineData(search,Exp,flag):
    data = pd.DataFrame(index = range(30) ,columns = ["單字",'詞性',"解釋","例句"])
    data.iloc[0,0] = search 
    k0 = k1 = k2 = ii = 0
    for vv in Exp:
        test = vv.text
        if flag == 2:
            test = str(ii) + '. ' + test 
        if test[0].isupper() :
            if test.find('.') != -1 :
                test = test[:test.find('.')+1]
            elif test.find('?') != -1 :
                test = test[:test.find('?')+1]
            data.iloc[k2,3] = test
            k2 += 1   
            #k2 = np.max([k1,k2])
        elif test[0].isdigit():
            k1 = np.max([k1,k2])
            if test.find('[') != -1 : 
               test =  test[:test.find('[')]
            data.iloc[k1,2] = test
            k1 += 1  
        else:
            k0 = k1 = k2 = np.max([k1,k2])
            data.iloc[k0,1] = test   
        #print('k0=' + str(k0) + ', k1=' + str(k1) + ', k2=' + str(k2), ', k1cmpk2=' + str(np.max([k1,k2])))
    data = data.dropna(axis = 0,how = 'all') 
    data = data.fillna(value = '')  
    if k2 + k1 == 0 and Exp == []:
        data = []
    return data


def SaveResult(FileName,search,data):
    try:
        Data = pd.read_excel(FileName)
        index = Data.iloc[:,0].tolist()
    except:
        Data = pd.DataFrame(index = range(1) ,columns = ["單字",'詞性',"解釋","例句"])
        index = ['',''] 
    
    if search not in index:        
        Data = Data.append(data,ignore_index = True)  
        Data = Data.dropna(axis = 0,how = 'all') 
        Data = Data.fillna(value = '') 
        Data.to_excel(FileName,index=False, encoding='utf_8_sig')
    

def Show(data):   
    tree.delete(*tree.get_children())
    num = np.max(data.index.tolist())  + 1
    for i in range(num):
        tree.insert("",tk.END,text="" + str(i) ,values=(data.iloc[i,1],data.iloc[i,2],data.iloc[i,3])) 
    
    
    
def main():
    search = Input.get() 
    FileName = 'test.xlsx'
    dd = DictionaryProcess(search) 
    Exp,flag = dd.getExplain()  
    data = combineData(search,Exp,flag) 
        
    if type(data) != list:
       SaveResult(FileName,search,data) 
    elif data == [] :
       data = pd.DataFrame(index = range(1) ,columns = ["單字",'詞性',"解釋","例句"])
       data.iloc[0,1] = 'xxxxxxxxx'
       data.iloc[0,2] = '無相關解釋與例句'
       data.iloc[0,3] = 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'
       data = data.fillna(value = '') 
    Show(data) 
    return data
    
     





 

win = tk.Tk()
win.geometry('800x450')
win.title('英文單字查詢與彙整')




####### Variables ########
Input = tk.StringVar()
##########################
Input_Fra = tk.Frame(win)
Input_Fra.pack() 
lab = tk.Label(Input_Fra,text = '查詢單字 : ',font = ('微軟正黑體',12))
lab.grid(row = 0,column = 0, padx = 5)

txtInput = tk.Entry(Input_Fra, textvariable = Input ,font = ('times new roman',12))
txtInput.grid(row=0, column=1,pady = 5)

btnEnter = tk.Button(Input_Fra,text = '確認',height = 1, command = main, font = ('微軟正黑體',12))
btnEnter.grid(row=0, column=2, padx=10,pady = 5)



 
Show_Fra = tk.Frame(win)
Show_Fra.pack()
tree=ttk.Treeview(win, height = 18, selectmode = "extended")#表格   
tree["columns"]=("#0","#1","#2","#3")  
tree.column("#0",width=50)   #表示列,不显示  
tree.column("#1",width=100, anchor="s")   #表示列,不显示  
tree.column("#2",width=230, anchor="s")  
tree.column("#3",width=430, anchor="s")  
tree.column("#4",width=0)  
  
tree.heading("#0",text="Iter") #显示表头  
tree.heading("#1",text="詞性") #显示表头  
tree.heading("#2",text="解釋")  
tree.heading("#3",text="例句")  
  
tree.pack() 
win.mainloop()












# =============================================================================
# txtShow = tk.Text(Show_Fra,width = 80, font = ('微軟正黑體',15))
# txtShow.grid(row = 0,column = 0)
# =============================================================================














# =============================================================================
# book = load_workbook(FileName)
# writer = pd.ExcelWriter(FileName, engine='openpyxl') 
# writer.book = book
# writer.sheets = dict((ws.title, ws) for ws in book.worksheets)
# 
# data.to_excel(writer,'Sheet1',index=False, encoding='utf_8_sig')
# 
# writer.save()
# =============================================================================

 
 


























# =============================================================================
# search = 'parallel'
# 
# url = 'https://tw.dictionary.search.yahoo.com/search;_ylt=AwrtXWlt9NNaUCYAfTt9rolQ;_ylc=X1MDMTM1MTIwMDM4MQRfcgMyBGZyAwRncHJpZAMEbl9yc2x0AzAEbl9zdWdnAzAEb3JpZ2luA3R3LmRpY3Rpb25hcnkuc2VhcmNoLnlhaG9vLmNvbQRwb3MDMARwcXN0cgMEcHFzdHJsAwRxc3RybAMxMQRxdWVyeQNyZWNvZ25pdGlvbgR0X3N0bXADMTUyMzg0MDIwNw--?p='+  search +  '&fr2=sb-top-tw.dictionary.search'
# res = requests.get(url)
# res.encoding = 'utf-8'
# sp = BeautifulSoup(res.text,'html.parser')
#  
# =============================================================================

# =============================================================================
# data = sp.find_all('span',{'class':'fz-14'})
# data = sp.find_all('div',{'class':'dd cardDesign dictionaryWordCard sys_dict_word_card'})
# data2 = data[0].find_all('span',{'class':'fz-14'})
# for vv in data2:
#     print(vv)
# =============================================================================


#### This part is to find explain
# =============================================================================
# data = sp.find_all('span',{'class':'fz-14'})
# data = sp.find_all('div',{'class':'grp grp-tab-content-explanation tabsContent tab-content-explanation tabActived'})
# data2 = data[0].find_all('span',{'class':'fz-14'})
# for vv in data2:
#     print(vv)
# =============================================================================

