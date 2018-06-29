import matplotlib.pyplot as plt
import numpy as np

plt.style.use('ggplot')

N = 2000
x = np.random.randn(N)
y = x + np.random.randn(N)*0.5



margin_border = 0.1
width = 0.6
height = 0.2
margin_between = 0.02



left_s = margin_border
bottom_s = margin_border
height_s = width
width_s = width

left_x = margin_border 
bottom_x = margin_border + margin_between + width
height_x = height
width_x = width

left_y = margin_border + margin_between + width
bottom_y = margin_border 
height_y = width
width_y = height



plt.figure(1,figsize = (8,8))
rect_s = [left_s, bottom_s, width_s, height_s]
rect_x = [left_x, bottom_x, width_x, height_x]
rect_y = [left_y, bottom_y, width_y, height_y]

axScatter = plt.axes(rect_s)
axX = plt.axes(rect_x)
axY = plt.axes(rect_y)
axX.set_xticklabels([])
axY.set_yticklabels([])


axScatter.scatter(x,y)


bin_width = 0.25
xymax = np.max([np.max(np.fabs(x)),np.max(np.fabs(y))])





