# Day-1                     Date: 13-06-2025

# a=int(input("a: "))
# b=int(input("b: "))
# logic 1
a=10
b=20
print(f"Before swap: \na:{a}\tb:{b}")
c=a
a=b
b=c
print(f"After swap: \na:{a}\tb:{b}")

# logic 2
a=10
b=20
print(f"Before swap: \na:{a}\tb:{b}")
a=a+b
b=a-b
a=a-b
print(f"After swap: \na:{a}\tb:{b}")

# logic 3
a=10
b=20
print(f"Before swap: \na:{a}\tb:{b}")
a=a*b
b=a//b
a=a//b
print(f"After swap: \na:{a}\tb:{b}")

# logic 4
a=10
b=20
print(f"Before swap: \na:{a}\tb:{b}")
a=a^b
b=a^b
a=a^b
print(f"After swap: \na:{a}\tb:{b}")

# logic 5
a=10
b=20
print(f"Before swap: \na:{a}\tb:{b}")
a,b=b,a
print(f"After swap: \na:{a}\tb:{b}")



# Day-2                     Date: 14-06-2025

# Swapping of 2 numbers

# a=int(input("a: "))
# b=int(input("b: "))
# c=int(input("c: "))
# logic 1
a=10
b=20
c=30
d=a
a=c
c=b
b=d
print(f"a: {a}\tb: {b}\tc: {c}")

# logic 2
a=10
b=20
c=30
a=a+b+c
b=a-b-c
c=a-b-c
a=a-b-c
print(f"a: {a}\tb: {b}\tc: {c}")

# logic 3
a=10
b=20
c=30
a=a*b*c
# b=a//b//c
# c=a//b//c
# a=a//b//c
b=a//(b*c)
c=a//(b*c)
a=a//(b*c)
print(f"a: {a}\tb: {b}\tc: {c}")

# logic 4
a=10
b=20
c=30
a=a^b^c
b=a^b^c
c=a^b^c
a=a^b^c
print(f"a: {a}\tb: {b}\tc: {c}")

# logic 5
a=10
b=20
c=30
a,b,c=c,a,b
print(f"a: {a}\tb: {b}\tc: {c}")

# checking if the number is even or odd



# Day-3                     Date: 16-06-2025

# Pattern Programming

print("*")


print("*")
print("*")


print("*")
print("*")
print("*")

for i in range(3):
    print("*")


n=int(input("n: "))
for i in range(n):
    print("*")



# Day-4                     Date: 17-06-2025

n=int(input("n: "))
for i in range(n):
    print("* *")

for i in range(3):
    for j in range(4):
        print("j", end=" ")

row=int(input("Enter number of rows: "))
col=int(input("Enter number of columns: "))
for i in range(row):
    for j in range(col):
        print("*", end=" ")
    print()  # Move to the next line after each row is printed


val=1
row=int(input("Enter number of rows: "))
col=int(input("Enter number of columns: "))
for i in range(row):
    for j in range(col):
        print(val, end=" ")
    print()
    val+=1  # Increment val after each row is printed


val=1
row=int(input("Enter number of rows: "))
col=int(input("Enter number of columns: "))
for i in range(row):
    for j in range(col):
        print(val, end=" ")
    print()
    val+=1
    if val>9:
        val=1


row=int(input("Enter number of rows: "))
col=int(input("Enter number of columns: "))
for i in range(row):
    val=1
    for j in range(col):
        print(val, end=" ")
        val+=1
    print()


row=int(input("Enter number of rows: "))
col=int(input("Enter number of columns: "))
val=row
if val>9:   # be careful about comparators
    val=9
for i in range(row):
    for j in range(col):
        print(val, end=" ")
    print()
    val-=1
    if val<1:
        val=9



# Day-5                     Date: 18-06-2025

row=int(input("Enter number of rows: "))
col=int(input("Enter number of columns: "))
for i in range(row):
    val=col
    for j in range(col):
        print(val, end=" ")
        val-=1
    print()  # Move to the next line after each row is printed



# Day-6                     Date: 19-06-2025




# Day-7                     Date: 20-06-2025

