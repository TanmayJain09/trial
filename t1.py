import numpy as np
import matplotlib.pyplot as plt
from matplotlib import animation

# grid
m, n = 20, 20
x = np.arange(n)
y = np.arange(m)
X, Y = np.meshgrid(x, y)

def surface(t):
    return np.sin(0.2 * X + t) * np.cos(0.2 * Y)

fig = plt.figure()
ax = fig.add_subplot(projection='3d')

ax.set_zlim(-1.5, 1.5)
ax.set_xlabel("X")
ax.set_ylabel("Y")
ax.set_zlabel("Z")

Z = surface(0)

surf = ax.plot_surface(X, Y, Z, cmap='coolwarm')

def update(frame):
    ax.collections.clear()
    Z = surface(frame * 0.1)
    surf = ax.plot_surface(X, Y, Z, cmap='coolwarm')
    return surf,

ani = animation.FuncAnimation(
    fig,
    update,
    frames=100,
    interval=100,
    blit=False
)

plt.show()
