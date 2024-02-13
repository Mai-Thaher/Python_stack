#Q: Update Values in Dictionaries and Lists
x = [ [5,2,3], [10,8,9] ] 
students = [
    {'first_name':  'Michael', 'last_name' : 'Jordan'},
    {'first_name' : 'John', 'last_name' : 'Rosales'}
]
sports_directory = {
    'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
    'soccer' : ['Messi', 'Ronaldo', 'Rooney']
}
z = [ {'x': 10, 'y': 20} ]

# 1.Change the value 10 in x to 15. Once you're done, x should now be [ [5,2,3], [15,8,9] ].
x[1][0]=15
print(x)

# 2.Change the last_name of the first student from 'Jordan' to 'Bryant'
#students[0]['last_name']='Bryant'
#print(students)

# 3.In the sports_directory, change 'Messi' to 'Andres'
sports_directory['soccer'][0]='Andres'
print(sports_directory)

# 4.Change the value 20 in z to 30
z[0]['y']=30
print(z)

#Q: Iterate Through a List of Dictionaries
students = [
    {'first_name':  'Michael', 'last_name' : 'Jordan'},
    {'first_name': 'John', 'last_name' : 'Rosales'},
    {'first_name': 'Mark', 'last_name': 'Guillen'},
    {'first_name': 'KB', 'last_name':'Tonel'},
    ]
def iterateDictionary(list): 
    for i in range(len(list)):
        print('first_name -',list[i]['first_name'],',', 'last_name -',list[i]['last_name'])
print(iterateDictionary(students))

#Q: Get Values From a List of Dictionaries
def iterateDictionary2(key_name, some_list):
    for i in range(len(some_list)):
        print(some_list[i][key_name])
print(iterateDictionary2('first_name', students)) #why it printes none after the last item
print(iterateDictionary2('last_name', students))

#Q: Iterate Through a Dictionary with List Values
dojo = {
'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}
def printInfo(some_dict):
    for x, y in some_dict.items():# it will print y as a list!
        len_key=str(len(y) )+' '+x
        print(len_key)
        for i in range(len(y)):# I included a loop to print y items (not as a list)
            print (y[i])
        
    
printInfo(dojo)


