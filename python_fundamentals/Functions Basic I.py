#1
def a():
    return 5
print(a())
# output: 5

#2
def a():
    return 5
print(a()+a())
# output: 10

#3
def a():
    return 5
    return 10
print(a())
#output: 5

#4
def a():
    return 5
    print(10)
print(a())
# output: 5

#5
def a():
    print(5)
x = a()
print(x)
# output: 5

#6
def a(b,c):
    print(b+c)
print(a(1,2) + a(2,3))
# output: 8

#7
def a(b,c):
    return str(b)+str(c)
print(a(2,5))
#output: 25

#8
def a():
    b = 100
    print(b)
    if b < 10:
        return 5
    else:
        return 10
    return 7

print(a())
#output: 10

#9
def a(b,c):
    if b<c:
        return 7
    else:
        return 14
    return 3
print(a(2,3))
print(a(5,3))
print(a(2,3) + a(5,3))
# output: 7, 14, 21







