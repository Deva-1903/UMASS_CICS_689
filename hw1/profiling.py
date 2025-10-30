import numpy as np
import time

# Define sizes
Ns = [2, 5, 10, 20, 50, 100, 200, 500, 1000, 1500, 2000, 2500, 3000, 3500, 4000, 4500, 5000]

# Define operations
problems = [
    "x+x", "x^T x", "xx^T", "Ax", "AB",
    "inv(A)", "inv(A)@x", "inv(A)@B",
    "solve(A,x)", "solve(A,B)", "svd(A)"
]

# Initialize table
results = {p: [] for p in problems}

for N in Ns:
    # Create random data
    x = np.random.randn(N)
    A = np.random.randn(N, N)
    B = np.random.randn(N, N)

    for prob in problems:
        start = time.time()
        
        if prob == "x+x":
            _ = x + x
        elif prob == "x^T x":
            _ = x @ x
        elif prob == "xx^T":
            _ = np.outer(x, x)
        elif prob == "Ax":
            _ = A @ x
        elif prob == "AB":
            _ = A @ B
        elif prob == "inv(A)":
            _ = np.linalg.inv(A)
        elif prob == "inv(A)@x":
            _ = np.linalg.inv(A) @ x
        elif prob == "inv(A)@B":
            _ = np.linalg.inv(A) @ B
        elif prob == "solve(A,x)":
            _ = np.linalg.solve(A, x)
        elif prob == "solve(A,B)":
            _ = np.linalg.solve(A, B)
        elif prob == "svd(A)":
            _ = np.linalg.svd(A)
        
        end = time.time()
        results[prob].append(end - start)

# Print table
print("problem,", ",".join(f"N={N}" for N in Ns))
for prob in problems:
    print(prob + "," + ",".join(f"{t:.6f}" for t in results[prob]))
