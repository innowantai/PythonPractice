import requests 
from bs4 import BeautifulSoup
import pandas as pd
import numpy as np
import re



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
# =============================================================================
#         for vv in self.data2:
#             print(vv)
# =============================================================================
        return self.data2
    
    def getKK(self):
        self.dataKK = self.sp.find_all('div',{'class':'dd cardDesign dictionaryWordCard sys_dict_word_card'})
        self.dataKK2 = self.dataKK[0].find_all('span',{'class':'fz-14'})
        index = self.dataKK2[0].text  
        return index.replace('KK','')
     
        
    
    
search = 'data'
dd = DictionaryProcess(search)
KK = dd.getKK()
Exp = dd.getExplain() 


data = pd.DataFrame(index = range(30) ,columns = ["單字",'詞性',"解釋","例句"])
data.iloc[0,0] = search
data.iloc[1,0] = KK 
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





 
FileName = 'test.csv'
 

try:
    Data = pd.read_csv(FileName)
except:
    Data = pd.DataFrame(index = range(1) ,columns = ["單字",'詞性',"解釋","例句"])  


Data = Data.append(data,ignore_index = True)

Data = Data.dropna(axis = 0,how = 'all') 
Data = Data.fillna(value = '')


Data.to_csv(FileName,index=False, encoding='utf_8_sig')
























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

