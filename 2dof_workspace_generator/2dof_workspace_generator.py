import matplotlib.pyplot as plt
import math as m

l1 = 0.1
l2 = 0.08

workspace_x = []
workspace_y = []

for angle1 in range(0, 181):
    for angle2 in range(-180, 181):
        
        a1 = m.radians(angle1)
        a2 = m.radians(angle2)
        
        x1 = l1 * m.cos(a1)
        y1 = l1 * m.sin(a1)

        x2 = x1 + l2 * m.cos(a1+a2)
        y2 = y1 + l2 * m.sin(a1+a2)
        if y2 >= 0 :
            workspace_x.append(x2)
            workspace_y.append(y2)

plt.scatter(workspace_x, workspace_y, s=1)
plt.title("2-DOF Kinematic Workspace with Collision Constraint")
plt.xlabel("X-axis (meters)")
plt.ylabel("Y-axis (meters)")
plt.grid(False)
plt.show()

