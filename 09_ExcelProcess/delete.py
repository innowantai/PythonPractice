
import re

test = '4.周哲瑋('
t1 = test.encode()

t2 = t1.decode()

r1 = b'[\W]*';   
c1 = re.findall(r1,test.encode('utf-8'))

for vv in c1:
    if vv.decode() != '':
        test = vv.decode()

print(c1)
