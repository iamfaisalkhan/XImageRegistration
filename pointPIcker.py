
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from matplotlib.image import AxesImage
import numpy as np
from numpy.random import rand
import sys

def onpick1(event):
    print (event.xdata)
    # if isinstance(event.artist, AxesImage):
    #     axImage = event.artist

    #     print (axImage.xdata)
        # xdata = thisline.get_xdata()
        # ydata = thisline.get_ydata()
        # ind = event.ind
        
        # print ('X='+str(np.take(xdata, ind)[0])) # Print X point
        # print ('Y='+str(np.take(ydata, ind)[0])) # Print Y point


fig, ax = plt.subplots()
ax.set_title('click on points', picker=True)
ax.set_ylabel('ylabel', picker=True, bbox=dict(facecolor='red'))

img = mpimg.imread(sys.argv[1])
ax.imshow(img, cmap='gray', picker=True)
#line, = ax.plot(rand(100), 'o', picker=5)
fig.canvas.mpl_connect('button_press_event', onpick1)
plt.show()