import numpy as np
import matplotlib.pyplot as plt
import xml.etree.ElementTree
import math
import csv

e = xml.etree.ElementTree.parse('fMLP_Spin001_Tracks_2.xml').getroot()

track = int(0)
x_origin = float(0)
y_origin = float(0)
x = np.zeros(2)
y = np.zeros(2)
i = int(0)
graphscale = int(1500)

for track in e.iter('particle'):
    Length = int(track.get("nSpots"))
    index = 1
    i = i+1
    for child in track:
        new_xRow = [i, float(child.get("x"))]
        x = np.vstack([x, new_xRow])
        new_yRow = [i, float(child.get("y"))]
        y = np.vstack([y, new_yRow])
        #y.append(float(child.get("y")))
    if(x[i,0]>850):
        for i in range(1, Length, 1):
            print(x[1,index])
        #plt.plot(x[i, :], y[i, :], linewidth=1)

print(np.random.randint(10, size=(1, 2)))
plt.axis('square')
plt.show()



