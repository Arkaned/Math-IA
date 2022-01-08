import numpy as np
import random
import matplotlib.pyplot as plt

time = [i for i in range(600)]
A = [0.001+0.09*i**2 for i in time]
B = [0.001+0.085*i**2 for i in time]
C = [0.001+0.08*i**2 for i in time]
D = [0.001+0.075*i**2 for i in time]
E = [0.001+0.07*i**2 for i in time]
F = [0.001+0.05*i**2 for i in time]
petri = [17671.459 for i in time]

plt.plot(time, A, color='blue', label='AG1')
plt.plot(time, B, color='green', label='M131')
plt.plot(time, C, color='orange', label='AG4, M99, M109')
plt.plot(time, D, color='black', label='M166')
plt.plot(time, E, color='purple', label='M142')
plt.plot(time, F, color='yellow', label='M189, M200, M211')
plt.plot(time, petri, color='red', alpha=0.7, label='Area of petri dish', linestyle=(0, (5, 1)))
# line style numbers are collected from online database showing different number codes for different arrays of lines.
# HELP HERE, WE NEED TO FIGURE OUT HOW TO SET TICKS

plt.legend()
plt.grid()
plt.xlabel('time/hours')
plt.ylabel('Area of Mycelium/mm^2')
plt.title('Area of Mycelium Over Time')

plt.show()

