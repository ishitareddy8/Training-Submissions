import numpy as np

a = np.array([1, 4, 8, 14], dtype=float)
b = np.array([2, 26, 8, 25], dtype=float)

if a.shape != b.shape:
    raise ValueError("Arrays must have the same shape for element-wise multiplication")

result = a * b

print("Array A:", a)
print("Array B:", b)
print("Element-wise multiplication of the Numpy Arrays:", result)
