import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy
import random


def magnitude(x,y):
    return numpy.sqrt((x-0.5)**2 + (y-0.5)**2)

def gen_pt():
    return random.random(), random.random()

def calc_pi(in_pts, out_pts):
    return 4 * (in_pts / (out_pts + in_pts))


fig, ax = plt.subplots()

circle = plt.Circle((0.5,0.5), 0.5, edgecolor='r', facecolor='none')
ax.add_patch(circle)

ax.set_xlim(0,1)
ax.set_ylim(0,1)
ax.set_aspect(1)

plt.axis()

points_x, points_y = [], []
point_plot, = ax.plot([], [], 'o', markersize=2)

text = ax.text(0.02, 1.05, '', transform=ax.transAxes)

in_pts = 1
out_pts = 1

def update(frame):
    global in_pts, out_pts

    x, y = gen_pt()
    points_x.append(x)
    points_y.append(y)

    if magnitude(x,y) < 0.5:
        in_pts += 1 
    else: 
        out_pts += 1
    

    point_plot.set_data(points_x, points_y)
    text.set_text(f'$\pi = {str(calc_pi(in_pts, out_pts))}$')

    return point_plot,

# Create an animation that calls the update function every 1000ms (1 second)
ani = animation.FuncAnimation(fig, update, interval=3)



plt.show()