import matplotlib.pyplot as plt
import scipy.signal as signal

numerator = [10]
denominator = [1, 2, 10]

dc_motor_system = signal.TransferFunction(numerator, denominator)

time, response = signal.step(dc_motor_system)

plt.plot(time, response, label = "Transfer function")
plt.xlabel("Time (s)")
plt.ylabel("Amplitude")
plt.grid(True)
plt.legend()
plt.show()
