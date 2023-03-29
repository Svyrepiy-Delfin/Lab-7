import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np

x = np.linspace(-np.pi, np.pi)
y = x
z = np.tan(x)
fig = plt.figure()
ax = fig.add_subplot(projection='3d')
ax.plot(x, y, z, label='parametric curve')
plt.show()