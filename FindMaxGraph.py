import numpy as np
from FindMax import findSecondDNCWithCount, findSecondLinearWithCount
from matplotlib import pyplot as plt

array_sizes = range(2, 200, 1)
dnc_comparisons = []
linear_comparisons = []

for i in array_sizes:
    dnc_total = 0
    linear_total = 0
    sample_num = 100
    for j in range(sample_num):
        random_array = np.random.randint(1, 100, i)
        dnc_total += findSecondDNCWithCount(random_array)[1]
        linear_total += findSecondLinearWithCount(random_array)[1]
    dnc_comparisons.append(dnc_total / sample_num)
    linear_comparisons.append(linear_total / sample_num)
    
line1, = plt.plot(array_sizes, dnc_comparisons, label='DNC')
line2, = plt.plot(array_sizes, linear_comparisons, label='Linear')
plt.ylabel('Comparisons')
plt.xlabel('Array size')
plt.legend(handles=[line1, line2])
plt.show()