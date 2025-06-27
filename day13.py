# Day-13                     Date: 27-06-2025

# WAP to print complete sum of the series from 1 to digit from a given number.
n=abs(int(input("n: ")))
total_sum=0
while n!=0:
    digit=n%10
    start=1
    sum=0
    while start<=digit:
        sum=sum+start
        start=start+1
    total_sum=total_sum+sum
    n=n//10
print(total_sum)

# WAP to print the sum of the factorial of each digit from a given number.
n=int(input("n: "))
sum=0
while n!=0:
    digit=n%10
    start=1
    fact=1
    while start<=digit:
        fact=fact*start
        start=start+1
    n=n//10
    sum=sum+fact
print(sum)

# WAP to check the given number is STRONG NUMBER or not.
n=int(input("n: "))
real_n=n
sum=0
while n!=0:
    digit=n%10
    start=1
    fact=1
    while start<=digit:
        fact=fact*start
        start=start+1
    n=n//10
    sum=sum+fact
if real_n==sum:
        print(f"{real_n} is a STRONG NUMBER")
else:
        print(f"{real_n} is not a STRONG NUMBER")

# WAP to print count of the digits present in agiven number.
n=int(input("n: "))
count=0
while n!=0:
    digit=n%10
    count=count+1
    n=n//10
print(count)

# WAP to print the power of each digit with count of digits from a given number.
n=int(input("n: "))
real_n=n
count=0
while n!=0:
    digit=n%10
    count+=1
    n=n//10
while real_n!=0:
    digit=real_n%10
    power=digit**count
    print(power)
    # print(digit**count)
    real_n=real_n//10

# WAP to check the sum of the power of each digit with its total number of digits from a given number is equal to the same number or not. If equal, print "ARMSTRONG NUMBER" else, print "Not an ARMSTRONG NUMBER".
n=int(input("n: "))
real_n=n
count=0
total_sum=0
while n!=0:
    digit=n%10
    count+=1
    n=n//10
n=real_n  # Reset n to original value
while n!=0:
    digit=n%10
    power=digit**count
    total_sum=total_sum+power
    n=n//10
if total_sum==real_n:
    print("ARMSTRONG NUMBER")
else:
    print("Not an ARMSTRONG NUMBER")