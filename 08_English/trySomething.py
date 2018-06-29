
import requests
from bs4 import BeautifulSoup
import os


url = 'https://tw.dictionary.search.yahoo.com/search?p=save'
res = requests.get(url)
res.encoding = 'utf-8'
sp = BeautifulSoup(res.text,'html.parser')


# =============================================================================
# data = sp.find_all('div',{'class':'dd cardDesign dictionaryWordCard sys_dict_word_card'})
# data2 = data[0].find_all('div',{'class':' fz-16 fl-l dictionaryExplanation'})
# =============================================================================


data = sp.find_all('div',{'class':'grp grp-tab-content-explanation tabsContent tab-content-explanation tabActived'})
data2 = data[0].find_all('span',{'class':'fz-14'}) 
for vv in data2:
    print(vv)
    
os.system('pause')
 