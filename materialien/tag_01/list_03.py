#a list of strings
str_list=['this', 'is', 'a', 'list']

print("before updating the list: ")
print(str_list)
str_list[3]='updated list'
print("after updating the list: ")
print(str_list)

#an empty list
empty_list=[]

#a list of strings
str_list=['this', 'is', 'a', 'list']

#to remove a specific element, like 'is'
str_list.remove('is')
print(str_list)

#to remove an item of a specific index like 2
del str_list[2]
print(str_list)

#there are yet another way to remove an item of a specific index
str_list.pop(0)
print(str_list)

#an empty list
empty_list=[]

#a list of strings
str_list=['this', 'is', 'a', 'list']

# add an element to the end of the list
str_list.append('appended')
print(str_list)

#insert an item at the defined index
str_list.insert(3,'inserted')
print(str_list)

#to get the index of the first matched item
print(str_list.index('a'))

#to count number of a specific element in a list
print(str_list.count('is'))

#to reverse the order of a list
str_list.reverse()
print(str_list)

#to sort the list in ascending order
str_list.sort()
print(str_list)