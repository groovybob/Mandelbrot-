import math
import random
import numpy as np


# set up an array of real numbers between -2+-1j and 2+~2j

size = int(input("how many numbers would you like to use?"))
# notes 
#randomly generate complex mumbers and assess if fit in BMset
sets = np.array([])
for n in range(size):
    rand1 = random.randint(-2000000,2000000)/1000000
    rand2 = random.randint(-2000000,2000000)/1000000
    complex_num = complex(rand1,rand2)
    #print(complex_num)



    sets = np.append(sets,complex_num)


print(sets)