row=int(input("Enter number of rows: "))
col=int(input("Enter number of columns: "))
val=ord("A")
for i in range(row):
    for j in range(col):
        print(chr(val), end="")
    print()
    val+=1
    if val>ord("Z"):
        val=ord("A")

val=ord("Z")
for i in range(row):
    for j in range(col):
        print(chr(val), end=" ")
    print()
    val -= 1
    if val<ord("A"):
        val=ord("Z")


val=ord("A")
for i in range(row):
    val=ord("A")
    for j in range(col):
        print(chr(val), end="")
        val+=1
    print()



# Assignments:

# 1. Write a program to print the following pattern:
# o/p:-
# 1
# 2 2
# 3 3 3
# 4 4 4 4

# logic-1
n=4
for i in range(n):
    for j in range(n):
        if i>=j:
            print(i+1, end=" ")
        else:
            print(" ", end=" ")
    print()

# logic-2
n=4
s=1
for i in range(n):
    for j in range(n):
        if i>=j:
            print(s, end=" ")
        else:
            print(" ", end=" ")
    s+=1
    print()

# logic-3
n=4
for i in range(n+1):
    for j in range(1,n+1):
        if i>=j:
            print(i, end=" ")
        else:
            print(" ", end=" ")
    print()

# 2.
# Write a program to print the following pattern:
# o/p:-
# 1
# 1 2
# 1 2 3
# 1 2 3 4

# logic-1
n=int(input("n: "))
for i in range(n):
    for j in range(n):
        if i>=j:
            print(j+1,end=" ")
        else:
            print(" ", end=" ")
    print()

# logic-2 (correct it later)
n=int(input("n: "))
s=1
for i in range(n):
    for j in range(n):
        if i>=j:
            print(s, end=" ")
        else:
            print(" ",end=" ")
    s+=1
    print()

# logic-3
n=4
for i in range(n+1):
    for j in range(1,n+1):
        if i>=j:
            print(j, end=" ")
        else:
            print(" ", end=" ")
    print()

# 3. Write a program to print the following pattern:
# 4
# 3 3
# 2 2 2
# 1 1 1 1

n=4
val=n
for i in range(n):
    for j in range(n+1):
        if i>=j:
            print(val,end=" ")
        else:
            print(" ",end=" ")
    print()
    val-=1

# 4. Write a program to print the following pattern:
# 4
# 4 3
# 4 3 2
# 4 3 2 1

n=4
val=n
for i in range(n):
    for j in range(n):
        if i>=j:
            print(val, end=" ")
        else:
            print(" ", end=" ")
        val-=1
        if val<1:
            val=n
    print()

# 5. Write a program to print the following pattern:
# A
# B B
# C C C
# D D D D

n=4
val=ord("A")
for i in range(n):
    for j in range(n):
        if i>=j:
            print(chr(val),end=" ")
        else:
            print(" ",end=" ")
    val+=1
    print()

# 6. Write a program to print the following pattern:
# A
# A B
# A B C
# A B C D

n=4
val=ord("A")
for i in range(n):
    for j in range(n):
        if i>=j:
            print(chr(val), end=" ")
        else:
            print(" ", end=" ")
        val+=1
    val=ord("A")
    print()


# 7. Write a program to print the following pattern:
# D
# C C
# B B B
# A A A A

n=4
val=68
for i in range(n):
    for j in range(n):
        if i>=j:
            print(chr(val),end=" ")
        else:
            print(" ",end=" ")
    val-=1
    print()

# generalized program
n=int(input("n: "))
val=68
for i in range(n):
    for j in range(n):
        if i>=j:
            print(chr(val),end=" ")
        else:
            print(" ",end=" ")
    val-=1
    if val<65:
        val=68
    print()

# 8. Write a program to print the following pattern:
# D
# D C
# D C B
# D C B A

n=4
val=ord("D")
for i in range(n):
    for j in range(n):
        if i>=j:
            print(chr(val), end=" ")
        else:
            print(" ", end=" ")
        val-=1
    if val<ord("A"):
        val=ord("D")
    print()

# 9. Write a program to print the following pattern:
# 1 1 1 1
#   2 2 2
#     3 3
#       4

