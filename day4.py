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

