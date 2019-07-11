import numpy as np
import matplotlib.pyplot as plt
import xml.etree.ElementTree
e = xml.etree.ElementTree.parse('Neutrophils_fMLP_Tracks_12.xml').getroot()

track = int(0)
x_origin = float(0)
y_origin = float(0)
x = [0]
y = [0]
graphscale = int(300)
initialPosX = [0,0]
initialPosY = [0,0]
finalPosX = [0]
finalPosY = [0]
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
        #get final position to be stored in another array
        finalPosX.append(x.pop())
        finalPosY.append(y.pop())
       #Plot particle track
        plt.plot(x, y, linewidth=1)
       #Reset Arrays
        x[:] = []
        y[:] = []
        x.append(0)
        y.append(0)
       #Move on to next track
        track = track+1
       # First X and Y readout is the origin offset for each track
        x_origin = float(detection.get('x'))
        y_origin = float(detection.get('y'))
        initialPosX.append(x_origin)
        initialPosY.append(y_origin)
    else:
        #if seeing
        x.append(float(detection.get('x')) - x_origin)
        y.append(float(detection.get('y')) - y_origin)


# Draw Axes
x = np.linspace(-graphscale, graphscale, graphscale, endpoint=True)
y= np.zeros(graphscale)
plt.figure(1)
plt.plot(x, y, 'k--')
plt.plot(y, x, 'k--')

# Draw Origin
# plt.plot(0, 0, 'ko')

# Specify Bounds
plt.axis([-graphscale, graphscale, -graphscale, graphscale])

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
plt.axis([-graphscale, graphscale, -graphscale, graphscale])

# Specify Axis Labels
plt.xlabel('Distance in microns')

# Voila
plt.show()

print(left)
print(right)
print(COM_X)
print(COM_Y)

print(len(initialPosX))
print(len(finalPosX))
print(len(initialPosY))
print(len(finalPosY))

for i in range(1,len(finalPosX), 1):
    finalPosX[i]= finalPosX[i]+initialPosX[i]
    finalPosY[i]= finalPosY[i]+initialPosY[i]

#for i in range(1,len(finalPosX), 1):
#    plt.plot([initialPosX[i], initialPosY[i]], [initialPosX[i]+finalPosX[i], initialPosX[i]+finalPosY[i]])

for i in range (1, len(finalPosX), 1):
    plt.scatter(initialPosX, initialPosY, c='tab:blue')
    plt.scatter(finalPosX, finalPosY, c='tab:orange')
# Specify Bounds
plt.axis([0, 2000, 0, 2000])
# Specify Axis Labels
plt.xlabel('Distance in pixels')
# Voila
plt.show()
