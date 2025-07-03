# Day-18                     Date: 03-07-2025

# String Programming.

# WAP to check whether the given charecter is uppercase or not.
# without using built-in methods.
char=input("char: ")
if char>='A' and char<='Z':
    print("Uppercase Letter")
else:
    print("Not an Uppercase Letter")

# Using built-in methods.
n=input("n: ")
if ord(chr)>=65 and ord(n)<=90:
    print("Uppercase Letter")
else:
    print("Not an Uppercase Letter")

# WAP to check the given charecter is digit. If it is a digit, then print its ascii value. Else, print not a digit.
char=input("char: ")
if char>="0" and char<="9":
    print(ord(char))
else:
    print("Not a digit")

# WAP to check the given charecter is alphabet. If it is alphabet, then print last digit of the ascii value else, print "not an alphabet".
char=input("char: ")
if (char>="A" and char<="Z") or (char>="a" and char<="z"):
    print(ord(char)%10)
else:
    print("Not an alphabet")

# WAP to check whether the given charecter ascii value is even or odd.
char=input("char: ")
ascii=ord(char)
if ascii%2==0:
    print("ascii value is even")
else:
    print("ascii value is odd")

# WAP to check the given charecter is symbol or not. If it is, then print charecter for 3 times.
char=input("char: ")
if not(((char>="A" and char<="Z") or (char>="a" or char<="z") or (char>="0" and char<="9"))):
    print(char*3)
else:
    print("Not a symbol")

#  WAP to check the given char is alpha or digit. If it is then square the ascii value else print bye bye.
char=input("char: ")
if (char>="A" and char<="Z") or (char>="a" and char<="z") or (char>="0" and char<="9"):
    print(ord(char)**2)
else:
    print("bye bye")

# WAP to check the given charecter is vowel,
char=input("char: ")
# if char in ("A","E","I","O","U","a","e","i","o","u"):
if char in ("aeiouAEIOU"):
    print("vowel")
else:
    print("Not a vowel")

# WAP to check the given char is lowercase consonant or not.
char=input("char: ")
if char>="a" and char<="z" and char not in ("aeiou"):
    print("lowercase consonant")
else:
    print("Not a lowercase consonant")

# WAP to check whether the given charecter ascii value is odd and also charecter is uppercase. If it is, then print its next char. Else, print previous charecter.
char=input("char: ")
if char>="A" and char<="Z" and ord(char)%2!=0:
    print(chr(ord(char)+1))
else:
    print(chr(ord(char)-1))

# WAp to check the given charecter is uppercase or not, If it is uppercase,then convert it into lowercase.
char=input("char: ")
if char>="A" and char<="Z":
    print(chr(ord(char)+32))
else:
    print("Not Uppercase")