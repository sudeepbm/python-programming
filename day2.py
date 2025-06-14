# Swapping of 2 numbers

# a=int(input("a: "))
# b=int(input("b: "))
# c=int(input("c: "))
a=10
b=20
c=30
# logic 1
d=a
a=c
c=b
b=d
print(f"a: {a}\tb: {b}\tc: {c}")

a=10
b=20
c=30
# logic 2
a=a+b+c
b=a-b-c
c=a-b-c
a=a-b-c
print(f"a: {a}\tb: {b}\tc: {c}")

a=10
b=20
c=30
# logic 3
a=a*b*c
# b=a//b//c
# c=a//b//c
# a=a//b//c
b=a//(b*c)
c=a//(b*c)
a=a//(b*c)
print(f"a: {a}\tb: {b}\tc: {c}")

a=10
b=20
c=30
# logic 4
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

