import numpy as np

# Easy diagonal matrix (check if methods work)
Diagonal = np.array([[2,0],[0,2]])

# Pertubation of identityi
A = lambda n: np.eye(n) + np.outer(np.arange(1, n+1)**2, np.arange(n)**2)
I_per = A(10)

# Wilson's matrix
Wilson_matrix = np.array([[10, 7, 8, 7], [7, 5, 6, 5], [8, 6, 10, 9], [7, 5, 9, 10]])

# VanderMonde matrix of Chebyshev polynomial
Chebyshev = np.polynomial.chebyshev.chebvander([59,89,45,71,56], 4)

# Generate moderately non-normal 8x8 matrix
T = np.triu(np.random.randn(8,8))
Q = np.linalg.qr ( np.random.randn(8,8) )[0]
Non_normal = Q @ T @ Q.transpose()

# Moler matrix (found in MATLAB, 15 eigenvalues order 1 and 1 order 10**(-9) )
Moler_matrix = np.zeros((16,16))
for i in range(16):
    for j in range(16):
        Moler_matrix[i, j] = max(i+1, j+1) - 2
        if i == j:
            Moler_matrix[i, j] += 1


# Singular matrix 4x4
Singular = np.array([[2, 1, 0, 0],
              [1, 2, 1, 0],
              [0, 1, 2, 1],
              [0, 0, 0, 0]])

# Hermitian matrix of dimension 2**13 = 16384
n = 2**13
X = np.random.randn(n, n) + 1j * np.random.randn(n, n)
Hermitian = 0.5 * (X + X.conj().T)