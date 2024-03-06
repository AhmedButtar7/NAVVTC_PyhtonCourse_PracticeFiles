dic = {'A': 'Apple', 'B': 'Ball', 'c': 'cat', 'd': 'dog', 'e': 'elephant',
       'f ': 'frog', 'g': 'gel', 'h': 'head', 'i': 'impala', 'j': 'jug'}

# print all keys and value in dictionary
print(dic.keys(), dic.values())

# access one element of the list using its key
print(dic['A'])

# access the dictionary with get method
print(dic.get('B'))

# Modify the dictionary elements
dic.update({'A': 'Analog'})
print(dic.get('A'))
print(dic.get('B'))

# Print length of the dictionary
print(len(dic))

# Use for loop to print items in list
for keys, values in dic.items():
    print(keys, values)

# pop or delete an item in the dictionary
dic.pop('A')
print(dic)

# Print type of the dictionary
print(type(dic))

# Nested Dictionary In Python
people = {
    1: {'name': 'John', 'age': '27', 'gender': 'Male'},
    2: {'name': 'Marie', 'age': '22', 'gender': 'Female'}
}
print(people[1]['name'])
print(people[1]['age'])
print(people[1]['gender'])
