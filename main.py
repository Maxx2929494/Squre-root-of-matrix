from benchmark import *
from numerical_methods import *
from example_matrices import *

# Initialize methods
methods = [newton_method, commutating, DB, iannazoo, sqrtm]


# Intialize matrices
matrices = {
    "Diagonal": Diagonal,
    "I_per": I_per,
    "Wilson_matrix": Wilson_matrix,
    "Chebyshev": Chebyshev,
    "Non_normal": Non_normal,
    "Moler_matrix": Moler_matrix,
    "Singular": Singular,
    "Hermitian": Hermitian
}

# time test of all methods and all matrices
k = 100
tol = 10**(-20)
repeat = 10

if __name__ == "__main__":
    for name, matrix in matrices.items():
        for method in methods:
            print(f"---Results for matrix {name}---") 
            if method == sqrtm:
                benchmark(matrix, method, repeat) 

            else:
                benchmark(matrix, method, repeat, k, tol)
