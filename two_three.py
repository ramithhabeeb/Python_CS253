import numpy as np
def solve_linear_system(A, B):
    try:
        x = np.linalg.solve(A, B)
        return x
    except np.linalg.LinAlgError as e:
        # Handle cases where the matrix is singular or not square
        print(f"Error: {e}")
        return None
    
