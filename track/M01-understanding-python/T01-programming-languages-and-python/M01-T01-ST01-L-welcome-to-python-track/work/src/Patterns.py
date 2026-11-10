# # print a dimond star pattern
# rows = int(input("Enter no:"))

# # Upper pyramid
# for i in range(1, rows + 1):
#     for j in range(rows - i):
#         print(" ", end="")

#     for j in range(i):
#         print("*", end=" ")

#     print()

# # Lower inverted pyramid
# for i in range(rows - 1, 0, -1):
#     for j in range(rows - i):
#         print(" ", end="")

#     for j in range(i):
#         print("*", end=" ")

#     print()

# Pyramid


rows = 3

# Upper 3 rows
for i in range(1, rows + 1):
    print(" " * (rows - i) + "* " * i)

# Lower 3 rows
for i in range(rows, 0, -1):
    print(" " * (rows - i) + "* " * i)

# Hollow Rectangle Pattern.

rows = int(input("Enter no:"))
columns = int(input("Enter no:"))

for i in range(rows):
   for j in range(columns):
      if i == 0 or i == rows - 1 or j == 0 or j == columns - 1:
          print("*", end="")
      else:
          print(" ", end="")
   print()

# pyramid Alphabet Pattern.

rows = int(input("Enter a no:"))

for i in range(1, rows + 1):
    for j in range(rows-i):
        print(" ", end="")
    for j in range(1, i + 1):
        print(chr(64 + j), end="")
    for j in range(i - 1, 0, -1):
        print(chr(64 + j), end="")
    print()                  
    
          
