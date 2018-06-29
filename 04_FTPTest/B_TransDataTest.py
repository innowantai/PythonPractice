




import os

fileName = '20170315.pptx'
#fileName = 'oldfriend.png'

fp = open(fileName,'rb')
line = fp.read()
result = []
while line: 
    result.append(line)
    line = fp.readline()
    print(line)
fp.close()
print("The Files Read completed")

path = os.getcwd()
folderName = '\\TestUs'
try:
    os.mkdir(folderName)
except:
    pass
    
    
    
 
os.chdir(path + folderName)


fpp = open(fileName,'wb') 
vv = result[0]
st = 0
index = []
for ii in range(0,len(vv)+1):
    test = vv[st : ii+1]
    fpp.write(test)  
    index += test
    st = st + 1
    
    
fpp.close()    
    
    
    
    
    
    
    
    
    
    