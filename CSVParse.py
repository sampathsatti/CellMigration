import numpy as np

import scipy.stats
import matplotlib.pyplot as plt
import random
from matplotlib.lines import Line2D
import seaborn as sns
import pandas as pd

before = np.genfromtxt('Device1_Sanitized.csv', delimiter=',')
after = np.genfromtxt('Device4_Sanitized.csv', delimiter=',')
device2 = np.genfromtxt('Device2_Sanitized.csv', delimiter=',')
device9 = np.genfromtxt('Device9_Sanitized.csv', delimiter=',')
device12 = np.genfromtxt('Device12_Sanitized.csv', delimiter=',')

before_x = before[:, 1]
before_x = before_x[1:]
before_y = before[:, 2]
before_y = before_y[1:]

after_x = after[:, 1]
after_x = after_x[1:]
after_y = after[:, 2]
after_y = after_y[1:]

#initialize CSV data to origin/backstop

device2_x = device2[:, 1]
device2_x = device2_x[1:]

for i in range(0, len(device2_x)-1, 1):
    device2_x[i] = 1011-device2_x[i]


device9_x = device9[:, 1]
device9_x = device9_x[1:]

for i in range(0, len(device9_x)-1, 1):
    device9_x[i] = 1004-device9_x[i]


device12_x = device12[:, 1]
device12_x = device12_x[1:]

for i in range(0, len(device12_x)-1, 1):
    device12_x[i] = 1008-device12_x[i]

#translation for better scatter plot

for i in range(0, len(before_x), 1):
    before_x[i]= 850-before_x[i]
    before_y[i]= before_y[i]-100

for i in range(0, len(after_x), 1):
    after_x[i] = 835 - after_x[i]
    after_y[i] = after_y[i]

#plot raw data scatter plot
for i in range(1, len(before_x), 1):
    plt.scatter(before_x[i], before_y[i], c='tab:blue', s=50, alpha=0.7, edgecolors='none')
for i in range(1, len(after_x), 1):
    plt.scatter(after_x[i], after_y[i], c='tab:orange', s=50, alpha=0.7, edgecolors='none')
# Specify Bounds
plt.axis([-50, 350, 200, 800])
# Specify Axis Labels
from matplotlib.patches import Patch
from matplotlib.lines import Line2D

legend_elements = [Line2D([0], [0], marker='o', color='w', label='100nM fMLP',
                          markerfacecolor='tab:blue', markersize=10),
                   Line2D([0], [0], marker='o', color='w', label='0nM fMLP',
                          markerfacecolor='tab:orange', markersize=10),
                   ]

plt.legend(handles = legend_elements,
           loc='upper right', shadow=False)
plt.xlabel('Position along channel (um)', size=16)
plt.ylabel('Position across channel (um)', size=16)
#plt.title('Scatter plot of cells', size=16)
# Voila
plt.show()

#plot custom beehive scatter plot




for i in range(1, len(before_x), 1):
    plt.scatter(150 + random.uniform(-15, 15), before_x[i], c='tab:blue', s=50, alpha=0.7, edgecolors='none')
for i in range(1, len(after_x), 1):
    plt.scatter(50 + random.uniform(-15, 15), after_x[i], c='tab:orange', s=50, alpha=0.7, edgecolors='none')
for i in range(1, len(device9_x), 1):
        plt.scatter(100+random.uniform(-15, 15), device9_x[i], c='tab:orange', s=50, alpha=0.7, edgecolors='none')
for i in range(1, len(device2_x), 1):
        plt.scatter(200+random.uniform(-15, 15), device2_x[i], c='tab:blue', s=50, alpha=0.7, edgecolors='none')
# Specify Bounds
plt.axis([0, 250, 0, 500])
# Specify Axis Labels
from matplotlib.patches import Patch
from matplotlib.lines import Line2D

legend_elements = [Line2D([0], [0], marker='o', color='w', label='100nM fMLP',
                          markerfacecolor='tab:blue', markersize=10),
                   Line2D([0], [0], marker='o', color='w', label='0nM fMLP',
                          markerfacecolor='tab:orange', markersize=10),
                   ]
plt.xticks([50, 100, 150, 200], ['Control', 'Control', '100nM', '100nM'])
plt.legend(handles = legend_elements,
           loc='upper right', shadow=False)
#plt.xlabel('Position along channel (um)', size=16)
plt.ylabel('Distance migrated (um)', size=16)
#plt.title('Scatter plot of cells', size=16)
# Voila
plt.show()


num_bins = 40
# the histogram of the data
n, bins, patches = plt.hist(before_x, num_bins, histtype=u'step', cumulative=1,  density=1, facecolor='tab:blue',  linewidth=2.5, alpha=0.6)
n, bins, patches = plt.hist(after_x, num_bins,  histtype=u'step', cumulative=1, density=1, facecolor='tab:orange', linewidth=2.5, alpha=0.6)
plt.ticklabel_format(axis='y', style='sci', scilimits=(0, 0))


plt.axis([0, 350, 0, 1.05])
plt.ticklabel_format(axis='y', style='sci', scilimits=(0,0))
plt.xlabel('Position along axis', size=16)
plt.ylabel('Cumulative distribution function', size=16)
#plt.title(r'Cell Distribution', size=16)
legend_elements = [Line2D([0], [0], marker='o', color='w', label='100nM fMLP',
                          markerfacecolor='tab:blue', markersize=10),
                   Line2D([0], [0], marker='o', color='w', label='0nM fMLP',
                          markerfacecolor='tab:orange', markersize=10),
                   ]

plt.legend(handles = legend_elements,
           loc='upper right', shadow=False)

plt.show()


#plt.title('Cell Distribution Before and After')
data = [before_x, device2_x, device12_x, after_x]
print(np.mean(before_x), np.mean(after_x), np.mean(device2_x), np.mean(device9_x), np.mean(device12_x))
print(np.median(before_x), np.median(after_x), np.median(device2_x), np.median(device9_x), np.median(device12_x))

plt.violinplot(data)
#plt.xlabel(size=16)
plt.ylabel('Distance of migration from backstop', size=16)
#plt.title('Cell migration after alignment', size=16)
plt.show()
