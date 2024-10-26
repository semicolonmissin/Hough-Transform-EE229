import numpy as np
import matplotlib.pyplot as plt


# Define a set of points in image space
points = [(1,1), (3,3), (5,5)]  # Points lying on a line 
# Create a range of theta values from 0 to pi
theta = np.deg2rad(np.arange(0, 180))


# Prepare to plot the Hough transform (r-theta space)
fig, ax = plt.subplots(1, 2, figsize=(10, 5))


# Image space plot
ax[0].set_title('Points in Image Space')
ax[0].set_xlabel('x')
ax[0].set_ylabel('y')
ax[0].grid(True)


# Hough transform plot
ax[1].set_title('Lines in Hough Space (r-theta)')
ax[1].set_xlabel('Theta (radians)')
ax[1].set_ylabel('r')
ax[1].grid(True)


# Plot the points in image space
for point in points:
    ax[0].scatter(*point, color='red')
    ax[0].annotate(f'({point[0]}, {point[1]})', (point[0] + 0.2, point[1] + 0.2))


# For each point in image space, compute the corresponding sinusoidal line in Hough space
for x, y in points:
    r = x * np.cos(theta) + y * np.sin(theta)
    ax[1].plot(theta, r, label=f'Point ({x}, {y})')


ax[1].legend()


plt.tight_layout()
plt.show()