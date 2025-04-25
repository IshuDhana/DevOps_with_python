my_list = [1,2,3,4]
print(my_list)
print(my_list[1])

#mutable
my_list[2] = 8
print(my_list)

#duplication
my_list = [1,2,3,4]

print(my_list)

#set
my_set = {1, 2, 3, 4, 5}
print(my_set)

#mutable
my_set.add(6)
print(my_set)

#no duplicate element
my_set = {1, 2, 2, 3, 4}
print(my_set)

#list
if 3 in my_list:
    print("3 is in the list")

# Sets
if 3 in my_set:
    print("3 is in the set")

    
'''Choosing Between Lists and Sets
Use Lists When:

You need to maintain the order of elements.
Duplicate elements are allowed.
You need to access elements by index.
Use Sets When:

Order doesn't matter.
You want to ensure unique elements.
You need to perform set operations like union, intersection, or difference.'''