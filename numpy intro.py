import numpy as np

arr = np.random.randint(1,500,100)
print(arr)

# Remove Duplicate Values
x = np.unique(arr)
print(x)

y = np.sort(x)
print(y)
print("After Duplication Remove length ", len(y))
print("Original Length" ,len(arr))
