# KUKA KR16 Pneumatic Gripper Analysis

## Objective
Automate the required gripping force calculations for a custom 3D-printed end-effector handling a 2kg payload, ensuring a factor of safety of 2.0.

## Engineering Logic
The script calculates dynamic required force factoring in gravitational and maximum robotic acceleration forces, utilizing the formula for frictional grip limits. 

## Results
The automated Matplotlib output identified the exact failure boundary:
* **Max Cylinder Output:** 60N
* **Failure Point:** 8.2 m/s² max acceleration.
* **Recommendation:** Upgrade gripper pad material to high-friction polyurethane to safely achieve 10 m/s² cycle times.

![Force Plot](force_vs_acceleration_plot.png)
