import numpy as np
import matplotlib.pyplot as plt

N = 5

x1 = np.linspace(0, 5, N, endpoint=True)
x2 = np.linspace(0, 5, N, endpoint=False)
x3 = np.arange(0,5)
x4 = np.arange(0,6)

y1 = np.zeros(N)
y2 = np.ones(N)
y3 = np.ones(N) - 0.2
y4 = np.zeros(N + 1) - 0.2
print(y3)
print(y4)

plt.title("numpy.linspace(), N = number of samples = 5")
plt.plot(x1, y1, 'D', color='salmon')
plt.plot(x2, y2, 'D', color='seagreen')
plt.plot(x3, y3, 'D', color='mediumseagreen')
plt.plot(x4, y4, 'D', color='lightsalmon')
plt.ylim([-0.7, 1.5])
plt.yticks([-0.2, 0, 0.8, 1], 
    ['numpy\n.arange(0,6)', 
     'linspace(0,5,N,\nendpoint=True)', 
     'numpy\n.arange(0,5)', 
     'linspace(0,5,N,\nendpoint=False)'])
plt.subplots_adjust(left=0.2)
plt.show()
