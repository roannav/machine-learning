import numpy as np

a = np.array([3, 6, 9])  # Correct

print("Arithmetic operators apply ELEMENTWISE on arrays.")
print(f"a    \t{ a}")

print("\nThese will create a new array")
print(f"a / 3 \t{ a/3}")
print(f"a - 1 \t{ a - 1}")
print(f"a > 5 \t{ a > 5}")
print("a + np.ones(a.size)")
print( a + np.ones(a.size))

print(f"\na    \t{ a}")
print("\nThese will modify the original array")
a += 1
print(f"a += 1  a={a}")
a *= 2
print(f"a *= 1  a={a}")





A = np.array([[4, 5],
              [1, 0]])

B = np.array([[1, 0],
              [2, 3]])

print("\nA\n", A)
print("\nB\n", B)

print("\nelementwise product: A * B")
print(A * B)

print("Instead of elementwise product...")
print("\nmatrix product: A @ B")
print(A @ B)

print("\nmatrix product: A.dot(B)")
print(A.dot(B))

