
import re

test = '1.工區、工務所環境整理2.工區周圍環境整理3.圍籬綠美化養護4.工區休息區宮廷帳搭設(哲在1)5.工區LINE線標示6.配合練續壁灌漿洗車(國產1+4h)7.庫房整'



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

t1 = test.encode()

t2 = t1.decode()

r1 = b'(\d\..*)\d\.';   
r2 = b'(\d\..*?\))'

sp = Split(test)

c1 = re.findall(r1,test.encode('utf-8'))

res = []
for vv in c1:
    if vv.decode() != '':
        test = vv.decode()
        res.append(test)

print(res)



 



## \((.*?)\)