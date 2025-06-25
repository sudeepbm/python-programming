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