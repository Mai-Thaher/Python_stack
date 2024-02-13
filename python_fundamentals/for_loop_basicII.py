# 1.Biggie Size
def biggie_size(list):
    for i in range(len(list)):
        if list[i]>0:
            list[i]="Big"
    return list
x=biggie_size([-1, 3, 5, -5])
print(x)

# 2.Count Positives
def count_positive(list):
    count=0
    for i in range(len(list)):
        if list[i]>0:
            count+=1
        list[len(list)-1]=count
    return list
x=count_positive([-1,1,1,3] )
print(x)
y=count_positive([1,6,-4,-2,7,2])
print(y)

# 3.Sum Total
def sum_total(list):
    sum=0
    for i in range(len(list)):
        sum+=list[i]
    return sum
x= sum_total([1,2,3,4])
print(x)

# 4.Average 
def average(list):
    sum=0
    for i in range(len(list)):
        sum+=list[i]
    avg=sum/len(list)
    return avg
print(average([1,2,3,4]))

# 5.Length 
def length(list):
    for i in range(len(list)):
        if len(list)==0:
            print(0)
    return len(list)
print(length([1,4,5,8]))
print(length([]))

# 6. Minimum
def minimum(list):
    if len(list)==0:
        return False
    min = list[0]
    for i in range(len(list)):
        if list[i]<min:
            min=list[i]
    return min
print(minimum([5,-8,2,1]))
print(minimum([]))

#7 Maximum
def maximum(list):
    if len(list)==0:
        return False
    max = list[0]
    for i in range(len(list)):
        if list[i]>max:
            max=list[i]
    return max
print(maximum([5,-8,2,1]))
print(maximum([]))

#8. Ultimate Analysis
def ultimate_analysis(list):
    result={'sum_total':0, 'average':0, 'minimum':0, 'maximum':0, 'length':len(list) }
    sum=0
    min = list[0]
    max = list[0]
    for i in range(len(list)):
        sum+=list[i]
        result['sum_total']=sum
        avg=sum/len(list)
        result['average']=avg
        if list[i]<min:
            min=list[i]
        result['minimum']=min
        if list[i]>max:
            max=list[i]
        result['maximum']=max
    return result
    
print(ultimate_analysis([37,2,1,-9]))

# 9. Reverse List
def reverse_list(list):
    start_index=0
    end_index=len(list)-1
    while start_index<end_index:
        list[start_index],list[end_index]=list[end_index], list[start_index]
        start_index+=1
        end_index-=1
    return list
print(reverse_list([37,2,1,-9]))
