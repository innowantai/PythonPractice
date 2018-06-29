import PIL
import numpy as np
import cv2
import matplotlib.pyplot as plt
import dpkt
import struct
import sys
import base64
from PIL import Image
import pandas as pd



 
    
case = 25
Name = 'Channel_' + '%03d' % case +'.raw'
     
# =============================================================================
# rawfile  = np.fromfile(Name)
# rawfile = rawfile[-180000:]
# x = np.arange(len(rawfile))  
# with open('Res.txt','w') as f:
#     for ff in rawfile:
#         f.writelines(str(ff) + '\n')
# =============================================================================





file = open(Name, "rb")
rawdata = file.read() 
im = Image.frombytes("F", (512,512), rawdata, "raw", "F;32F")


 





