# str = """all is 
# well"""
# print(str)

# str = "my name is  \"Madhab\" & i study in \'kodnest\'"
# print(str)

# str = 'my name is  \"Madhab\" & i study in \'kodnest\''
# print(str)

# str = """my name is  \"Madhab\" & i study in \'kodnest\' """
# print(str)

a = "hello"
b = "world"
c = a + " " +b
print(c)

# string formatting
age = 23
print("my age is:" + " "+ str(age))

# Question
s1 = " "
res = bool(s1)
print(res) # True

# Question
s1 = ""
res = bool(s1)
print(res) # False

# is and == identity operator

a  = [1, 2, 3]
b = a
c = [1, 2, 3]

print( a is b)
print(a is c)  # checks the address
print(a == c)  # checks the content

# print address of any object

s1 = "Python"
s2 = "Python"

print(s1, id(s1))

# Question 
s1 = "Python"
s2 = "Python"

print(s1 is s2)
print(s1 == s2)

# Q
s1 = "hello"
print(s1)
s1 = s1 + "world"
print(s1)   # string is immutable if we need to add the another things then we reassign a variable

#
s1 = "hello"
print(s1, id(s1))
s1 = s1 + "world"
print(s1, id(s1))

# String methods
# inbuilt string method - single program

s = "KodNest Technologies 123 "

print("Original String:", s)

# case conversion methods
print("upper():", s.upper())
print("lower():", s.lower())
print("capitalize():", s.capitalize())
print("title():", s.title())
print("swapcase():", s.swapcase())

# searching and counting
print("find('Tech'):", s.find("Tech"))
print("count('o'):", s.count("o"))

# Replace
print("replace('123', '2025'):", s.replace("123", "2025"))

# start & End checks
print("startswith('  Kod'):", s.startswith("  Kod"))
print("endswith('123  '):", s.endswith("123  "))

# split and join

words = s.split()
print("split():", words)
print("join:", "-".join(words))

#strip Spaces
print("strip():", s.strip())
print("lstrip():", s.lstrip())
print("rstrip():", s.rstrip())

#checking Methods
print("isalpha():", s.isalpha())
print("isdigit():", s.isdigit())
print("isalnum():", s.isalnum())

#length
print("length if string:", len(s))