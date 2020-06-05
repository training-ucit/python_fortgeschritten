
my_dictionary = {} #init empty dictionary

#init dictionary with some key-value pair
another = {
            #key    : value,
            'man'   : 'Bob',
            'woman' : 'Alice',
            'other' : 'Trudy'
        }

#print initial dictionaries
print(my_dictionary)
print(another)

#insert value
my_dictionary['day']='Thursday'
another['day']='Thursday'
my_dictionary['color']='Blue'
another['color']='Blue'

#print updated dictionaries
print('Updated Dictionaries:')
print(my_dictionary)
print(another)

#update values
my_dictionary['day']='Friday'
another['day']='Friday'
my_dictionary['color']='Black'
another['color']='Black'

#print updated dictionaries
print('After Update:')
print(my_dictionary)
print(another)

#printing a single element
print(my_dictionary['day'])
print(another['color'])

