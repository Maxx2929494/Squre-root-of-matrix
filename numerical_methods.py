import numpy as np
from scipy.linalg import solve_sylvester, norm, inv, sqrtm 

# Method 1: standard Newton's method.
def newton_method(A, max_k: int, tol: float):
    # Dimension + initialize identity 
    n = A.shape[0]
    X = np.identity(n)
    X_k = X.copy()

    for k in range(max_k):
        
        # Obtain H by solving sylvester equation
        RHS = A - X @ X
        H = solve_sylvester(X,X,RHS)  

        # Iteration step
        X_k = X + H

        # Convergence check
        if norm(H, 'fro') < tol:
            return X_k
    
        X = X_k

    return X_k


# Method 2: commutating Newton's method
def DB(A, max_k: int, tol: float):
    # Dimension + initialize Y 
    n = A.shape[0]
    Y = A.copy()

    # Iteration step
    for k in range(max_k):
        Y_k = 0.5 * (Y + inv(Y) @ A)

        #convergence check
        if norm(Y_k - Y, 'fro') < tol:
            return Y_k

        Y = Y_k


    return Y

# Method 3: Iannazzo's iteration
def iannazoo(A, max_k: int, tol: float):
    # Dimension + initialize X and E
    n = A.shape[0]
    X = A.copy()
    E = 0.5 * ( np.identity(n) - A )

    #iteration step
    for k in range(max_k):
        X_k = X + E 
        E_k = -0.5 * E @ inv(X_k) @ E

        # Convergence check
        if norm(E, 'fro') < tol:
            return X_k
        
        X,E = X_k,E_k

    return X


# Method 4: Schur's method implented by Scipy
schur_method = sqrtm