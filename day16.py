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