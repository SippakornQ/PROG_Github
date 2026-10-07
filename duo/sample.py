import numpy as np
 
A = np.array([
    [2, 1, 1],
    [1, 2, 3],
    [3, 1, 2],
], dtype=float)
 
totals = np.array([50, 75, 65], dtype=float)
 
det = np.linalg.det(A)
print("Determinant:", round(det, 6))
 
prices = np.linalg.solve(A, totals)
print("Unit prices [pen, notebook, eraser]:", np.round(prices, 2))
 
print("Verification A @ prices == totals:", np.allclose(A @ prices, totals))
 
new_order = np.array([4, 2, 5], dtype=float)
print("New order cost:", round(float(np.sum(new_order * prices)), 2))
print("Condition number:", round(float(np.linalg.cond(A)), 2))
 
bad_A = np.array([
    [1, 2, 3],
    [2, 4, 6],
    [3, 1, 2],
], dtype=float)
try:
    np.linalg.solve(bad_A, totals)
except np.linalg.LinAlgError as err:
    print("Singular matrix caught:", err)