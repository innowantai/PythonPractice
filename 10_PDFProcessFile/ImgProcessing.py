import PIL
import os
import numpy as np 
import cv2



Folder1 = 'A1_0'
Folder2 = 'A1_1'


path1 = os.path.join(os.getcwd(),Folder1)
path2 = os.path.join(os.getcwd(),Folder2)
files1 = os.listdir(path1)
files2 = os.listdir(path2)

for i in range(len(files1)): 
    ff = files1[i]
    ff2 = files2[i]
    PATH1 = os.path.join(path1,ff)
    PATH2 = os.path.join(path2,ff2)
    
    img = PIL.Image.open(PATH1).convert('RGB')
    open_cv_img = np.array(img) 
    IMG1 = cv2.cvtColor(open_cv_img,cv2.COLOR_BGR2GRAY)
    
    img = PIL.Image.open(PATH2).convert('RGB')
    open_cv_img = np.array(img) 
    IMG2 = cv2.cvtColor(open_cv_img,cv2.COLOR_BGR2GRAY)
    
    index = IMG1 - IMG2
    test = np.max(np.abs(IMG1 - IMG2))
    if test != 0:            
        index[index == 0] = 1
        index[index == 255] = 0 
        index[index == 1] = 255 
        test1 = PIL.Image.fromarray(index)
        test1.save(os.path.join(os.getcwd(),'DiffPage_' + str(i+1) + '.jpg'))
        
    print('Page' ,i + 1,'Compared Result = ',test)


