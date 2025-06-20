# Day-6                     Date: 19-06-2025

# row=int(input("Enter number of rows: "))
# col=int(input("Enter number of columns: "))

n = 5  # Size of the pattern (must be odd for symmetry)

for i in range(n):
    for j in range(n):
        if i == j or i + j == n - 1:
            print("*", end="")
        else:
            print(" ", end="")
    print()
