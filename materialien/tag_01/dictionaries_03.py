dictionary = {
    'name'  : 'Alex',
    'age'   : 23,
    'sex'   : 'male'
    }

#print initial dictionary
print(dictionary)

#delete a single element
del dictionary['name']
print('After deleting name')
print(dictionary)


'''
you cannot the element which is not in the dictionary. so the below statement
will raise an error

del dictionary['name']
'''


#delete all elements from the list
dictionary.clear()
print(dictionary) #this will show an empty dictionary

#delete the entire variable
del dictionary
print(dictionary) #this will produce error