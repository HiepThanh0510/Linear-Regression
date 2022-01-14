
from __future__ import division, print_function, unicode_literals
import numpy as np 
import matplotlib.pyplot as plt

# Area (cm^2)
X = np.array([[230.30, 234.06, 220.60, 227.70, 251.07, 245.40, 214.10, 208.20, 238.35, 231.8, 216.77, 231.08, 214.10, 
               274.25, 253.58, 244.89, 248.10, 237.16, 231.26, 250.66, 235.76, 234.70, 224.60, 232.06, 270.70, 268.30, 
               242.90, 252.60, 255.20, 233.91, 248.40, 254.20, 242.0, 239.9, 292.10, 309.80, 296.20, 265.95, 308.10, 296, 
               273.70, 266, 273.3, 285.3, 251.35, 240.08, 242.99, 246.30, 230.10, 224.29]]).T
# weight (kg)
y = np.array([[388, 428, 352, 374, 450, 462, 332, 338, 444, 388, 408, 388, 360, 570, 492, 496, 462, 436, 432, 464, 418, 
               442, 408, 428, 558, 512, 490, 480, 512, 460, 484, 528, 498, 442, 610, 746, 678, 574, 684, 638, 602, 600, 616, 
               584, 482, 454, 484, 484, 440, 388]]).T

Matrix_One = np.ones((X.shape[0], 1))
Xbar = np.concatenate((Matrix_One, X), axis = 1)

# Calculating weights of the fitting line 
A = np.dot(Xbar.T, Xbar)
b = np.dot(Xbar.T, y)
w = np.dot(np.linalg.pinv(A), b)
print('w = ', w)

w_0 = w[0][0]
w_1 = w[1][0]
x0 = np.linspace(200, 310, 2)
y0 = w_0 + w_1*x0


plt.plot(X.T, y.T, 'ro')      
plt.plot(x0, y0)               
plt.axis([200, 310, 300, 800])
plt.xlabel('Area (cm^2)')
plt.ylabel('Weight (kg)')
plt.show()