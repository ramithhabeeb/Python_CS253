"""
Task 2.3

This program provides a function to solve a system of linear equations using NumPy.
Functions:
    solve_linear_system(A, B):
        Solves the linear system Ax = B, where A is the coefficient matrix and B is the constant matrix/vector.
        Handles cases where the matrix is singular or not square.
        Parameters:
            A (numpy.ndarray): A 2D array representing the coefficient matrix.
            B (numpy.ndarray): A 1D or 2D array representing the constant matrix/vector.
        Returns:
            numpy.ndarray or None: The solution vector/matrix if the system is solvable, or None if the matrix is singular or not square.
        Raises:
            np.linalg.LinAlgError: If the matrix A is singular or not square.
"""

import numpy as np
def solve_linear_system(A, B):
    try:
        x = np.linalg.solve(A, B)
        return x
    except np.linalg.LinAlgError as e:
        # Handle cases where the matrix is singular or not square
        print(f"Error: {e}")
        return None
    
