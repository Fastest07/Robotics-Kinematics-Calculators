import math as m
import numpy as np

def pid_controller(target_angle, current_angle, previous_error, accumulated_integral, time_step):
        kp = 0.1
        ki = 0
        kd = 0
        current_error = target_angle - current_angle
        new_accumulated_integral = accumulated_integral + (current_error * time_step)
        derivative = (current_error - previous_error)/ time_step
        p = kp * current_error
        i = ki * new_accumulated_integral
        d = kd * derivative
        motor_voltage = p + new_accumulated_integral + derivative
        return(motor_voltage, current_error, new_accumulated_integral)


previous_error = 0.0
accumulated_integral = 0.0
dt = 0.01

#for time t in range(100):

        #motor_voltage, previous_error, accumulated_integral = pid_controller(
          #     current_angle,
          #     previous_error,
          #    accumulated_integral,
          #    dt
 #       )
