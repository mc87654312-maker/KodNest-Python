# # Hash method
# print(hash(10))
# print(hash("hello"))
# print(hash(1.0))

# x = "Python"
# print(hash(x))

# # hashing in sets

# s = {1, "python"}
# # print(hash(s)) not posible

# a = 1
# b = 1.0
# print(hash(a))
# print(hash(b))
# print(a == b)
# print(a is b)

# custom hashing - __dunder, magic
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def __eq__(self, other):
        return self.name == other.name and self.age == other.age    
p1 = Person("john", 30)
p2 = Person("john", 30)        
print(p1 == p2)
# print(hash(p1))
# print(hash(p2))

# Function Overloading - Same name, different parameters

def add(a, b):
    print(a + b)


def add(a, b, c):
    print(a + b + c)


def add(a, b, c, d):
    print(a + b + c + d)


# add(1, 2)       # 3
# add(1, 2, 3)    # 6
add(1, 2, 3, 4)   # 10


# Python does not support function overloading
# The last function definition will overwrite the previous definition


# Default Arguments

def add(a, b=0, c=0, d=0):
    print(a + b + c + d)


# add()       # Error: missing required positional argument
add(100)      # 100 (100+0+0+0)
add(1, 2)     # 3 (1+2+0+0)
add(1, 2, 3)  # 6 (1+2+3+0)
add(1, 2, 3, 4)  # 10 (1+2+3+4)


# *args = *(0...infinity)

def add(*args):
    print(sum(args))


add(1, 2)       # 3
add(1, 2, 3)    # 6
add(1, 2, 3, 4) # 10
add()           # 0


# **kwargs = **{key:value, key:value}

def add(**kwargs):
    print(kwargs)


add(a=1, b=2)  # {'a': 1, 'b': 2}