







from time import time
import threading  
def factorize(number):
    rr = []
    for i in range(1, number):
        if number % i == 0:
            rr.append(i)
    if sum(rr) == number:
        print(number)
            





Re = []
task = []

for i in range(6,100000):
    task.append ( threading.Thread(target=factorize(i)))
    
k = 0
for st in task:
    print(k)
    st.start()
    k += 1
    
    
    