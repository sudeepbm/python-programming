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
