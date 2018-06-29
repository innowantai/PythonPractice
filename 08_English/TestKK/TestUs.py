import requests
from bs4 import BeautifulSoup
import numpy as np
import pandas as pd



search = 'congratulations'
url = 'https://tw.dictionary.search.yahoo.com/search?p='
URL = url + search

res = requests.get(URL)
res.encoding = 'utf-8'
sp = BeautifulSoup(res.text,'html.parser')


dataKK = sp.find_all('div',{'class':'dd cardDesign dictionaryWordCard sys_dict_word_card'})[0]

data2 = dataKK.find_all('span',{'class':'fz-14'})

result = []
result.append( data2[0].getText())

dic = {'KK':result}

rr = pd.DataFrame(dic)

rr.to_excel('TestUs.xlsx')