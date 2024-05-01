import numpy as np
from matplotlib import pyplot as plt
import scipy.stats as stats

# x = np.random.normal(5.0, 1.0, 100000)
#
# plt.hist(x,100)
# plt.show()

#
x = [5, 7, 8, 7, 2, 17, 2, 9, 4, 11, 12, 9, 6]
y = [99, 86, 87, 88, 111, 86, 103, 87, 94, 78, 77, 85, 86]

slope, intercept, r, p, std_err = stats.linregress(x, y)


def myfunc(x):
    return slope * x + intercept


myModel = list(map(myfunc, x))

plt.scatter(x, y)
plt.plot(x, myModel)
plt.show()
