import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Polygon 







def func(x):
     return -(x-2)*(x-8)+40


x = np.linspace(0,10)
y = func(x)


fig, ax = plt.subplots()

ax.plot(x,y,'r',linewidth = 1)

a = 2 
b = 9
ax.set_xticks([a,b])
ax.set_yticks([ ])
ax.set_xticklabels([r'$a$',r'$b$'],size = 17)

plt.figtext(0.89,0.08,'$x$',size = 17)
plt.figtext(0.11,0.9,'$y$',size = 17)



ix = np.linspace(a,b) 
iy = func(ix)
ixy = zip(ix.tolist(),iy.tolist())
vert = [(a,0)]
for ii in ixy:
     vert.append(ii)
     
vert.append((b,0)) 
poly = Polygon(vert,facecolor = '0.8', edgecolor = '0.4')
ax.add_patch(poly)

ax.text((a+b)*0.5,30 ,r'$ \int_a^b(-(x-2)*(x-8)+40)dx$',size = 17,horizontalalignment = 'center')

