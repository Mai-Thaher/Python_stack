# 1. Countdown
def Countdown(num):
    countdown_list=[]
    for i in range(num, -1, -1):
        countdown_list.append(i)
    return countdown_list
result=Countdown(8)
print(result)

#2. Print and Return
def print_and_return(alist):
    for i in range(len(alist)):
        print(alist[0])
        return alist[1]
x= print_and_return([1,2])
print(x)

#3. First Plus Length
def first__plus_length(alist):
    for i in range(len(alist)):
        sum=alist[0]+alist[len(alist)-1]
    return sum
y= first__plus_length([1,2,3,4,5])
print(y)

#4. Values Greater than Second 
def values_greater_than_second(alist):
    new_list=[]
    for i in range(len(alist)):
        if len(alist)<2 :
            return False
        elif alist[i]>alist[1] :
            new_list.append(alist[i])
    print(len(new_list))
    return new_list
z=values_greater_than_second([3,4,5,2,8,7])
print(z)
x=values_greater_than_second([3])
print(x)

#5 This Length, That Value
def length_and_value(size,value):
    return[value]*size
print(length_and_value(4,7))




