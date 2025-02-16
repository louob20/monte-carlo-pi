import matplotlib.pyplot as plt
import numpy
import random


def magnitude(x,y):
    return numpy.sqrt((x-0.5)**2 + (y-0.5)**2)

def gen_pt():
    return random.random(), random.random()





fig, ax = plt.subplots()
circle = plt.Circle((0.5,0.5), 0.5, edgecolor='r', facecolor='none')
ax.add_patch(circle)
ax.set_xlim(0,1)
ax.set_ylim(0,1)
ax.set_aspect(1)
plt.axis()

x,y = gen_pt()
ax.plot(x , y, marker='o', markersize=1, color='b')



plt.show()