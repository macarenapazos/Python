#set is a list of unique elements

my_set = {1,2,3,4,5,5}
print(my_set) #would print {1,2,3,4,5}
print(len(my_set)) #would print 5

new_set = my_set.copy()
my_set.clear()
print(new_set)
print(my_set)

my_set = {1,2,3,4,5}
your_set = {4,5,6,7,8,9,10}

print(my_set.difference(your_set))
my_set.discard(5) #discard the element of my set
print(my_set) #would print {1,2,3,4}
my_set.differrence_update(your_set)
print(my_set) 
print(my_set.intersection(your_set))
print(my_set & your_set) #same as intersection
print(my_set.isdisjoint(your_set)) # does the set have something in common?
print(my_set.issubset(your_set))
print(my_set.issuperset(your_set))
print(my_set.union(your_set)) #unificate the sets but removes the duplicates
print(my_set | your_set) #same as union