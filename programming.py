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
