import numpy as np
import operator
import matplotlib.pyplot as plt
import json
import os

# directory = '.'
# d = {}
# for filename in os.listdir(directory):
#     if filename.endswith(".npy"):
#         t = np.load(filename)
#         d[filename[:-4]] = float(t)

# j = json.dumps(d)
# f = open("woloop.json","w")
# f.write(j)
# f.close()


plt.style.use(['science','no-latex'])

with open('withloop.json') as json_file:
    d_w = json.load(json_file)
d_w = dict(sorted(d_w.items(), key=operator.itemgetter(1)))


with open('woloop.json') as json_file:
    d_wo = json.load(json_file)
d_wo = dict(sorted(d_wo.items(), key=operator.itemgetter(1)))


fig, axes = plt.subplots(figsize=(5,5))
axes.scatter(d_w.keys(), d_w.values())
axes.scatter(d_wo.keys(), d_wo.values())
axes.legend(['With nested loops','W/O nested loops'])
axes.set_ylabel('Time (s)', fontsize=16)
axes.set_xlabel('Model-resolution', fontsize=16)

chartBox = axes.get_position()
axes.set_position([chartBox.x0, chartBox.y0*2, 
                 chartBox.width, 
                 chartBox.height]) 
plt.xticks(rotation=90)

plt.show()