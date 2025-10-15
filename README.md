# Square root of matrix

## Overview

This codebase containes the code used in the OMR project "square root of matrix" 2025.

## Dependencies

This project relies on several Python libraries for data handling and visualization. Make sure the following packages are installed:

- `numpy`
- `scipy`
- `matplotlib`

## File Descriptions

- **`benchmark.py`**: records time and relative error of a given method and matrix.
- **`circle_test_commuting.py`**: calculates stability condition commutating method and draws cricles visualizing the condition.
- **`convergence_plot.py`**: draws a convergence plot of relative error against number of iterations for multiple matrices (only works for Iannazoo method).
- **`example_matrices.py`**: initialization of matrices used.
- **`main.py`**: script to run to obtain all numerical results and the convergence plot (does not include circle plot).
- **`numerical_methods.py`**: initialization of methods used.
