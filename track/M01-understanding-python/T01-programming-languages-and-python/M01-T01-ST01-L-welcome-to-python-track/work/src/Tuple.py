# Tuples -> () ordered,

nums = (1,2,3,4,5)
# nums[0] = 100 # immutable
print(nums, type(nums))

stu_info = ("Mohamad", True, 7.93, 22)
print(stu_info)
print(stu_info[0])  # indexing
print(stu_info[0:2]) # slicing
print(stu_info[-2]) # negative indexing

name = ("madhab",)
print(name)
print(type(name))

# 
lst = [1,2,3]
print(lst, type(lst))
# Tuple constructor
rgb = tuple("red")
print(rgb)
print(type(rgb))
# Adding and removing elements
t = (10, 20, 30)

# Convert tuple into list
a = list(t)

# Add element
a.append(40)

# Convert list into tuple
t = tuple(a)

print(t)

#Remove elements

t = (10, 20, 30, 40)

a = list(t)

a.remove(20)

t = tuple(a)

print(t)

#loop
z = (10,20,12,10)

for i in range(len(z)):
    print(z[i])

#    unpacking of tuples
emp =("Mohamad", 22, "Developer")
print(emp, type(emp))
(name, age, role) = emp
print(name)
print(age)
print(role)

#tuple b*
s = (2, 4, 6, 8, 10)
(a, *b, c) = s
print(a)
print(b)
print(c)
# other methods
t = (10, 20, 30, 40, 50)
print(len(t))
print(max(t))
print(min(t))
print(sum(t))
print(sorted(t))
print(any(t))
print(all(t))
print(10 in t)

t1 = (1, 2)
t2 = (3, 4)

print(t1 + t2)
print(t1 * 2)
del t

#list aliasing and shared Reference
# rename => aliasis

stu1 = stu_info
print(stu1)
print(stu_info)
print(stu1 is stu_info)
#
x = [1, 2, 3]
y = [1, 2, 3]
print(x, y)
print(x == y)
print(x is y)

###
t = (10, 20, 30, 40, 50, 60, 70, 80)

print(t[-6:-1])
print(t[-1:-6:-2])

#
t = (1, 2, 3, 4, 5, 6, 7, 8, 9)

print(t[7:2:-1])
print(t[8:1:-2])

#
t = (10, 20, 30, 40, 50, 60, 70, 80, 90)

print(t[-2:-8:-2])
print(t[-8:-2:2])
#
t = (5, 10, 15, 20, 25, 30, 35, 40, 45, 50)

print(t[::-2])
print(t[8::-3])
print(t[-2::-3])
#
t = (10, 20, 30, 40, 50)

print(t[2:2])
print(t[4:1])
print(t[-1:2])
print(t[1:4:-1])
#
t = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)

a = t[::-1]
b = a[2:8:2]

print(a)
print(b)
print(b[::-1])

#
t = (10, 20, 30, 40, 50)

print(t[2:100])
print(t[-100:3])
print(t[100:0:-1])
print(t[-100:100:2])
#
t = ((10, 20, 30), (40, 50, 60),
     (70, 80, 90), (100, 110, 120))

print(t[::-1])
print(t[1:4:2])
print(t[0][::-1])
print(t[::-1][1][1:])

#
t = (10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120)

a = t[::-1]
b = a[1:-1:2]
c = b[::-1]

print(a)
print(b)
print(c)
print(c[1::2])
print(c[-2::-2])

###
t = (10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120)

a = t[::-1]
b = a[1:-1:2]
c = b[::-1]

print(a)
print(b)
print(c)
print(c[1::2])
print(c[-2::-2])