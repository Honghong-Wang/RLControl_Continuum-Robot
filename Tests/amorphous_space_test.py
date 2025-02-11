# %%
import sys # to include the path of the package
sys.path.append('../Reinforcement Learning') # AmorphousSpace.py is in the parent directory
from AmorphousSpace import AmorphousSpace

import numpy as np
import matplotlib.pyplot as plt

circles = [{'center': np.array([-0.1, -0.07]), 'radius': 0.03},
           {'center': np.array([-0.08, -0.07]), 'radius': 0.023},
           {'center': np.array([-0.15, 0.00]), 'radius': 0.025},
           {'center': np.array([-0.15, -0.07]), 'radius': 0.03},
           {'center': np.array([-0.155, 0.01]), 'radius': 0.025},
           {'center': np.array([-0.16, 0.02]), 'radius': 0.025},
           {'center': np.array([-0.165, 0.03]), 'radius': 0.025},
           {'center': np.array([-0.13, -0.04]), 'radius': 0.025},
           {'center': np.array([-0.15, 0.06]), 'radius': 0.025},
           {'center': np.array([-0.15, 0.17]), 'radius': 0.06},
           {'center': np.array([-0.12, 0.20]), 'radius': 0.025},
           {'center': np.array([-0.196, 0.1]), 'radius': 0.06},
           {'center': np.array([-0.2, 0.0]), 'radius': 0.04},
           {'center': np.array([-0.2, 0.09]), 'radius': 0.06},
           {'center': np.array([-0.2, 0.08]), 'radius': 0.06},
           {'center': np.array([-0.2, 0.07]), 'radius': 0.065},
           {'center': np.array([-0.2, 0.07]), 'radius': 0.06},
           {'center': np.array([-0.2, 0.06]), 'radius': 0.06},
           {'center': np.array([-0.2, 0.05]), 'radius': 0.06},
           {'center': np.array([-0.2, 0.04]), 'radius': 0.06},
           {'center': np.array([-0.2, 0.03]), 'radius': 0.06},
           {'center': np.array([-0.205, 0.05]), 'radius': 0.06},
           {'center': np.array([-0.16, -0.05]), 'radius': 0.04},
           {'center': np.array([-0.17, 0.17]), 'radius': 0.05},
           {'center': np.array([-0.15, 0.12]), 'radius': 0.03},
           {'center': np.array([-0.143, 0.16]), 'radius': 0.04},
           {'center': np.array([-0.15, 0.20]), 'radius': 0.044},
           {'center': np.array([-0.2, 0.15]), 'radius': 0.035},
           {'center': np.array([-0.21, 0.14]), 'radius': 0.033},
           {'center': np.array([-0.12, -0.07]), 'radius': 0.033},
           {'center': np.array([-0.18, -0.03]), 'radius': 0.043},
           {'center': np.array([-0.10, 0.25]), 'radius': 0.03},
           {'center': np.array([-0.10, 0.23]), 'radius': 0.03},
           {'center': np.array([-0.13, 0.235]), 'radius': 0.027},
           {'center': np.array([-0.06, 0.26]), 'radius': 0.025},
           {'center': np.array([-0.06, 0.268]), 'radius': 0.025},
           {'center': np.array([-0.07, 0.268]), 'radius': 0.023},
           {'center': np.array([-0.05, 0.268]), 'radius': 0.023},
           {'center': np.array([-0.04, 0.268]), 'radius': 0.023},
           {'center': np.array([-0.04, 0.272]), 'radius': 0.023},
           {'center': np.array([-0.03, 0.273]), 'radius': 0.021},
           {'center': np.array([-0.02, 0.275]), 'radius': 0.019},
           {'center': np.array([-0.02, 0.278]), 'radius': 0.020},
           {'center': np.array([-0.015, 0.28]), 'radius': 0.020},
           {'center': np.array([-0.015, 0.28]), 'radius': 0.020},
           {'center': np.array([-0.012, 0.28]), 'radius': 0.020},
           {'center': np.array([-0.011, 0.28]), 'radius': 0.020},
           {'center': np.array([-0.010, 0.28]), 'radius': 0.020},
           {'center': np.array([-0.009, 0.28]), 'radius': 0.020},
           {'center': np.array([-0.008, 0.28]), 'radius': 0.020},
           {'center': np.array([-0.007, 0.28]), 'radius': 0.020},
           {'center': np.array([-0.006, 0.28]), 'radius': 0.020},
           {'center': np.array([-0.005, 0.28]), 'radius': 0.020},
           {'center': np.array([0.00, 0.28]), 'radius': 0.0150},
           {'center': np.array([0.005, 0.285]), 'radius': 0.0150},
           {'center': np.array([0.0075, 0.285]), 'radius': 0.0150},
           {'center': np.array([0.01, 0.285]), 'radius': 0.0150},
           {'center': np.array([0.015, 0.285]), 'radius': 0.0150},
           {'center': np.array([0.02, 0.285]), 'radius': 0.0150},
           {'center': np.array([0.03, 0.285]), 'radius': 0.012},
           {'center': np.array([0.04, 0.285]), 'radius': 0.012},
           {'center': np.array([0.05, 0.285]), 'radius': 0.010},
           {'center': np.array([0.06, 0.28]), 'radius': 0.012},
           {'center': np.array([0.07, 0.28]), 'radius': 0.012},
           {'center': np.array([0.08, 0.275]), 'radius': 0.012},
           {'center': np.array([0.09, 0.276]), 'radius': 0.01},
           {'center': np.array([0.1, 0.275]), 'radius': 0.01},
           {'center': np.array([0.11, 0.27]), 'radius': 0.01},
           {'center': np.array([0.12, 0.265]), 'radius': 0.01},
           {'center': np.array([0.13, 0.255]), 'radius': 0.01},
           {'center': np.array([0.14, 0.245]), 'radius': 0.01},
           {'center': np.array([0.15, 0.235]), 'radius': 0.01},
           {'center': np.array([-0.2, 0.000]), 'radius': 0.05},
           {'center': np.array([-0.2, -0.0150]), 'radius': 0.045},
           {'center': np.array([-0.15, 0.075]), 'radius': 0.025},
           {'center': np.array([-0.10, 0.2]), 'radius': 0.020},
           {'center': np.array([-0.080, 0.21]), 'radius': 0.020},
           {'center': np.array([-0.22, 0.17]), 'radius': 0.01},
           {'center': np.array([-0.215, 0.177]), 'radius': 0.012},
           {'center': np.array([-0.225, 0.165]), 'radius': 0.01},
           {'center': np.array([-0.125, 0.225]), 'radius': 0.045},]
space = AmorphousSpace(circles)
print('Shape of the State: ',space.shape[0]*2)
# Generate a random point in the space
point = space.sample() #[0.06,0.074]
print('Sample Point is ',point)

# Check if the point is within the bounds of the space
print('The point is within the bounds of the space: ',space.contains(point))

# Clip the point to the bounds of the space
clipped_point = space.clip(point)
print('Clip the point to the bounds of the space: ',clipped_point)

# Plot the amorphous space
fig, ax = plt.subplots()
for circle in space.circles:
    ax.add_artist(plt.Circle(circle['center'], circle['radius'], fill=False))
ax.scatter(clipped_point[0],clipped_point[1])
ax.set_title('Space for the Continuum Robot Consisting of Several Circular Shapes')
ax.set_xlabel('X [m]')
ax.set_ylabel('Y [m]')
ax.set_xlim(-0.3, 0.2)
ax.set_ylim(-0.15, 0.3)
plt.show()
# %%
