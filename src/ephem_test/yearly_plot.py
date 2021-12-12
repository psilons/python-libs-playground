import os
import numpy
import matplotlib.pyplot as plt


with open('beijing-2021.txt', 'r') as f:
    lines = f.readlines()

minl = numpy.array(lines, dtype=float)
minl = minl - min(minl)
midx = numpy.argmax(minl)
nidx = numpy.argmin(minl)
maxlv = max(minl)

fig = plt.figure(figsize=(8, 8))
ax = plt.subplot(111, projection='polar')

ax.set_rticks([i*maxlv / 6 for i in range(1, 7)])  # need 6 circles
ax.set_ylim(0, maxlv)

ax.set_xticks(numpy.linspace(0,  2*numpy.pi, 25))  # need 24 sections

# re-org to 2 halves separated by min and max.
data = numpy.concatenate([minl[midx:], minl[:nidx+1]])[::-1]
theta = numpy.linspace(0, numpy.pi, len(data))
ax.plot(theta, data, color='black')
ax.fill(theta, data, '0.8')

data = minl[nidx:midx]
theta = numpy.linspace(numpy.pi, 2*numpy.pi, len(data))
ax.plot(theta, data, color='black')

plt.fill_between(theta, maxlv, data, alpha=0.2, color='black')

# change outer circle to color red
# ax.plot(numpy.linspace(0, 2*numpy.pi, 100), numpy.ones(100)*max(minl), color='r', linestyle='-')

ax.set_xticklabels([])
ax.set_yticklabels([])

plt.show()
fig.savefig('yingyang.png')