n=4
val=1
for i in range(n):
    for j in range(n):
        if i<=j:
            print(val,end=" ")
        else:
            print(" ",end=" ")
        if val>9:
            val=1
    val+=1
    print()

# 10. Write a program to print the following pattern:
# 1 2 3 4
#   1 2 3
#     1 2
#       1

n=4
val=1
for i in range(n):
    for j in range(n):
        if i<=j:
            print(val,end=" ")
            val+=1
        else:
            print(" ",end=" ")
    val=1
    print()

# 11. Write a program to print the following pattern:
# 4 4 4 4
#   3 3 3
#     2 2
#       1

n=4
val=4
for i in range(n):
    for j in range(n):
        if i<=j:
            print(val,end=" ")
        else:
            print(" ",end=" ")
    val-=1
    print()

# 12. Write a program to print the following pattern:
# 4 3 2 1
#   4 3 2
#     4 3
#       4

n=4
val=4
for i in range(n):
    for j in range(n):
        if i<=j:
            print(val,end=" ")
            val-=1
        else:
            print(" ",end=" ")
    print()
    val=4

# 13. Write a program to print the following pattern:
#  A A A A
#    B B B
#      C C
#        D

n=4
val=ord("A")
for i in range(n):
    for j in range(n):
        if i<=j:
            print(chr(val),end=" ")
        else:
            print(" ",end=" ")
    val+=1
    print()

# 14. Write a program to print the following pattern:
#  A B C D
#    A B C
#      A B
#        A

n=4
val=ord("A")
for i in range(n):
    for j in range(n):
        if i<=j:
            print(chr(val),end=" ")
            val+=1
        else:
            print(" ",end=" ")
    print()
    val=ord("A")

# 15. Write a program to print the following pattern:
# D D D D
#   C C C
#     B B
#       A

n=int(input("n: "))
val=ord("A")+n-1
for i in range(n):
    for j in range(n):
        if i<=j:
            print(chr(val),end=" ")
        else:
            print(" ",end=" ")
    val-=1
    print()

# 16. Write a program to print the following pattern:
# D C B A
#   D C B
#     D C
#       D

n=int(input("n: "))
val=ord("A")+n-1
for i in range(n):
    for j in range(n):
        if i<=j:
            print(chr(val),end=" ")
            val-=1
        else:
            print(" ",end=" ")
    print()
    val=ord("A")+n-1

# 17. Write a program to print the following pattern:
# 1
#   2
#     3
#       4

n=int(input("n: "))
val=1
for i in range(n):
    for j in range(n):
        if i==j:
            print(val,end=" ")
            val+=1
        else:
            print(" ",end=" ")
    print()

# 18. Write a program to print the following pattern:
# 4
#   3
#     2
#       1

n=int(input("n: "))
val=n
for i in range(n):
    for j in range(n):
        if i==j:
            print(val,end=" ")
            val-=1
        else:
            print(" ",end=" ")
    print()

# 19. Write a program to print the following pattern:
# A
#   B
#     C
#       D

n=int(input("n: "))
val=ord("A")
for i in range(n):
    for j in range(n):
        if i==j:
            print(chr(val),end=" ")
            val+=1
        else:
            print(" ",end=" ")
    print()

# 20. Write a program to print the following pattern:
# D
#   C
#     B
#       A

n=int(input("n: "))
val=ord("A")+n-1
for i in range(n):
    for j in range(n):
        if i==j:
            print(chr(val),end=" ")
            val-=1
        else:
            print(" ",end=" ")
    print()



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
    val-=1
    print()

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



# Day-9                     Date: 23-06-2025

# n: 4
# 1 1 1 1
# * * * *
# 2 2 2 2
# * * * *
# n: 9
# 1 1 1 1 1 1 1 1 1
# * * * * * * * * *
# 2 2 2 2 2 2 2 2 2
# * * * * * * * * *
# 3 3 3 3 3 3 3 3 3
# * * * * * * * * *
# 4 4 4 4 4 4 4 4 4
# * * * * * * * * *
# 5 5 5 5 5 5 5 5 5
n=int(input("n: "))
val=1
for i in range(n):
    for j in range(n):
        if i%2==0:
            print(val,end=" ")
        else:
            print("*",end=" ")
    print()
    if i%2==0:
        val+=1

