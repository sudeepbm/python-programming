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