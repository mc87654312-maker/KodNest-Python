# union - | operator also can be used
fruits =  {"apple", "banana", "kiwi"}
fruits2 = {"orange", "mango", "grapes"}
print(fruits.union(fruits2))
# intersection() - & operator also can be used

fruits = {"apple", "banana", "kiwi"}
fruits2 = {"orange", "mango", "grapes"}

print(fruits.intersection(fruits2))

# difference()

fruits = {"apple", "banana", "kiwi"}
fruits2 = {"orange", "mango", "grapes"}
print(fruits.difference(fruits2))
print(fruits2 - fruits)

# symmetric_difference() - ^ operator also can be used

fruits = {"apple", "banana", "kiwi"}
fruits2 = {"orange", "mango", "grapes"}
print(fruits.symmetric_difference(fruits2))
print(fruits ^ fruits2)

# update()
fruits = {"apple", "banana", "kiwi"}
fruits2 = {"orange", "mango", "grapes"}
print(fruits.update(fruits2))
print(fruits)

# discard()
fruits.discard("apple")
print(fruits)

# remove()

fruits.remove("banana")
print(fruits)

# difference_update()
fruits = {"apple", "banana", "kiwi", "grapes"}
fruits2 = {"orange", "mango", "grapes"}
fruits.difference_update(fruits2)
print(fruits)

#intersection_update()

fruits = {"apple", "banana", "kiwi"}
fruits2 = {"orange", "mango","grapes"}
fruits.intersection_update(fruits2)
print(fruits)

# symmetric_difference_update()
fruits = {"apple", "banana", "kiwi"}
fruits2 = {"orange", "mango", "grapes"}

fruits.symmetric_difference_update(fruits2)
print(fruits)

# isdisjoint()
fruits = {"apple", "banana", "kiwi"}
fruits2 = {"orange","mango", "grapes"}
print(fruits.isdisjoint(fruits2))
print(fruits)

# issubset()
fruits = {"apple", "banana", "kiwi"}
fruits2 = {"apple", "banana", "kiwi","orange","mango", "grapes"}
print(fruits.issubset(fruits2))

#issuperset()
fruits = {"apple", "banana", "kiwi"}
fruits2 = {"apple", "banana", "kiwi","orange","mango", "grapes"}
print(fruits.issuperset(fruits2))

# frozenset()

fruits = frozenset({"apple","banana","kiwi"})
print(fruits, type(fruits))