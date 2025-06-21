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