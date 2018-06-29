import os
import cv2
import matplotlib.pyplot as plt
import numpy as np
import PIL



cap  = cv2.VideoCapture('00314.mp4')

folder = os.path.join(os.getcwd(),'0_Folder')
if not os.path.exists(folder):
    os.mkdir(folder)
    
ii = 0
x = []
y = []
while cap.isOpened():
    print(ii)
    _, frame  = cap .read() 
    frame = frame[350:700,700:1200]
    blur = cv2.blur(frame, (4, 4))
    diff = cv2.absdiff(1080*1920, blur)
    test = diff[:,:,2] 
    ret, thresh = cv2.threshold(test, 100, 255, cv2.THRESH_BINARY)
    cv2.imwrite(os.path.join(folder,'Fig_' + str(ii) + '.png'),thresh)   
    po = np.where(thresh == 255)
    y.append(np.mean(po[0]))
    x.append(np.mean(po[1])) 
    ii += 1
 

cv2.imshow('thresh',thresh)
