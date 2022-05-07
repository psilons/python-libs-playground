import numpy
import matplotlib.pyplot as plt


with open('beijing-2021-t.txt', 'r') as f:
    lines = f.readlines()

minl = numpy.array(lines, dtype=float)
minlv = min(minl)
minl = minl - minlv  # meaning we lean the pole to an angle?
midx = numpy.argmax(minl)
nidx = numpy.argmin(minl)
maxlv = max(minl)

fig = plt.figure(figsize=(8, 8))
ax = plt.subplot(111, projection='polar')

ax.set_rticks([i*maxlv / 6 for i in range(1, 7)])  # need 6 circles
ax.set_ylim(0, maxlv)

ax.set_xticks(numpy.linspace(0,  2*numpy.pi, 25))  # need 24 sections

ax.set_xticklabels([])
ax.set_yticklabels([])

# data = minl
# theta = numpy.linspace(0, 2*numpy.pi, len(data))
# ax.plot(theta, data, color='black')
# ax.fill(theta, data, '0.8')

# re-org to 2 halves separated by min and max.
data = numpy.concatenate([minl[nidx:], minl[:midx]])
theta = numpy.linspace(0, numpy.pi, len(data))
ax.plot(theta, data, color='black')
ax.fill(theta, data, '0.3')

data = minl[midx:nidx][::-1]
theta = numpy.linspace(numpy.pi, 2*numpy.pi, len(data))
ax.plot(theta, data, color='black')
plt.fill_between(theta, maxlv, data, alpha=0.7, color='black')

# eyes, use half length?
plt.polar(numpy.pi/2, maxlv/4, marker='o', markersize=20, fillstyle='full', color='white')
plt.polar(3*numpy.pi/2, maxlv/4, marker='o', markersize=20, color='black')

# change outer circle to color red
# ax.plot(numpy.linspace(0, 2*numpy.pi, 100), numpy.ones(100)*max(minl), color='r', linestyle='-')

fig.savefig('yingyang-t.png')
plt.show()
