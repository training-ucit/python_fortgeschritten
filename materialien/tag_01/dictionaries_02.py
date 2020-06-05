dictionary = {
    'name'  : 'Alex',
    'age'   : 23,
    'sex'   : 'male'
    }

#method1
print('Method1')

#fetch all the keys of that dictionary
key_list = dictionary.keys() #store the key list in key_list

#print to see the keys
print('list of keys')
print(key_list)

#pick key from the key_list
for key in key_list:
    #print the specific value for the key
    print('key = '+key+' value = '+str(dictionary[key]))

#method2
print('\nMethod2')

#pick key from directly from the dictionary
for key in dictionary:
    #print the specific value for the key
    print('key = '+key+' value = '+str(dictionary[key]))