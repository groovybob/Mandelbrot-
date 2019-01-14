import numpy as np
import matplotlib.pyplot as plt
from numba import autojit

def Mandelbrot(Re, Im, max_iter ):
    c = complex(Re,Im)
    z = 0.0j

    for i in range (max_iter):
        z = z**2 + c
        if (z.real*z.real + z.imag*z.imag) >= 4:
            return i

    return max_iter
columns = 2000
rows = 2000

result = np.zeros([rows, columns])
for row_index, Re in enumerate(np.linspace(-2,2,num=rows)):
    for columns_index, Im in enumerate(np.linspace(-0.02,0.02,num=columns)):
        result[row_index, columns_index] = Mandelbrot(Re , Im , 1000)

plt.figure(dpi=100)
ax.set_facecolor('black')
plt.imshow(result.T, cmap = 'hot', interpolation='bilinear', extent=[-2,1,-1,1])
plt.savefig('image1.jpg', format='png', dpi=1000)
plt.show()