# n: 8
# 1 * 2 * 3 * 4 *
# 5 * 6 * 7 * 8 *
# 9 * 1 * 2 * 3 *
# 4 * 5 * 6 * 7 *
# 8 * 9 * 1 * 2 *
# 3 * 4 * 5 * 6 *
# 7 * 8 * 9 * 1 *
# 2 * 3 * 4 * 5 *
# n: 4
# 1 * 2 *
# 3 * 4 *
# 5 * 6 *
# 7 * 8 *
n=int(input("n: "))
val=1
for i in range(n):
    for j in range(n):
        if j%2==0:
            print(val,end=" ")
            val+=1
            if val>9:
                val=1
        else:
            print("*",end=" ")
    print()
    
    if j%2==0:
        val+=1
# both of these also works
# n: 8
# 1 * 2 * 3 * 4 *
# 5 * 6 * 7 * 8 *
# 9 * 1 * 2 * 3 *
# 4 * 5 * 6 * 7 *
# 8 * 9 * 1 * 2 *
# 3 * 4 * 5 * 6 *
# 7 * 8 * 9 * 1 *
# 2 * 3 * 4 * 5 *
# n: 4
# 1 * 2 *
# 3 * 4 *
# 5 * 6 *
# 7 * 8 *
n=int(input("n: "))
p=True
val=1
for i in range(n):
    for j in range(n):
        if p:
            print(val,end=" ")
            p=False
            val+=1
            if val>9:
                val=1
        else:
            print("*",end=" ")
            p=True
    print()


# Pyramid Pattern

n=int(input("n: "))
str=1
spc=n-1
for i in range(n):
    for j in range(spc):
        print(" ",end=" ")
    for k in range(str):
        print("*",end=" ")
    print()
    spc-=1
    str+=2


n=int(input("n: "))
str=1
val=1
spc=n-1
for i in range(n):
    for j in range(spc):
        print(" ",end=" ")
    for k in range(str):
        print(val,end=" ")
    print()
    spc-=1
    str+=2
    val+=1

# without using star and space variables
n=int(input("n: "))
for i in range(n):
    for j in range(n-i-1):
        print(" ",end=" ")
    for k in range(2*i+1):
        print("*",end=" ")
    print()

n=int(input("n: "))
for i in range(n):
    for j in range(n):
        if i==0 or j==0 or i==n-1 or j==n-1:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()



# Day-10                     Date: 24-06-2025

# Number Programming.

# Example 1
n=123
print(n%10)
n=n//10
print(n%10)
n=n//10
print(n%10)
n=n//10
print(n%10)
n=n//10

# Example 2
n=81953
print(n%10)
n=n//10
print(n%10)
n=n//10
print(n%10)
n=n//10
print(n%10)
n=n//10
print(n%10)
n=n//10
print(n%10)



# Day-11                     Date: 25-06-2025

# WAP to print the odd digits from the given number.
n=abs(int(input("n: ")))
while n!=0:
    digit=n%10
    if digit%2!=0:
        print(digit)
    n=n//10

# WAP to print the digits which are present between 4 and 7 (inclusive) from the given number.
n=int(input("n: "))
while n!=0:
    digit=n%10
    if 4<=digit<=7:
        print(digit)
    n=n//10

# WAP to print the digits which are divisible by either 2 or 3.
n=int(input("n: "))
while n!=0:
    digit=n%10
    if (digit%2==0) or (digit%3==0):
        print(digit)
    n=n//10

# WAP to print the sum of the digits from the given number.
n=abs(int(input("n: ")))
sum=0
while n!=0:
    digit=n%10
    sum=sum+digit
    n=n//10
print(sum)

# WAP to print the sum of the even digits from the given number.
n=abs(int(input("n: ")))
sum=0
while n!=0:
    digit=n%10
    if digit%2==0:
        sum=sum+digit
    n=n//10
print(sum)

# WAP to print the product of the digits which are divisible by 4 from the given number.
n=abs(int(input("n: ")))
product=1
while n!=0:
    digit=n%10
    if digit%4==0:
        product=product*digit
    n=n//10
print(product)

