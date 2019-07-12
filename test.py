import numpy as np
import matplotlib.pyplot as plt
import xml.etree.ElementTree
import math
import csv
import brewer2mpl

e = xml.etree.ElementTree.parse('Neutrophils_fMLP_Tracks_12.xml').getroot()

bmap = brewer2mpl.get_map('Set2', 'qualitative', 8)
colors = bmap.mpl_colors

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




print(np.random.randint(10, size=(1, 2)))
plt.axis('square')
plt.show()


plt.figure(2)




#figure showing first and last points only

for i in range (1, len(finalPosX), 1):
    #if (initialPosX[i] > 850):
    plt.plot([0, finalPosY[i]-initialPosY[i]], [0,  -finalPosX[i]+initialPosX[i]], color=colors[7])
    plt.plot([finalPosY[i]-initialPosY[i]], [-finalPosX[i]+initialPosX[i]], 'o', alpha = 0.8, color=colors[1], label='point')
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

plt.gca().spines['right'].set_visible(False)
plt.gca().spines['top'].set_visible(False)
plt.gca().spines['left'].set_position('zero')
plt.gca().spines['bottom'].set_position('zero')
plt.axis([-350, 350, -250, 1000])
plt.xticks([-300, -150, 0, 150, 300])
plt.gca().set_aspect('equal')
plt.show()

print(len(initialPosX))
print(len(finalPosX))

plt.figure(3)

#flip data around to ensure continuity with figure 5


for i in range(0, len(finalPosX)-1, 1):
    finalPosX[i] = 2000-finalPosX[i]

for i in range(0, len(initialPosX)-1, 1):
    initialPosX[i] = 2000-initialPosX[i]

for i in range(0, len(finalPosX)-1, 1):
    after.append(finalPosX[i])

before = []
for i in range(0, len(finalPosX)-1, 1):
    before.append(initialPosX[i])


num_bins = 40


n, bins, patches = plt.hist(after, num_bins, histtype=u'step', cumulative=True, density=1, facecolor='tab:blue', alpha=0.7)
n, bins, patches = plt.hist(before, num_bins,  histtype=u'step', cumulative=True, density=1, facecolor='tab:orange', alpha=0.7)
plt.ticklabel_format(axis='y', style='sci', scilimits=(0, 0))
plt.xlabel('Position along axis', size=12)
plt.ylabel('Cumulative distribution function', size=12)


plt.show()

plt.figure(4)

for i in range(1, len(finalPosY), 1):
    plt.scatter(finalPosX[i], finalPosY[i], c='tab:blue', s=50, alpha=0.7, edgecolors='none')
for i in range(1, len(initialPosX), 1):
    plt.scatter(initialPosX[i], initialPosY[i], c='tab:orange', s=50, alpha=0.7, edgecolors='none')

plt.show()
