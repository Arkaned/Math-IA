import numpy as np
import random
import matplotlib.pyplot as plt

A = [0, 135]
B = [0, 127.5]
C = [0, 120]
D = [0, 112.5]
E = [0, 105 ]
F = [0, 75]
petri = [75, 75]
Size = [0, 750]

plt.plot(Size, A, color='blue', label='AG1')
plt.plot(Size, B, color='green', label='M131')
plt.plot(Size, C, color='orange', label='AG4, M99, M109')
plt.plot(Size, D, color='black', label='M166')
plt.plot(Size, E, color='purple', label='M142')
plt.plot(Size, F, color='yellow', label='M189, M200, M211')
plt.plot(Size, petri, color='red', alpha=0.7, label='radius of petri dish', linestyle=(0, (5, 1)))
# line style numbers are collected from online database showing different number codes for different arrays of lines.
plt.legend()
plt.grid()
plt.xlabel('time/hours')
plt.ylabel('Radius of Mycelium/mm')
plt.title('Radius of Mycelium Over Time')

plt.show()