import os
from firebase import firebase
import sqlite3 as lite
import numpy as np





# =============================================================================
# con = lite.connect('Test.sqlite')
# cursor = con.execute('select name from Docs')
# data = cursor.fetchall()
# con.close()
# =============================================================================





#140.110.17.180,ncree_guest,ncree_guest,21

url = 'https://savetrying.firebaseio.com/'
fb = firebase.FirebaseApplication(url,None)
Data = fb.get('/FTP',None)



      
#fb.put(url , name = 'FigName' + str(ii), data = Names)

#fb.post(url,Names)





# =============================================================================
# Names = {'IP' : '140.110.17.180','Account':'ncree_guest','PassWord':'ncree_guest','Port':'21'}
# fb.put(url , name = 'FTP', data = Names)
# =============================================================================


#fb.delete(url,None)

































