# Day-8                     Date: 21-06-2025

n=int(input("n: "))
for i in range(n):
    for j in range(n):
        if (i+j)>=n-1:
        # if (i+j)>n:           #both works
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()

n=int(input("n: "))
for i in range(n):
    for j in range(n):
        if (i+j)<=n-1:
        # if (i+j)<n:           #both works
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()

n=int(input("n: "))
for i in range(n):
    for j in range(n):
        if (i+j)==n-1:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()

n=int(input("n: "))
for i in range(1,n+1):
    print("* "*i)

n=int(input("n: "))
val=1
for i in range(1,n+1):
    print((str(val)+" ")*i)
    val+=1
    if val>9:
        val=1

n=int(input("n: "))
val=ord("A")
for i in range(1,n+1):
    print((chr(val)+" ")*i)
    val+=1
    if val>ord("Z"):
        val=ord("A")

n=int(input("n: "))
val=ord("A")+n-1
for i in range(1,n+1):
    print((chr(val)+" ")*i)
    val-=1

n=int(input("n: "))
val=ord("A")
for i in range(1,n+1):
    print("  "*(n-i)+"* "*i)

n=int(input("n: "))
for i in range(n,0,-1):
    print("* "*i)



# Assignments

# 1. Write a program to print the following pattern:
#       1
#     2 2
#   3 3 3

n=int(input("n: "))
val=1
for i in range(n):
    for j in range(n):
        if (i+j)>=n-1:
            print(val,end=" ")
        else:
            print(" ",end=" ")
    print()
    val+=1

# 2. Write a program to print the following pattern:
#       1
#     1 2
#   1 2 3

n=int(input("n: "))
val=1
for i in range(n):
    for j in range(n):
        if (i+j)>=n-1:
            print(val,end=" ")
            val+=1
        else:
            print(" ",end=" ")
    print()
    val=1

# 3. Write a program to print the following pattern:
#       3
#     2 2
#   1 1 1

n=int(input("n: "))
val=n
for i in range(n):
    for j in range(n):
        if (i+j)>=n-1:
            print(val,end=" ")
        else:
            print(" ",end=" ")
    print()
    val-=1

# 4. Write a program to print the following pattern:
#       3
#     3 2
#   3 2 1

n=int(input("n: "))
val=n
for i in range(n):
    for j in range(n):
        if (i+j)>=n-1:
            print(val,end=" ")
            val-=1
        else:
            print(" ",end=" ")
    print()
    val=n

# 5. Write a program to print the following pattern:
#       A
#     B B
#   C C C

n=int(input("n: "))
val=ord("A")
for i in range(n):
    for j in range(n):
        if (i+j)>=n-1:
            print(chr(val),end=" ")
        else:
            print(" ",end=" ")
    val+=1
    print()

# 6. Write a program to print the following pattern:
#       A
#     A B
#   A B C

n=int(input("n: "))
val=ord("A")
for i in range(n):
    for j in range(n):
        if (i+j)>=n-1:
            print(chr(val),end=" ")
            val+=1
        else:
            print(" ",end=" ")
    print()
    val=ord("A")

# 7. Write a program to print the following pattern:
#       C
#     B B
#   A A A

n=int(input("n: "))
val=ord("A")+n-1
for i in range(n):
    for j in range(n):
        if (i+j)>=n-1:
            print(chr(val),end=" ")
        else:
            print(" ",end=" ")
    val-=1
    print()

# 8. Write a program to print the following pattern:
#       C
#     C B
#   C B A

n=int(input("n: "))
val=ord("A")+n-1
for i in range(n):
    for j in range(n):
        if (i+j)>=n-1:
            print(chr(val),end=" ")
            val-=1
        else:
            print(" ",end=" ")
    print()
    val=ord("A")+n-1

# 9. Write a program to print the following pattern:
#       Z
#     Y Y
#   X X X

n=int(input("n: "))
val=ord("Z")
for i in range(n):
    for j in range(n):
        if (i+j)>=n-1:
            print(chr(val),end=" ")
        else:
            print(" ",end=" ")
    val-=1
    print()

# 10. Write a program to print the following pattern:
# 1 1 1
# 2 2
# 3

n=int(input("n: "))
val=1
for i in range(n):
    for j in range(n):
        if (i+j)<=n-1:
            print(val,end=" ")
        else:
            print(" ",end=" ")
    val+=1
    print()

# 11. Write a program to print the following pattern:
# 1 2 3
# 1 2
# 1

n=int(input("n: "))
val=1
for i in range(n):
    for j in range(n):
        if (i+j)<=n-1:
            print(val,end=" ")
        else:
            print(" ",end=" ")
        val+=1
    print()
    val=1

# 12. Write a program to print the following pattern:
# 1 2 3
# 4 5
# 6

n=int(input("n: "))
val=1
for i in range(n):
    for j in range(n):
        if (i+j)<=n-1:
            print(val,end=" ")
            val+=1
        else:
            print(" ",end=" ")
    print()

# 13. Write a program to print the following pattern:
# A B C
# A B
# A

n=int(input("n: "))
val=ord("A")
for i in range(n):
    for j in range(n):
        if (i+j)<=n-1:
            print(chr(val),end=" ")
        else:
            print(" ",end=" ")
        val+=1
    print()
    val=ord("A")

# 14. Write a program to print the following pattern:
# A A A
# B B
# C

n=int(input("n: "))
val=ord("A")
for i in range(n):
    for j in range(n):
        if (i+j)<=n-1:
            print(chr(val),end=" ")
        else:
            print(" ",end=" ")
    val+=1
    print()

# 15. Write a program to print the following pattern:
# 3 2 1
# 3 2
# 3

n=int(input("n: "))
val=n
for i in range(n):
    for j in range(n):
        if (i+j)<=n-1:
            print(val,end=" ")
        else:
            print(" ",end=" ")
        val-=1
    print()
    val=n

# 16. Write a program to print the following pattern:
# C B A
# C B
# C

n=int(input("n: "))
val=ord("A")+n-1
for i in range(n):
    for j in range(n):
        if (i+j)<=n-1:
            print(chr(val),end=" ")
        else:
            print(" ",end=" ")
        val-=1
    print()
    val=ord("A")+n-1

# 17. Write a program to print the following pattern:
# Z Y X
# Z Y
# Z

n=int(input("n: "))
val=ord("Z")
for i in range(n):
    for j in range(n):
        if (i+j)<=n-1:
            print(chr(val),end=" ")
        else:
            print(" ",end=" ")
        val-=1
    print()
    val=ord("Z")

# 18. Write a program to print the following pattern:
# Z Z Z
# Y Y
# X

n=int(input("n: "))
val=ord("Z")
for i in range(n):
    for j in range(n):
        if (i+j)<=n-1:
            print(chr(val),end=" ")
        else:
            print(" ",end=" ")
    val-=1
    print()

# 19. Write a program to print the following pattern:
#       1
#     2
#   3
# 4

n=int(input("n: "))
val=1
for i in range(n):
    for j in range(n):
        if (i+j)==n-1:
            print(val,end=" ")
            val+=1
        else:
            print(" ",end=" ")
    print()

# 20. Write a program to print the following pattern:
#       D
#     C
#   B
# A

n=int(input("n: "))
val=ord("A")+n-1
for i in range(n):
    for j in range(n):
        if (i+j)==n-1:
            print(chr(val),end=" ")
            val-=1
        else:
            print(" ",end=" ")
    print()