# WAP to check the sum of the digits in a given number is equal to the product of the digits from the same number. If equal, print "SPY Number", else print "Not a SPY Number".
n=abs(int(input("n: ")))
sum=0
product=1
while n!=0:
    digit=n%10
    sum=sum+digit
    product=product*digit
    n=n//10
if sum==product:
    print("SPY Nmuber")
else:
    print("Not a SPY Number")

# WAP to check whether the sum of the digits from a given number is divisor for the same number or not. (Assignment)
n=abs(int(input("n: ")))
real_n=n
sum=0
while n!=0:
    digit=n%10
    sum=sum+digit
    n=n//10
if real_n%sum==0:
    print("divisor")
else:
    print("not a divisor")



# Day-12                     Date: 26-06-2025

# WAP to print the factorial of a given number.
n=int(input("n: "))
start=1
fact=1
while start<=n:
    fact=fact*start
    start=start+1
print(fact)

# WAP to print the series of numbers from 1 to n.
n=int(input("n: "))
start=1
while start<=n:
    print(start)
    start=start+1

# WAP to print odd numbers from 1 to n.
n=int(input("n: "))
start=1
while start<=n:
    if start%2!=0:
    # if start%2==1:
        print(start)
    start=start+1

# WAP to print sum of the numbers between n1 and n2.
n1=int(input("n1: "))
n2=int(input("n2: "))
sum=0
while n1<=n2:
    sum=sum+n1
    n1=n1+1
print(sum)

# WAP to print the product of the numbers from n1 to n2.
n1=int(input("n1: "))
n2=int(input("n2: "))
product=1
while n1<=n2:
    product=product*n1
    n1=n1+1
print(product)

# WAP to print the series of the numbers from 1 to digits from a given number.
n=abs(int(input("n: ")))
while n!=0:
    digit=n%10
    start=1
    while start<=digit:
        print(start)
        start=start+1
    n=n//10

# Assignments

# WAP to print the sum of the numbers from 1 to digit from a given number.
n=abs(int(input("n: ")))
while n!=0:
    digit=n%10
    start=1
    sum=0
    while start<=digit:
        sum=sum+start
        start=start+1
    print(sum)
    n=n//10

# WAP to print the product of the numbers from 1 to digit from a given number.
n=abs(int(input("n: ")))
while n!=0:
    digit=n%10
    start=1
    product=1
    while start<=digit:
        product=product*start
        start=start+1
    print(product)
    n=n//10



# Day-13                     Date: 27-06-2025

# WAP to print complete sum of the series from 1 to digit from a given number.
n=abs(int(input("n: ")))
total_sum=0
while n!=0:
    digit=n%10
    start=1
    sum=0
    while start<=digit:
        sum=sum+start
        start=start+1
    total_sum=total_sum+sum
    n=n//10
print(total_sum)

# WAP to print the sum of the factorial of each digit from a given number.
n=int(input("n: "))
sum=0
while n!=0:
    digit=n%10
    start=1
    fact=1
    while start<=digit:
        fact=fact*start
        start=start+1
    n=n//10
    sum=sum+fact
print(sum)

# WAP to check the given number is STRONG NUMBER or not.
n=int(input("n: "))
real_n=n
sum=0
while n!=0:
    digit=n%10
    start=1
    fact=1
    while start<=digit:
        fact=fact*start
        start=start+1
    n=n//10
    sum=sum+fact
if real_n==sum:
        print(f"{real_n} is a STRONG NUMBER")
else:
        print(f"{real_n} is not a STRONG NUMBER")

# WAP to print count of the digits present in agiven number.
n=int(input("n: "))
count=0
while n!=0:
    digit=n%10
    count=count+1
    n=n//10
print(count)

# WAP to print the power of each digit with count of digits from a given number.
n=int(input("n: "))
real_n=n
count=0
while n!=0:
    digit=n%10
    count+=1
    n=n//10
while real_n!=0:
    digit=real_n%10
    power=digit**count
    print(power)
    # print(digit**count)
    real_n=real_n//10

# WAP to check the sum of the power of each digit with its total number of digits from a given number is equal to the same number or not. If equal, print "ARMSTRONG NUMBER" else, print "Not an ARMSTRONG NUMBER".
n=int(input("n: "))
real_n=n
count=0
total_sum=0
while n!=0:
    digit=n%10
    count+=1
    n=n//10
