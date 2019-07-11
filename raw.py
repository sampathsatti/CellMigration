import numpy as np
import matplotlib.pyplot as plt
import xml.etree.ElementTree
import math
import csv

e = xml.etree.ElementTree.parse('fMLP_Spin001_Tracks_2.xml').getroot()

track = int(0)
x_origin = float(0)
y_origin = float(0)
x = [0]
y = [0]
graphscale = int(1500)
initialPosX = [0,0]
initialPosY = [0,0]
finalPosX = [0]
finalPosY = [0]
dist = [0]
#flag = int(0)
left = int(0)
right = int(0)
top = int(0)
mid = int(0)
bottom = int(0)
COM_X = float(0)
COM_Y = float(0)

for detection in e.iter('detection'):

# NEW track seen
    if detection.get('t') == "0":
#housekeeping for previous track
        #get final position to be stored in another array
        finalPosX.append(x.pop())
        finalPosY.append(y.pop())

        dist.append(math.sqrt((finalPosX[-1]-initialPosX[-1])**2 + (finalPosY[-1]-initialPosY[-1])**2))
       #Plot particle track
        plt.plot(x, y, linewidth=1)
#Housekeeping for new track
       #Reset Arrays
        x[:] = []
        y[:] = []
       #Move on to next track
        track = track+1
       # First X and Y readout is the origin offset for each track
        x_origin = float(detection.get('x'))
        y_origin = float(detection.get('y'))
        initialPosX.append(x_origin)
        initialPosY.append(y_origin)
    else:
#if seeing an existing track
        x.append(float(detection.get('x')))
        y.append(float(detection.get('y')))


# Draw Axes
x = np.linspace(-graphscale, graphscale, graphscale, endpoint=True)
y= np.zeros(graphscale)
plt.figure(1)
plt.plot(x, y, 'k--')
plt.plot(y, x, 'k--')

# Draw Origin
# plt.plot(0, 0, 'ko')

# Specify Bounds
plt.axis([0, 2000, 0, 2000])

# Specify Axis Labels
plt.xlabel('Distance in microns')

# Voila
plt.show()

# Second Plot
plt.figure(2)
# Draw Axes
x = np.linspace(-graphscale, graphscale, graphscale, endpoint=True)
y= np.zeros(graphscale)
plt.plot(x, y, 'k--')
plt.plot(y, x, 'k--')

for i in range(1, track, 1):
    if finalPosX[i]!=0:
        print(np.arctan(finalPosY[i]/finalPosX[i]))
    if finalPosX[i]>0:
        right=right+1
    else:
        left=left+1
    COM_X = COM_X + finalPosX[i]
    COM_Y = COM_Y + finalPosY[i]

    X = [0, finalPosX[i]]
    Y = [0, finalPosY[i]]
    plt.plot(X,Y)

COM_X = COM_X/ track
COM_Y = COM_Y/ track

# Specify Bounds
plt.axis([0, 2000, 0, 2000])

# Specify Axis Labels
plt.xlabel('Distance in microns')

# Voila
plt.show()


print(len(initialPosX))
print(len(finalPosX))
print(len(initialPosY))
print(len(finalPosY))


print(initialPosX[1:5])
print(initialPosY[1:5])
print(finalPosX[1:5])
print(finalPosY[1:5])
print(dist[1:5])

#for i in range(1,len(finalPosX), 1):
#    plt.plot([initialPosX[i], initialPosY[i]], [initialPosX[i]+finalPosX[i], initialPosX[i]+finalPosY[i]])

for i in range (1, len(finalPosX), 1):
    plt.scatter(initialPosX, initialPosY, c='tab:blue', alpha=0.3, edgecolors='none')
    plt.scatter(finalPosX, finalPosY, c='tab:orange', alpha=0.3, edgecolors='none', s=[i * 0.5 for i in dist])
# Specify Bounds
plt.axis([400, 1500, 0, 1750])
# Specify Axis Labels
from matplotlib.patches import Patch
from matplotlib.lines import Line2D

legend_elements = [Line2D([0], [0], marker='o', color='w', label='Before',
                          markerfacecolor='tab:blue', markersize=10),
                   Line2D([0], [0], marker='o', color='w', label='After',
                          markerfacecolor='tab:orange', markersize=10),
                   ]

plt.legend(handles = legend_elements,
           loc='upper right', shadow=False)
plt.xlabel('Position along channel (um)', size=20)
plt.ylabel('Position across channel (um)', size=20)
plt.title('Scatter plot of cells before and after chemotaxis', size=24)
# Voila
plt.show()

with open("output.csv", "w", newline='') as f:
    writer = csv.writer(f)
    writer.writerow(initialPosX)

    writer.writerow(initialPosY)

    writer.writerow(finalPosX)
    writer.writerow(finalPosY)

for i in range (1, len(finalPosX), 1):
    plt.plot([0, finalPosX[i]-initialPosX[i]], [initialPosY[i], finalPosY[i]])

# Specify Bounds
plt.axis([-500, 400, 0, 1750])
# Specify Axis Labels
plt.xlabel('Position along channel (um)', size=20)
plt.ylabel('Position across channel (um)', size=20)
plt.title('Cell Tracks shifted along the channel', size=24)
# Voila
plt.show()
