import matplotlib.pyplot as plt
import numpy as np
import datetime
import matplotlib as mpl


plt.style.use('classic')

fig, axes = plt.subplots(2,2)
ax1,ax2,ax3,ax4 = axes.ravel()

x , y = np.random.normal(size = (2,100))
ax1.plot(x,y,'o')

x = np.arange(0,10)
y = np.arange(0,10)
ncolors = len(plt.rcParams['axes.color_cycle'])

shift = np.linspace(0,10,ncolors)
for s in range(ncolors):
     ax2.plot(x,y+s,'-')

x = np.arange(5)
y1, y2, y3 = np.random.randint(1,25,size = (3,5 ))     
width = 0.25

ax3.bar(x,y1,width )
ax3.bar(x+width,y2,width )
ax3.bar(x+width*2,y3,width )


for i, color in enumerate(plt.rcParams['axes.color_cycle']):
     xy = np.random.normal(size = 2)
     ax4.add_patch(plt.Circle(xy,radius=0.3,color = color))
ax4.axis('equal')


print(plt.style.available)