n=real_n  # Reset n to original value
while n!=0:
    digit=n%10
    power=digit**count
    total_sum=total_sum+power
    n=n//10
if total_sum==real_n:
    print("ARMSTRONG NUMBER")
else:
    print("Not an ARMSTRONG NUMBER")



# Day-14                     Date: 28-06-2025

# WAP to add a digit to the end of a number
n=int(input("n: "))
digit=int(input("digit: "))
n=n*10+digit
print(n)

# WAP to reverse a given number.
n=int(input("n: "))
reversed_n=0
while n!=0:
    digit=n%10
    reversed_n=reversed_n*10+digit
    n=n//10
print(reversed_n)

# WAP to check whether a number is palindrome or not.
n=int(input("n: "))
real_n=n
reversed_n=0
while n!=0:
    digit=n%10
    reversed_n=reversed_n*10+digit
    n=n//10
if reversed_n==real_n:
    print("Palindrome")
else:
    print("Not a Palindrome")

# WAP to print the reverse of only odd digits from the given number.
input=189731
n=int(input("n: "))
# n=18793
reversed_n=0
while n!=0:
    digit=n%10
    if digit%2!=0:
        reversed_n=reversed_n*10+digit
    n=n//10
print(reversed_n)

# WAP to check squared digit sum is equal to the given number or not. If equal, print "NEON NUMBER" else, print "Not a NEON NUMBER".
n=int(input("n: "))
sum=0
squared_n=n**2
while squared_n!=0:
    digit=squared_n%10
    sum=sum+digit
    squared_n=squared_n//10
if sum==n:
    print("Neon Number")
else:
    print("Not a NEON Number")

# Assignment.

# WAP to reverse sum of the digits in a given number.
# n=int(input("n: "))
# sum=0
# while n!=0:
#     digit=n%10
#     n=n//10

# WAP to check the product of the digits in a given number is spy number or not.


# WAP to check the sum of odd digits in a given number is strong or not.


# WAP to check factorial of a given number is palindrome or not.


# WAP to print max digit and min digit number from a given number.

# Answers
#wap to print rev of sum of the digits of the given number
# n=int(input("n: "))
# sum=0
# rev=0
# while n>0:
#     digit=n%10
#     sum=digit+sum
#     n=n//10

# temp=sum
# while temp>0:
#     digit=temp%10
#     rev=rev*10+digit
#     temp=temp//10
# print(rev)

#wap to check the product of the digit in the given number is spy number or not 
# n=int(input("n: "))
# sum=0
# product=1
# n1=n
# while n1>0:
#     digit=n1%10
#     sum=digit+sum
#     product=product*digit
#     n1=n1//10
# if sum==product:
#     print("spy number")
# else:
#     print("not a spy number")

#wap to check sum of odd digits in a given number is strong or not
# n=int(input("n: "))
# sum=0
# while n>0:
#     digit=n%10
#     if digit%2!=0:
#         sum=digit+sum
#     n=n//10

# sum_fact=0
# temp=sum
# while temp>0:
#     digit=temp%10
#     fact=1
#     start=1
#     while start<=digit:
#         fact*=start
#         start+=1

#     sum_fact=sum_fact+fact
#     temp=temp//10

# if sum_fact==sum:
#     print("strong number")
# else:
#     print("Not a strong number")

#wap to check fact of given number is pallindrome

# n=int(input("n: "))
# n1=n
# start=1
# fact=1
# while start<=n:
#     fact=fact*start
#     start+=1

# temp=fact
# rev=0
# while temp>0:
#     digit=temp%10
#     rev=rev*10+digit
#     temp=temp//10

# if rev==fact:
#     print("pallindrome")
# else:
#     print("not a pallindrome")

#wap to print max and min digit from a given number
n=int(input("n: "))
max_digit=0
min_digit=9
while n>0:
    digit=n%10
    if digit>max_digit:
        max_digit=digit
    if digit<min_digit:
        min_digit=digit

    n=n//10
print("max number: ",max_digit)
print("min digit: ",min_digit)



