# #list are mutable, ordered, and allows duplicate values and can be accessed using index or it is represented by square baracket
#index  0 1 2 3 4 5
nums = [1,2,3,4,5,3]
print(nums[2])
print(nums)
print(type(nums))

#
names = ["Alice", "Dob", "charlie"]
names[1] = "Bob"
print(names)
print(type(names))

#append
names = ["Alice", "Dob", "charlie"]
names.append("Ram")
names.insert(2, "sita") # insert method
names.pop()
names.remove("sita")
names.clear()
del names
#
names = ["Alice", "Dob", "charlie"]
names1 = ["David", "Eve", "Frank"]
lst1 = names.extend(names1)
print(lst1)
for i in names:
    print(i)



print(names.count("Alice"))
print(names.index("Dob"))
print(names.copy())
print(names.extend(names1))
#
n = [5,7,3,1,2,6]
sortedlist = sorted(n) # sorted in new list
print(sortedlist)
#
n = [5, 7, 3, 1, 2, 6]

print(n)
n.sort()  # sort will same list
print(n)
n.reverse()
print(n)
 
#
arr = [1,2,3]
newarr = arr.copy()
print(newarr)
print(arr)

colors = ["red","green","blue","yellow","purple"]
colors[1:2] = ["black","white"]
print(colors)

#slicing on list
a = [10, 20, 30, 40, 50, 60, 70, 80]
print(a[-2:-7:-2])

a = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(a[-1:-9:-3])

a = [10, 20, 30, 40, 50, 60]
print(a[-3::-2])

a = [1, 2, 3, 4, 5, 6, 7]
print(a[-2:1:-2])

a = [10, 20, 30, 40, 50, 60, 70]
print(a[-1:-8:-2])

a = [1, 2, 3, 4, 5, 6, 7, 8]
print(a[-5:-1:2])

a = [10, 20, 30, 40, 50, 60, 70]
print(a[-6:-1:3])

a = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(a[-2:-8:-2])

# part-2

a = [10, 20, 30, 40, 50]
print(a[-1:-6:-1])

a = [1, 2, 3, 4, 5, 6, 7]
print(a[-3:0:-1])

a = [10, 20, 30, 40, 50, 60, 70]
print(a[1:-2:2])

a = [1, 2, 3, 4, 5, 6, 7, 8]
print(a[-6:7:2])

a = [10, 20, 30, 40, 50, 60, 70]
print(a[5:-6:-2])

a = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(a[-7:8:3])

a = [10, 20, 30, 40, 50, 60]
print(a[4:-5:-1])

a = [10, 20, 30, 40, 50, 60, 70]
print(a[2:-1:-1])

a = [1, 2, 3, 4, 5, 6, 7]
print(a[-5:1:1])

a = [10, 20, 30, 40, 50, 60]
print(a[5:-1:-1])

a = [1, 2, 3, 4, 5, 6, 7, 8]
print(a[-2:0:2])