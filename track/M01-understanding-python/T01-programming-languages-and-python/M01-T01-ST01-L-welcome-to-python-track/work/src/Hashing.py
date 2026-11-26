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
