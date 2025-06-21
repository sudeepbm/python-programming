# Day-7                     Date: 20-06-2025

# row=int(input("Enter number of rows: "))
# col=int(input("Enter number of columns: "))
# val=ord("A")
# for i in range(row):
#     for j in range(col):
#         print(chr(val), end="")
#     print()
#     val+=1
#     if val>ord("Z"):
#         val=ord("A")

# val=ord("Z")
# for i in range(row):
#     for j in range(col):
#         print(chr(val), end=" ")
#     print()
#     val -= 1
#     if val<ord("A"):
#         val=ord("Z")


# val=ord("A")
# for i in range(row):
#     val=ord("A")
#     for j in range(col):
#         print(chr(val), end="")
#         val+=1
#     print()



# Assignments:

# 1. Write a program to print the following pattern:
# o/p:-
# 1
# 2 2
# 3 3 3
# 4 4 4 4

# logic-1
# n=4
# for i in range(n):
#     for j in range(n):
#         if i>=j:
#             print(i+1, end=" ")
#         else:
#             print(" ", end=" ")
#     print()

# logic-2
# n=4
# s=1
# for i in range(n):
#     for j in range(n):
#         if i>=j:
#             print(s, end=" ")
#         else:
#             print(" ", end=" ")
#     s+=1
#     print()

# logic-3
# n=4
# for i in range(n+1):
#     for j in range(1,n+1):
#         if i>=j:
#             print(i, end=" ")
#         else:
#             print(" ", end=" ")
#     print()

# 2.
# Write a program to print the following pattern:
# o/p:-
# 1
# 1 2
# 1 2 3
# 1 2 3 4

# logic-1
# n=int(input("n: "))
# for i in range(n):
#     for j in range(n):
#         if i>=j:
#             print(j+1,end=" ")
#         else:
#             print(" ", end=" ")
#     print()

# logic-2 (correct it later)
# n=int(input("n: "))
# s=1
# for i in range(n):
#     for j in range(n):
#         if i>=j:
#             print(s, end=" ")
#         else:
#             print(" ",end=" ")
#     s+=1
#     print()

# logic-3
# n=4
# for i in range(n+1):
#     for j in range(1,n+1):
#         if i>=j:
#             print(j, end=" ")
#         else:
#             print(" ", end=" ")
#     print()

# 3. Write a program to print the following pattern:
# 4
# 3 3
# 2 2 2
# 1 1 1 1

# n=4
# val=n
# for i in range(n):
#     for j in range(n+1):
#         if i>=j:
#             print(val,end=" ")
#         else:
#             print(" ",end=" ")
#     print()
#     val-=1

# 4. Write a program to print the following pattern:
# 4
# 4 3
# 4 3 2
# 4 3 2 1

# n=4
# val=n
# for i in range(n):
#     for j in range(n):
#         if i>=j:
#             print(val, end=" ")
#         else:
#             print(" ", end=" ")
#         val-=1
#         if val<1:
#             val=n
#     print()

# 5. Write a program to print the following pattern:
# A
# B B
# C C C
# D D D D

# n=4
# val=ord("A")
# for i in range(n):
#     for j in range(n):
#         if i>=j:
#             print(chr(val),end=" ")
#         else:
#             print(" ",end=" ")
#     val+=1
#     print()

# 6. Write a program to print the following pattern:
# A
# A B
# A B C
# A B C D

# n=4
# val=ord("A")
# for i in range(n):
#     for j in range(n):
#         if i>=j:
#             print(chr(val), end=" ")
#         else:
#             print(" ", end=" ")
#         val+=1
#     val=ord("A")
#     print()


# 7. Write a program to print the following pattern:
# D
# C C
# B B B
# A A A A

# n=4
# val=68
# for i in range(n):
#     for j in range(n):
#         if i>=j:
#             print(chr(val),end=" ")
#         else:
#             print(" ",end=" ")
#     val-=1
#     print()

# generalized program
# n=int(input("n: "))
# val=68
# for i in range(n):
#     for j in range(n):
#         if i>=j:
#             print(chr(val),end=" ")
#         else:
#             print(" ",end=" ")
#     val-=1
#     if val<65:
#         val=68
#     print()

# 8. Write a program to print the following pattern:
# D
# D C
# D C B
# D C B A

# n=4
# val=ord("D")
# for i in range(n):
#     for j in range(n):
#         if i>=j:
#             print(chr(val), end=" ")
#         else:
#             print(" ", end=" ")
#         val-=1
#     if val<ord("A"):
#         val=ord("D")
#     print()

# 9. Write a program to print the following pattern:
# 1 1 1 1
#   2 2 2
#     3 3
#       4

# n=4
# val=1
# for i in range(n):
#     for j in range(n):
#         if i<=j:
#             print(val,end=" ")
#         else:
#             print(" ",end=" ")
#         if val>9:
#             val=1
#     val+=1
#     print()

# 10. Write a program to print the following pattern:
# 1 2 3 4
#   1 2 3
#     1 2
#       1

# n=4
# val=1
# for i in range(n):
#     for j in range(n):
#         if i<=j:
#             print(val,end=" ")
#             val+=1
#         else:
#             print(" ",end=" ")
#     val=1
#     print()

# 11. Write a program to print the following pattern:
# 4 4 4 4
#   3 3 3
#     2 2
#       1

# n=4
# val=4
# for i in range(n):
#     for j in range(n):
#         if i<=j:
#             print(val,end=" ")
#         else:
#             print(" ",end=" ")
#     val-=1
#     print()

# 12. Write a program to print the following pattern:
# 4 3 2 1
#   4 3 2
#     4 3
#       4

# n=4
# val=4
# for i in range(n):
#     for j in range(n):
#         if i<=j:
#             print(val,end=" ")
#             val-=1
#         else:
#             print(" ",end=" ")
#     print()
#     val=4

# 13. Write a program to print the following pattern:
#  A A A A
#    B B B
#      C C
#        D

# n=4
# val=ord("A")
# for i in range(n):
#     for j in range(n):
#         if i<=j:
#             print(chr(val),end=" ")
#         else:
#             print(" ",end=" ")
#     val+=1
#     print()

# 14. Write a program to print the following pattern:
#  A B C D
#    A B C
#      A B
#        A

# n=4
# val=ord("A")
# for i in range(n):
#     for j in range(n):
#         if i<=j:
#             print(chr(val),end=" ")
#             val+=1
#         else:
#             print(" ",end=" ")
#     print()
#     val=ord("A")

# 15. Write a program to print the following pattern:
# D D D D
#   C C C
#     B B
#       A

# n=int(input("n: "))
# val=ord("A")+n-1
# for i in range(n):
#     for j in range(n):
#         if i<=j:
#             print(chr(val),end=" ")
#         else:
#             print(" ",end=" ")
#     val-=1
#     print()

# 16. Write a program to print the following pattern:
# D C B A
#   D C B
#     D C
#       D

# n=int(input("n: "))
# val=ord("A")+n-1
# for i in range(n):
#     for j in range(n):
#         if i<=j:
#             print(chr(val),end=" ")
#             val-=1
#         else:
#             print(" ",end=" ")
#     print()
#     val=ord("A")+n-1




























##################     val=ord("A")+n-1     ###################