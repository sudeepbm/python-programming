# Day-15                     Date: 30-06-2025

n=int(input("n: "))
n=89503
sum=0
final_sum=0
while n!=0:
    digit=n%10
    sum=sum+digit
    n=n//10
    if n==0 and sum>9:
        n=sum
        sum=0
print(sum)

# 
n=int(input("n: "))
sum=0
while n!=0:
    digit=n%10
    sum=sum+digit**2
    n=n//10
    if n==0:
        if sum==1:
            print("Happy")
        elif sum==4:
            print("Not Happy")
        else:
            n=sum
            sum=0