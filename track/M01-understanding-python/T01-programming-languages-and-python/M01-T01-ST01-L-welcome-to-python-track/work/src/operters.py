# Arithematic Operators
print(3 + 3) # 6
print(3 - 3) # 0
print(3 * 3) # 9
print(3 / 3) #0.333333333333333
print(100 % 30) # 10
print(3 ** 3) # 27
print(10 // 3) # 3


# Comparison operators

print(11 == 10) # False
print(11 != 10) # True
print(11 > 10) # True
print(11 < 10) # False
print(11 >= 10) # True
print(11 <= 10) # False

# Assignment Operatyors

a = 10
print(a) # 10

a += 10 # a= a + 10 = 20
print(a)

a -= 10 # 10
print(a)

a *= 10 # 100
print(a)

a /= 10 # 10.0
print(a)

a %= 10 # 0.0
print(a)

a **= 10 # 0.0
print(a)

a //= 10 # 0.0
print(a)


# Logical Operators

a = True
b = False

print(a and b) # False
print(a or b) # False
print(not a) # True
print(not b) # True

a = (5 > 3) and (4 < 6) # True
a = (5 < 3) or (4 < 6) # True
a = not (5 > 3) # False


# Identity Operators
a = 10
b = 10
print(a is b) # True
print(a is not b) # False
print(a == b) # True
print(a !=b) # False

# Membership Operators

a = [1, 2, 3, 4, 5]
print(1 in a) # True
print(6 in a) # False
print(1 not in a) # False
print(6 not in a) # True

# Bitwise Operators

a = 2
b = 3

print(a & b) # 2
print(a | b) # 3
print(a ^ b) # 1
a = 5
print(~a) # -6
print(a << b) # 40
print(a >> b) # 0

# user_response = input(" Do you like ice cream ? (yes/no):").lower()

# is_ice_cream_lover = user_response == "yes"

# print(" Do you like ice cream ? ",is_ice_cream_lover)

# a = "Python"
# b = "Python"

# print(a==b)

# print(a is b)

a = 5
print(~a)

a = 2
b = 3

print(a & b)

print(a | b)

print(a ^ b)

