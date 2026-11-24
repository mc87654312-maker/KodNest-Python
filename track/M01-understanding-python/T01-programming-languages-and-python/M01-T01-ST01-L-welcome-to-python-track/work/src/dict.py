# ==========================================
# 1. DICTIONARY INTRODUCTION
# ==========================================

# Dictionary stores data in key:value pairs.
# Keys are immutable.
# Values can be of any data type.
# Duplicate values are allowed.
# Duplicate keys are not allowed.

dict1 = {
    "name": "John",
    "age": 30,
    "city": ["New York", "USA", "Germany"]
}

# Access and modify dictionary values
dict1["name"] = "Doe"

# Print dictionary methods
print(dict1)
print(dict1.keys())
print(dict1.values())
print(dict1.items())

# Check dictionary type and access elements
print(type(dict1))
print(dict1["name"])
print(dict1["city"][1])


# ==========================================
# 2. DICTIONARY CONSTRUCTOR
# ==========================================

# Creating dictionary using dict() constructor

stu_info = dict(name="Ram", age=30, city="USA")

# Adding a new key:value pair
stu_info["salary"] = 50000

# Updating existing value
stu_info["salary"] = 30000

# Updating dictionary using update()
stu_info.update({"salary": 20000})

# Removing a particular key using pop()
stu_info.pop("age")

# Removing the last inserted item using popitem()
stu_info.popitem()

# Deleting a particular key
del stu_info["city"]

# Removing all items from dictionary
stu_info.clear()

# Deleting the dictionary completely
del stu_info

# print(stu_info)  # NameError because dictionary is deleted


# ==========================================
# 3. LOOP THROUGH DICTIONARY
# ==========================================

dict1 = {
    "name": "John",
    "age": 30,
    "city": ["New York", "USA", "Germany"]
}

# Loop through dictionary values
for i in dict1.values():
    print(i)


# ==========================================
# 4. DICTIONARY METHODS
# ==========================================

# get() - Returns the value of the given key
print(dict1.get("name"))

# get() with default value
# If salary is not available, it returns 0
print(dict1.get("salary", 0))


# ==========================================
# 5. FROMKEYS()
# ==========================================

# Creates a new dictionary using given keys
# Default value will be None

print(dict1.fromkeys(["name", "age", "city"]))


# ==========================================
# 6. SETDEFAULT()
# ==========================================

# Returns the value if key already exists.
# Otherwise, inserts the key with the given value.

print(dict1.setdefault("name", "John"))


# ==========================================
# 7. COPY()
# ==========================================

# Creates a shallow copy of the dictionary

dict2 = dict1.copy()

print(dict2)