import matplotlib.pyplot as plt


def pid_controller(target, current, prev_error, integral, dt):
    kp = 2.0
    ki = 0.
    kd = 0.8
    
    error = target - current
    p = kp * error
    new_integral = integral + (error * dt)
    i = ki * new_integral
    d = kd * ((error - prev_error) / dt)
    
    voltage = p + i + d
    return voltage, error, new_integral

torque_constant = 5.0
friction_coefficient = 2.0
time_step = 0.01

current_angle = 0.0
velocity = 0.0
previous_error = 0.0
accumulated_integral = 0.0

target_angle = 90.0

time_data = []
angle_data = []
target_data = []

#(Running for 3 seconds / 300 steps)
for step in range(300):
    current_time = step * time_step
    
    voltage, previous_error, accumulated_integral = pid_controller(target_angle, current_angle, previous_error, accumulated_integral, time_step)

    acceleration = (voltage * torque_constant) - (velocity * friction_coefficient)
    velocity += acceleration * time_step
    current_angle += velocity * time_step

    time_data.append(current_time)
    angle_data.append(current_angle)
    target_data.append(target_angle)

plt.plot(time_data, angle_data, label="Motor Angle", color="blue")
plt.plot(time_data, target_data, label="Target Angle", color="red", linestyle="--")
plt.title("PID Control of DC Motor Step Response")
plt.xlabel("Time (seconds)")
plt.ylabel("Angle (degrees)")
plt.legend()
plt.grid(True)
plt.show()