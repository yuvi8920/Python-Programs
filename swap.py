# swapping of 2 variables
# 1st
a = 10
b = 5
print("Before swapping: ")
print(a)
print(b)

temp = a
a = b
b = temp
print("After swapping: ")
print(a)
print(b)


# 2nd
c = 15
d = 7
print("Before swapping: ")
print(c)
print(d)

c = c + d
d = c - d
c = c - d
print("After swapping: ")
print(c)
print(d)


# swapping of 3 variables
# 1st
a = 10
b = 15
c = 20
print("Before swapping: ")
print(a)
print(b)
print(c)

temp = a
a = c
c = b
b = temp
print("After swapping: ")
print(a)
print(b)
print(c)


# 4th
a = 11
b = 14
c = 21
print("Before swapping: ")
print(a)
print(b)
print(c)

a = a + b
b = a - b
a = a - b
a = a + c
c = a - c
a = a - c
print("After swapping: ")
print(a)
print(b)
print(c)

print("This program is written and executed by Yuvraj Narang")