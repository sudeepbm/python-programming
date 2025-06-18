# Day-5                     Date: 18-06-2025

row=int(input("Enter number of rows: "))
col=int(input("Enter number of columns: "))
for i in range(row):
    val=col
    for j in range(col):
        print(val, end=" ")
        val-=1
    print()  # Move to the next line after each row is printed
