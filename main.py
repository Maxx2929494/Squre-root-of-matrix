from benchmark import *
from numerical_methods import *
from example_matrices import *
from convergence_plot import *

# Initialize methods
methods = [newton_method, commutating, DB, iannazoo, sqrtm]


# Intialize matrices
matrices = {
    "Diagonal": Diagonal,
    r"$I$ permutation": I_per,
    "Wilson matrix": Wilson_matrix,
    "Chebyshev": Chebyshev,
    "Non normal": Non_normal,
    "Moler matrix": Moler_matrix,
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

# Make a plot of convergence of Iannazoo
names = list(matrices.keys())
errors = []
it_list = [[k for k in range(100)]] * 8 

for name,matrix in matrices.items():
    errors.append(iannazoo(matrix,100,0,plot=True))

plot_convergence(it_list, errors, labels = names, filename='iannazoo_convergence.pdf', title="Convergence plot of IR method")