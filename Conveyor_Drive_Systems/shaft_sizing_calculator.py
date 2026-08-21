import matplotlib.pyplot as plt
from math import pi

def shaft_size_calculator(torque, allowable_shear_stress):
    d = ((16 * torque)/(pi * allowable_shear_stress))**(1/3)
    return d

allowable_shear_stress = 40*(10**6)
torque_list = []
diameter_list = []

for torque in range(100, 1100, 100):
    diameter = (shaft_size_calculator(torque, allowable_shear_stress))*1000
    torque_list.append(torque)
    diameter_list.append(diameter)

plt.plot(torque_list, diameter_list, label="1045 Carbon Steel")

plt.title("Required Shaft Diameter (mm) vs. Applied Torque (N·m)")
plt.xlabel("Torque (N.m)")
plt.ylabel("Diameter (mm)")
plt.legend()
plt.show()