# Day-15                     Date: 30-06-2025

n=int(input("n: "))
n=89503
sum=0
final_sum=0
while n!=0:
    digit=n%10
    sum=sum+digit
    n=n//10
    if n==0 and sum>9:
        n=sum
        sum=0
print(sum)

# 
n=int(input("n: "))
sum=0
while n!=0:
    digit=n%10
    sum=sum+digit**2
    n=n//10
    if n==0:
        if sum==1:
            print("Happy")
        elif sum==4:
            print("Not Happy")
        else:
            n=sum
            sum=0



# Day-16                     Date: 01-07-2025

# Series Programming

# WAP to print a series of numbers from 1 to 10.
start=1
end=10
while start<=end:
    print(start,end=" ")
    start+=1

# WAP to print numbers which are divisible by 5 from 21 to 31.
start=21
end=31
while start<=end:
    if start%5==0:
        print(start,end=" ")
    start+=1

# WAP to print the numbers which are divisible by both 3 and 5 from 1 to 15.
start=1
end=15
while start<=end:
    if start%3==0 and start %5==0:
        print(start,end=" ")
    start+=1

# WAP to print the divisors of 24 from 1 to 15.
n=24
start=1
end=15
while start<=end:
    if n%start==0:
        print(start,end=" ")
    start+=1

# WAP to print the divisors of a given number.
n=int(input("n: "))
start=1
end=n
while start<=end:
    if n%start==0:
        print(start,end=" ")
    start+=1

# WAP to count the total numbers which are divisible by 3 from 1 to 12.
start=1
end=12
count=0
while start<=end:
    if start%3==0:
        count+=1
    start+=1
print(count)

# WAP to print the count of the divisors of a given number.
n=abs(int(input("n: ")))
start=1
count=0
while start<=n:
    if n%start==0:
        count+=1
    start+=1
print(count)

# WAP to check count of the divisors of a given number is ewual to 2. If equal, print "Prime Number" else print "Not a Prime Number".
n=abs(int(input("n: ")))
start=1
count=0
while start<=n:
    if n%start==0:
        count+=1
    start+=1
if count==2:
    print("Prime Number")
else:
    print("Not a Prime Number")

# WAP to print the sum of the divisors of a given number.
n=abs(int(input("n: ")))
start=1
sum=0
while start<=n:
    if n%start==0:
        sum+=start
    start+=1
print(sum)

# WAP to check whether sum of the divisors of a given number is equal to the same number itself or not, If equal, print "Perfect Number" else print "Not a Perfect Number". (Note: Same number should not be a divisor)
n=abs(int(input("n: ")))
start=1
sum=0
while start!=n:
# while start<n:
    if n%start==0:
        sum+=start
    start+=1
if sum==n:
    print("Perfect Number")
else:
    print("Not a Perfect Number")

# Assignment.

# WAP to check sum of the digits in a given number is perfect number or not.
n=abs(int(input("n: ")))
i = 1
temp=n
digit_sum=0

while temp!=0:
    digit=temp%10
    digit_sum+=digit
    temp=temp//10

div_sum=0
while i<digit_sum:
    if digit_sum%i==0:
        div_sum+=i
    i+=1

if div_sum==digit_sum:
    print("Perfect Number")
else:
    print("Not a Perfect Number")

# WAP to print prime digits from a given number.
n=abs(int(input("n: ")))
temp=n
while temp!=0:
    digit=temp%10
    if digit==2 or digit==3 or digit==5 or digit==7:
        print(digit, end=" ")
    temp=temp//10

# WAP to check the sum of the series from n1 to n2 is strong number or not.
n1=abs(int(input("n1: ")))
n2=abs(int(input("n2: ")))
digit_sum=0
i = n1
while i <= n2:
    temp = i
    while temp != 0:
        digit = temp % 10
        fact = 1
        j = 1
        while j <= digit:
            fact *= j
            j += 1
        digit_sum += fact
        temp = temp // 10
    i += 1
if digit_sum==i:
    print("Strong Number")
else:
    print("Not a Strong Number")

# WAP to check the sum of the divisors of a given number is perfect ot not.
n=abs(int(input("n: ")))
start=1
sum_div=0
while start<n:
    if n%start==0:
        sum_div+=start
    start+=1
