
import numpy as np

def matrix_calculator():
    print("Enter elements for 2x2 Matrix A (space-separated):")
    A = np.array(list(map(float, input().split()))).reshape(2, 2)

    print("Enter elements for 2x2 Matrix B (space-separated):")
    B = np.array(list(map(float, input().split()))).reshape(2, 2)

    print("\n🧮 Matrix Calculator Results:")
    print("A + B =\n", A + B)
    print("A - B =\n", A - B)
    print("A × B =\n", np.dot(A, B))
    print("Transpose of A =\n", A.T)
    print("Transpose of B =\n", B.T)

if __name__ == "__main__":
    matrix_calculator()
