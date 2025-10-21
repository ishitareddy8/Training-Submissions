# Import the NumPy library
import numpy as np

# Create two arrays
arr1 = np.array([3, 6, 9, 12, 15])
arr2 = np.array([2, 3, 6, 8, 10])

print("Array 1:", arr1)
print("Array 2:", arr2)

# Element-wise arithmetic operations
print("\n--- Element-wise Operations ---")
print("Addition:", arr1 + arr2)
print("Subtraction:", arr1 - arr2)
print("Multiplication:", arr1 * arr2)
print("Division:", arr1 / arr2)
print("Power:", arr1 ** arr2)
print("Modulus:", arr1 % arr2)

# Comparison operations
print("\n--- Comparison Operations ---")
print("arr1 > arr2:", arr1 > arr2)
print("arr1 < arr2:", arr1 < arr2)
print("arr1 == arr2:", arr1 == arr2)

# Aggregate functions
print("\n--- Aggregate Functions ---")
print("Sum of arr1:", np.sum(arr1))
print("Mean of arr2:", np.mean(arr2))
print("Maximum value in arr1:", np.max(arr1))
print("Minimum value in arr2:", np.min(arr2))

# Vectorized operation example (faster than loops)
print("\n--- Vectorized Operation Example ---")
result = arr1 * 2 + arr2
print("Result of arr1 * 2 + arr2:", result)