if sum_div==n:
    print("Perfect Number")
else:
    print("Not a Perfect Number")

# WAP to check whether the given number is prime or not, If it is prime then check whether it is armstrong or not. If it is not prime then check whether it is strong number or not.
n = abs(int(input("n: ")))

count = 0
for i in range(1, n + 1):
    if n % i == 0:
        count += 1
if count == 2:
    print("Prime Number")

    temp = n
    num_digits = len(str(n))
    arm_sum = 0
    while temp != 0:
        digit = temp % 10
        arm_sum += digit ** num_digits
        temp //= 10
    if arm_sum == n:
        print("Armstrong Number")
    else:
        print("Not an Armstrong Number")
else:
    print("Not a Prime Number")

    temp = n
    strong_sum = 0
    while temp != 0:
        digit = temp % 10
        fact = 1
        for i in range(1, digit + 1):
            fact *= i
        strong_sum += fact
        temp //= 10
    if strong_sum == n:
        print("Strong Number")
    else:
        print("Not a Strong Number")



# Day-17                     Date: 02-07-2025

# WAP to check the given number is a common divisor for 12,15 and 18.
n=int(input("n: "))
# if n%12==0 and n%15==0 and n%18==0:
if 12%n==0 and 15%n==0 and 18%n==0:
    print("Common Divisor")
else:
    print("Not a Common Divisor")

# WAP to print common divisors for 12 and 18 from 1 to 10.
start=1
end=10
while start<=end:
    if 12%start==0 and 18%start==0:
        print(start)
    start+=1

# WAP to print common divisors for the given 2 numbers.
n1=int(input("n1: "))
n2=int(input("n2: "))
start=1
end=n1
# while start<=n1 and start<=n2:            # This can also be used
while start<=end:
    if n1%start==0 and n2%start==0:
        print(start)
    start+=1

# WAP to print greatest common divisor for the given 2 numbers.
n1=int(input("n1: "))
n2=int(input("n2: "))
start=1
end=n1
gcd=0
# while start<=n1 and start<=n2:            # This can also be used
while start<=end:
    if n1%start==0 and n2%start==0:
        # if start>gcd:             # as the loop is continuing and the numbers are in increasing (start value) order, we can use the latest value of start as gcd.
        #     gcd=start
        gcd=start
    start+=1
print(gcd)

# WAP to check whether the given number is multiple of 5 or not.
n=int(input("n: "))
if n%5==0:
    print("multiple of 5")
else:
    print("Not a multiple of 5")

# WAP to check whether the given n is multiple for 2, 3 and 8 or not.
n=int(input("n: "))
if n%2==0 and n%3==0 and n%8==0:
    print("n is a multiple of 2,3 and 8")
else:
    print("n is not a multiple of 2,3 and 8")

# WAP to print the multiples of 3 from 1 to 10.
start=1
end=10
while start<=end:
    if start%3==0:
        print(start)
    start+=1

# WAP to print common multiples for the given 2 numbers from 1 to 20.
n1=int(input("n1: "))
n2=int(input("n2: "))
start=1
end=20
while start<=end:
    if start%n1==0 and start%n2==0:
        print(start)
    start+=1

# Assignment.

# LCM of given 2 numbers.
# logic 1
n1=int(input("n1: "))
n2=int(input("n2: "))
start=1
end=n1
gcd=0
# while start<=n1 and start<=n2:            # This can also be used
while start<=end:
    if n1%start==0 and n2%start==0:
        # if start>gcd:             # as the loop is continuing and the numbers are in increasing (start value) order, we can use the latest value of start as gcd.
        #     gcd=start
        gcd=start
    start+=1
lcm=(n1*n2)//gcd
print(lcm)

# logic 2
n1=int(input("n1: "))
n2=int(input("n2: "))
start=1
c=1
while c>0:
    if start%n1==0 and start%n2==0:
        print(start)
        c=0
    start+=1

# logic 3
n1=int(input("n1: "))
n2=int(input("n2: "))
start=1
while True:
    if start%n1==0 and start%n2==0:
        print(start)
        break
    start+=1