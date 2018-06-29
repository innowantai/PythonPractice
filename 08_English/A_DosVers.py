import requests 
from bs4 import BeautifulSoup
import pandas as pd
import numpy as np
from openpyxl import load_workbook
import tkinter as tk



class DictionaryProcess():    
    def __init__(self,search):
        self.url = 'https://tw.dictionary.search.yahoo.com/search;_ylt=AwrtXWlt9NNaUCYAfTt9rolQ;_ylc=X1MDMTM1MTIwMDM4MQRfcgMyBGZyAwRncHJpZAMEbl9yc2x0AzAEbl9zdWdnAzAEb3JpZ2luA3R3LmRpY3Rpb25hcnkuc2VhcmNoLnlhaG9vLmNvbQRwb3MDMARwcXN0cgMEcHFzdHJsAwRxc3RybAMxMQRxdWVyeQNyZWNvZ25pdGlvbgR0X3N0bXADMTUyMzg0MDIwNw--?p='+  search +  '&fr2=sb-top-tw.dictionary.search'
        self.res = requests.get(self.url)
        self.res.encoding = 'utf-8'
        self.sp = BeautifulSoup(self.res.text,'html.parser')
    
    def getExplain(self): 
        self.data = self.sp.find_all('div',{'class':'grp grp-tab-content-explanation tabsContent tab-content-explanation tabActived'})
        self.data2 = []
        if self.data != []:
            self.data2 = self.data[0].find_all('span',{'class':'fz-14'}) 
        return self.data2
    
    def getKK(self):
        self.dataKK = self.sp.find_all('div',{'class':'dd cardDesign dictionaryWordCard sys_dict_word_card'})
        index = []
        if self.dataKK != []:
            self.dataKK2 = self.dataKK[0].find_all('span',{'class':'fz-14'})
            index = self.dataKK2[0].text  
            index = index.replace('KK','')
        return index
     
        
def combineData(search,Exp):
    data = pd.DataFrame(index = range(30) ,columns = ["單字",'詞性',"解釋","例句"])
    data.iloc[0,0] = search
    #data.iloc[1,0] = KK 
    k0 = k1 = k2 = 0
    for vv in Exp:
        test = vv.text
        if test[0].isupper() :
            if test.find('.') != -1 :
                test = test[:test.find('.')+1]
            elif test.find('?') != -1 :
                test = test[:test.find('?')+1]
            data.iloc[k2,3] = test
            k2 += 1   
        elif test[0].isdigit():
            if test.find('[') != -1 : 
               test =  test[:test.find('[')]
            data.iloc[k1,2] = test
            k1 += 1  
        else:
            k0 = k1 = k2 = np.max([k1,k2])
            data.iloc[k0,1] = test   
    data = data.dropna(axis = 0,how = 'all') 
    data = data.fillna(value = '')
    if k2 == 0:
        data = []
    return data


def SaveResult(FileName):
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
    
    
    
    
    
FileName = 'test.xlsx'

 

while 1:

    search = input('輸入要查詢的單字 : ')
    print('查詢結果 : ')
    dd = DictionaryProcess(search)
    KK = dd.getKK()
    Exp = dd.getExplain() 
    data = combineData(search,Exp)
    if type(data) != list:
       SaveResult(FileName)
       
    print(' ')
    print(' ')
    print(data)







# =============================================================================
# win = tk.Tk()
# win.geometry('400x400')
# 
# txtInput = tk.Text()
# txtInput.pack()
# 
# 
# win.mainloop()
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

