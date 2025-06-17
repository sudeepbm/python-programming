# Day-1                     Date: 13-06-2025

# a=int(input("a: "))
# b=int(input("b: "))
# logic 1
a=10
b=20
print(f"Before swap: \na:{a}\tb:{b}")
c=a
a=b
b=c
print(f"After swap: \na:{a}\tb:{b}")

# logic 2
a=10
b=20
print(f"Before swap: \na:{a}\tb:{b}")
a=a+b
b=a-b
a=a-b
print(f"After swap: \na:{a}\tb:{b}")

# logic 3
a=10
b=20
print(f"Before swap: \na:{a}\tb:{b}")
a=a*b
b=a//b
a=a//b
print(f"After swap: \na:{a}\tb:{b}")

# logic 4
a=10
b=20
print(f"Before swap: \na:{a}\tb:{b}")
a=a^b
b=a^b
a=a^b
print(f"After swap: \na:{a}\tb:{b}")

# logic 5
a=10
b=20
print(f"Before swap: \na:{a}\tb:{b}")
a,b=b,a
print(f"After swap: \na:{a}\tb:{b}")



# Day-2                     Date: 14-06-2025

# Swapping of 2 numbers

# a=int(input("a: "))
# b=int(input("b: "))
# c=int(input("c: "))
# logic 1
a=10
b=20
c=30
d=a
a=c
c=b
b=d
print(f"a: {a}\tb: {b}\tc: {c}")

# logic 2
a=10
b=20
c=30
a=a+b+c
b=a-b-c
c=a-b-c
a=a-b-c
print(f"a: {a}\tb: {b}\tc: {c}")

# logic 3
a=10
b=20
c=30
a=a*b*c
# b=a//b//c
# c=a//b//c
# a=a//b//c
b=a//(b*c)
c=a//(b*c)
a=a//(b*c)
print(f"a: {a}\tb: {b}\tc: {c}")

# logic 4
a=10
b=20
c=30
a=a^b^c
b=a^b^c
c=a^b^c
a=a^b^c
print(f"a: {a}\tb: {b}\tc: {c}")

# logic 5
a=10
b=20
c=30
a,b,c=c,a,b
print(f"a: {a}\tb: {b}\tc: {c}")

# checking if the number is even or odd



# Day-3                     Date: 16-06-2025

# Pattern Programming

print("*")


print("*")
print("*")


print("*")
print("*")
print("*")

for i in range(3):
    print("*")


n=int(input("n: "))
for i in range(n):
    print("*")
