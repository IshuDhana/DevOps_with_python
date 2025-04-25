my_set = {1,2,3,4,5,6}
print(my_set)

my_set.add(6)
my_set.remove(5)

print(my_set)

set1 = {1,2,3,4,5,6,7}
set2 = {5,6,7,8,9,10}

union_set = set1.union(set2)
print("union:", union_set)
intersection_set = set1.intersection(set2)
print("intersection:", intersection_set)
difference_set = set1.difference(set2)
print("difference:",difference_set)

is_subset = set1.issubset(set2)
is_superset =set1.issuperset(set2)

print("issubset", is_subset)
print("issuperset", is_superset)




