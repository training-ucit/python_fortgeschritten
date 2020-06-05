#an empty tuple
emptyTup=()

#tuple of string
strTup=('This','is','a','tuple')

#tuple of integers
intTup=(1,2,3,4,5)

#tuple of string
strTup=('This','is','a','tuple')

#accessing first element
print(strTup[0])

#accessing second element
print(strTup[1])

#accessing fourth element
print(strTup[3])

#tuple of string
strTup=('This','is','a','tuple')

#accessing first element from the right
print(strTup[-1])

#accessing second element from the right
print(strTup[-2])

#accessing second element from the right
print(strTup[-4])

#tuple 1
tup1=(1,2,3)

#tuple 2
tup2=(4,5)

#tuple 3
tup3=tup1+tup2

print(tup3)

#to delete tuple 1
del tup1
#this will show a traceback as tup1 is deleted. So it is not defined now
print(tup1)

#a string tuple

tup=('this','is','a','tuple')


#len(tuple) gives total length of a tuple
print(len(tup))

#max(tuple) gives maximum element of a tuple
print(max(tup))

#min(tuple) gives minimum element of a tuple
print(min(tup))

#count(x) gives number of occurances of x in the tuple
print(tup.count('is'))

#index(x) gives index of first occurances of x in the tuple
print(tup.index('a'))
