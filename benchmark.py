import time
import numpy as np
from scipy.linalg import norm 


# Define function that measures time and relative error
def benchmark(A, func, repeat, k=None, tol=None):

    # Intialize times and resulting square root
    times = []
    result = A.copy()

    # Repeat time test k times
    for _ in range(repeat):
        start = time.time()

        try:
            # Seperate schur_method
            if k == None:
                result = func(A)
            else:
                result = func(A, k, tol)

        except np.linalg.LinAlgError as e:
            print(f"Method {func.__name__} failed on this matrix: {e}")
            break  # stop repeating if it fails

        times.append( time.time() - start )

    # Relative error of method
    rel_error = norm(result @ result - A, 'fro')

    print(f'Method: {func.__name__}') 
    print(f'Condition number: {np.linalg.cond(A)}')
    print(f'Average time: {np.mean(times):.6f} sec')
    print(f'Relative error method: {rel_error:.6e}')
    print(f'--------------------------------------------------------\n')

    return result 