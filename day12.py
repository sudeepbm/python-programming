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

#WAP to print odd numbers from 1 to n.
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