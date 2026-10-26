import numpy as np
import matplotlib.pyplot as plt
from math import pi, cos, sin

# 1. Denavit-Hartenberg Transformation Matrix Engine
def dh_matrix(theta, d, a, alpha):
    return np.array([
        [cos(theta), -sin(theta)*cos(alpha),  sin(theta)*sin(alpha), a*cos(theta)],
        [sin(theta),  cos(theta)*cos(alpha), -cos(theta)*sin(alpha), a*sin(theta)],
        [0,           sin(alpha),             cos(alpha),            d],
        [0,           0,                      0,                     1]
    ])

# 2. Hardware Dimensions (meters)
d1 = 0.10  # Base height
a2 = 0.10  # Upper arm length
a3 = 0.08  # Forearm length

workspace_x = []
workspace_y = []
workspace_z = []

# 3. The 3D Nested Loop (Stepping by 10 degrees to save RAM)
for t1 in range(-90, 91, 10):       # Base rotation (Yaw)
    for t2 in range(0, 181, 10):    # Shoulder pitch
        for t3 in range(-180, 181, 10): # Elbow pitch
            
            # Convert degrees to radians
            theta1 = np.radians(t1)
            theta2 = np.radians(t2)
            theta3 = np.radians(t3)
            
            # 4. Generate the DH Matrices
            # Base to Shoulder (alpha = pi/2 twists the Z-axis 90 degrees so the shoulder pitches)
            T1 = dh_matrix(theta1, d1, 0, pi/2)
            # Shoulder to Elbow (alpha = 0 because the axes are parallel)
            T2 = dh_matrix(theta2, 0, a2, 0)
            # Elbow to Fingertip
            T3 = dh_matrix(theta3, 0, a3, 0)
            
            # 5. Matrix Multiplication (@ is Python's symbol for matrix multiplication)
            T0_3 = T1 @ T2 @ T3
            
            # 6. Extract the Final Coordinates
            # The X, Y, Z position is always stored in the top 3 rows of the last column of the matrix
            x = T0_3[0, 3]
            y = T0_3[1, 3]
            z = T0_3[2, 3]
            
            # 7. Collision Constraint (Don't smash through the table at Z=0)
            if z >= 0:
                workspace_x.append(x)
                workspace_y.append(y)
                workspace_z.append(z)

# 8. 3D Plotting
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d') # Tell Matplotlib we are in 3D now
ax.scatter(workspace_x, workspace_y, workspace_z, s=2, alpha=0.3)

ax.set_title("3-DOF Kinematic Workspace (DH Parameters)")
ax.set_xlabel("X-axis (meters)")
ax.set_ylabel("Y-axis (meters)")
ax.set_zlabel("Z-axis (meters)")
plt.show()