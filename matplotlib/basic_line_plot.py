import matplotlib.pyplot as plt
import numpy as np

x = np.array([2, 9])
y = np.array([7, 1])

plt.plot(x, y)
plt.savefig('basic_line_plot.png')  # savefig must happen before show()
plt.show()
