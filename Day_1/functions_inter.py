#Change the value 10 in x to 15. Once you're done, x should now be [ [5,2,3], [15,8,9] ]
#x = [ [5,2,3], [10,8,9] ] 
#x[1][0]=15
#print(x)


#Change the last_name of the first student from 'Jordan' to 'Bryant'
# students = [
#     {'first_name':  'Michael', 'last_name' : 'Jordan'},
#     {'first_name' : 'John', 'last_name' : 'Rosales'}
# ]
# x = students[0]['last_name']
# x= 'Bryant'
# print(students)


#In the sports_directory, change 'Messi' to 'Andres'
# sports_directory = {
#     'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
#     'soccer' : ['Messi', 'Ronaldo', 'Rooney']
# }
# sports_directory['soccer'][0] = 'Andres'
# print(sports_directory)


#Change the value 20 in z to 30
# z = [ {'x': 10, 'y': 20} ]

# z[0]['y'] = 30
# print(z)

# students = [
#         {'first_name':  'Michael', 'last_name' : 'Jordan'},
#         {'first_name' : 'John', 'last_name' : 'Rosales'},
#         {'first_name' : 'Mark', 'last_name' : 'Guillen'},
#         {'first_name' : 'KB', 'last_name' : 'Tonel'}
#     ]

# for x in students:
#     print(x)

# def iterateDictionary2(key_name, students):
#     for d in some_list:
#         print(d[key_name])

#iterateDictionary(students) 
# should output: (it's okay if each key-value pair ends up on 2 separate lines;
# bonus to get them to appear exactly as below!)

dojo = {
'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}


def printInfo(dojo):
    for k, v in dojo.items():
        print(f"{len(v)} {k.upper()}")
        for i in v:
            print(i)
        print()


printInfo(dojo)

