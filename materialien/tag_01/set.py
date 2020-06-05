#set containing single data-type
set1 = {1, 2, 3, 4, 2, 3, 1}
print(set1)

#set containing multiple data-type
set2 = {1, 2, 3, (1, 2, 3), 2.45, "Python", 2, 3}
print(set2)

#creating a set from a list
theList = [1, 2, 3, 4, 2, 3, 1]
theSet = set(theList)
print(theSet)

#initialize an empty set
theSet = set()

#add a single element using add() function
theSet.add(1)
theSet.add(2)
theSet.add(3)
theSet.add(2)
#add another data-type
theSet.add('hello')

#add iterable elements using update() function
theSet.update([1,2,4,'hello','world']) #list as iterable element
theSet.update({1,2,5}) #set as iterable element
print(theSet)

theSet = {1,2,3,4,5,6}

#remove 3 using discard() function
theSet.discard(3)
print(theSet)

#call discard() function again to remove 3
theSet.discard(3) #This won't raise any exception
print(theSet)

#call remove() function to remove 5
theSet.remove(5)
print(theSet)

#call remove() function to remove 5 again
theSet.remove(5) #this would raise exception
print(theSet) #this won't be printed

A = {1, 2, 3, 4} #initializing set A
B = {2, 3, 5, 7} #initializing set B

union_operation = A.union(B)

print("A union B :")
print(union_operation)

intersection_operation = A.intersection(B)

print("A intersection B :")
print(intersection_operation)

difference_operation = A.difference(B)

print("A-B :")
print(difference_operation)

difference_operation = B.difference(A)
print("B-A :")
print(difference_operation)

