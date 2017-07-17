
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from matplotlib.image import AxesImage

from skimage.transform import rescale

import numpy as np

import sys

X = []
Y = []

def onpick1(event):
    if (event.button == 1):
        X.append(event.xdata)
        Y.append(event.ydata)
    elif (event.button == 3):
        xstr = "["
        ystr = "["
        for pt in X:
            xstr = "%s,%d"%(xstr, pt)
        xstr = "%s]"%(xstr)

        for pt in Y:
            ystr = "%s,%d"%(ystr, pt)
        ystr="%s]"%ystr
        
        print (xstr)
        print (ystr)
        sys.exit(0)

    
fig, ax = plt.subplots()
ax.set_title('click on points', picker=True)
ax.set_ylabel('ylabel', picker=True, bbox=dict(facecolor='red'))

img = mpimg.imread(sys.argv[1])
img = rescale(img, 0.4, mode='reflect')

ax.imshow(img, cmap='gray', picker=True)
#line, = ax.plot(rand(100), 'o', picker=5)
fig.canvas.mpl_connect('button_press_event', onpick1)
plt.show()