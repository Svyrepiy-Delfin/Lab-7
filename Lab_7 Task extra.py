import matplotlib.pyplot as plt
import numpy as np
from matplotlib.animation import FuncAnimation, PillowWriter

fig, ax = plt.subplots()
x = np.arange(0, 2 * np.pi, 0.01)
line, = ax.plot(x, np.sin(x))


def update(frame):
    line.set_ydata(np.sin(x + frame / 10.0))
    return line,


ani = FuncAnimation(fig, update, frames=100, blit=True)
writer = PillowWriter(fps=20)
ani.save("sin_animation.gif", writer=writer)
