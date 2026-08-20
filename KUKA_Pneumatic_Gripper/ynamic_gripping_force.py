import matplotlib.pyplot as plt

def calculate_gripping_force(mass, friction_coefficient, acceleration,number_of_fingers,gravity = 9.81, factor_of_safety=2):
    force = (mass*(acceleration+gravity)*factor_of_safety)/(friction_coefficient*number_of_fingers)
    return force

mass = 2
friction_coefficient = 0.6
number_of_fingers = 2
acceleration_list = []
force_list = []

for acceleration in range(0,11,1):
    force = calculate_gripping_force(mass, friction_coefficient, acceleration,number_of_fingers)
    acceleration_list.append(acceleration)
    force_list.append(force)

plt.plot(acceleration_list, force_list)
plt.axhline(y=60, color='r', linestyle='--', label='Max Gripper Capacity (60N)')

plt.title("Required Gripping Force vs. Robot Acceleration")
plt.xlabel("Acceleration (m/s^2)")
plt.ylabel("Required Force (N)")
plt.legend()
plt.show()
