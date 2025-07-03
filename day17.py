# Day-17                     Date: 02-07-2025

# WAP to check the given number is a common divisor for 12,15 and 18.
n=int(input("n: "))
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
# # while start<=n1 and start<=n2:            # This can also be used
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