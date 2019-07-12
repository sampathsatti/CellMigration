import numpy as np
import matplotlib.pyplot as plt
import xml.etree.ElementTree
import math
import csv

e = xml.etree.ElementTree.parse('Neutrophils_fMLP_Tracks_12.xml').getroot()

# Made a test change to see if its syncing

track = int(0)
x_origin = float(0)
y_origin = float(0)
x = [0]
y = [0]
initialPosX = []
initialPosY = []
finalPosX = []
finalPosY = []
xDisp = []
after = []
directness = []
forward = int(0)
reverse = int(0)
i = int(0)
graphscale = int(1500)


def distancecomp(in1, in2):
    count = int(0)
    for j in range(0, len(in1)-1, 1):
        #print(j)
        count = count + math.hypot(in1[j+1]-in1[j], in2[j+1]-in2[j])
        #print(count)
    return count
# figure showing raw paths

for track in e.iter('particle'):
    Length = int(track.get("nSpots"))
    x = []
    y = []
    for child in track:
        x.append(float(child.get("x")))
        y.append(float(child.get("y")))

    #if(x[0]>850):

    plt.plot(x, y, linewidth=1)
    distance = distancecomp(x,y)
    displacement = math.hypot((x[len(x)-1]-x[0]), (y[len(y)-1]-y[0]))
    directness.append(distance/displacement)

    initialPosX.append(x[0])
    finalPosX.append(x.pop())
    initialPosY.append(y[0])
    finalPosY.append(y.pop())

print(np.mean(directness))
print(np.random.randint(10, size=(1, 2)))
plt.axis('square')
plt.show()

# Figure showing raw paths from origin

for track in e.iter('particle'):
    Length = int(track.get("nSpots"))
    x = []
    y = []
    for child in track:
        if len(x)==0:
            x_origin = float(child.get("x"))
            y_origin = float(child.get("y"))
        x.append(float(child.get("x"))-x_origin)
        y.append(float(child.get("y"))-y_origin)
    # if(x[0]>850):

    plt.plot(x, y, linewidth=1)



    initialPosX.append(x[0])
    finalPosX.append(x.pop())
    initialPosY.append(y[0])
    finalPosY.append(y.pop())

print(np.random.randint(10, size=(1, 2)))
plt.axis('square')
plt.show()


plt.figure(2)

plt.plot([-600, 300], [0, 0], 'k--')
plt.plot([0, 0], [-500, 500], 'k--')


#figure showing first and last points only

for i in range (1, len(finalPosX), 1):
    #if (initialPosX[i] > 850):
    plt.plot([0, finalPosX[i]-initialPosX[i]], [0, finalPosY[i]-initialPosY[i]])
    #print(finalPosX[i])
    if finalPosX[i]-initialPosX[i] < 0:
        forward = forward+1
    else:
        reverse = reverse+1
print("Number of cells: ", len(finalPosX))
print("Forward: ", forward)
print("Reverse: ", reverse)
#plt.ticklabel_format(axis='y', style='sci', scilimits=(0,0))
#plt.xlabel('Position along channel (um)', size=12)
#plt.ylabel('Position across channel', size=12)
#plt.title(r'Cell Migration', size=16)
plt.axis([-600, 300, -500, 500], 'square')
plt.show()

print(len(initialPosX))
print(len(finalPosX))

plt.figure(3)

for i in range(0, len(finalPosX)-1, 1):
    after.append(finalPosX[i])

before = []
for i in range(0, len(finalPosX)-1, 1):
    before.append(initialPosX[i])


num_bins = 40
# the histogram of the data
n, bins, patches = plt.hist(after, num_bins, histtype=u'step',  density=1, facecolor='tab:blue', alpha=0.5)
n, bins, patches = plt.hist(before, num_bins,  histtype=u'step',  density=1, facecolor='tab:orange', alpha=0.5)
plt.ticklabel_format(axis='y', style='sci', scilimits=(0, 0))
plt.xlabel('Position along axis', size=12)
plt.ylabel('Cumulative distribution function', size=12)
plt.title(r'Cell Distribution w/o alignment', size=16)

plt.show()


n, bins, patches = plt.hist(after, num_bins, histtype=u'step', cumulative=True, density=1, facecolor='tab:blue', alpha=0.5)
n, bins, patches = plt.hist(before, num_bins,  histtype=u'step', cumulative=True, density=1, facecolor='tab:orange', alpha=0.5)
plt.ticklabel_format(axis='y', style='sci', scilimits=(0, 0))
plt.xlabel('Position along axis', size=12)
plt.ylabel('Cumulative distribution function', size=12)
plt.title(r'Cell Distribution w/o alignment', size=16)

plt.show()
