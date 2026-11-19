# set-{} it is an unordered collection of elements and it is immutable, unindexed, items are unchagnable but add
# or remove, no duplicate elements are created.
fruits = {"apple","banana","kiwi", "apple"}
print(fruits, type(fruits))

# set constructor
stu_info = set(("RAM", 23, 89.65, "a"))
print(stu_info, type(stu_info), len(stu_info))

fruits2 = set(("apple", "banana", "kiwi"))
print(fruits2, type(fruits2))

# set method
# add()

fruits = {"apple", "banana", "kiwi", "apple"} # it is not allow duplicate element
nfruits = {"orange", "lemon", "grapes"}
fruits.update(nfruits)
print(fruits)

# remove()
fruits.remove("banana")
print(fruits)

# discard()
fruits.discard("apple")
print(fruits)


# pop() - last element remove
fruits.pop()
print(fruits)

# clear()
fruits.clear()
print(fruits)

# del
del fruits
# print(fruits)
fruits = {"apple", "banana", "kiwi"}
for i in fruits:
    print(i)

# immutable frozenset
fruits = frozenset({"apple", "banana", "kiwi"}) # it is constant it not changable once created (frozenset)
print(fruits, type(fruits))
for i in fruits:
    print(i)
# fruits.add("orange") 
# print(fruits)   

names = ["Ram","Sita","sam"]
new_names = names.copy()
names[0] = "shamm"
print(names)
print(new_names)