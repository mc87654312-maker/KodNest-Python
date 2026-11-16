# part 1- If, If-else, If-el-if-else( 12 Programs)
#Program1: check whether a number is positive.
n = 5
if n > 0:
    print("Number is positive")
elif n == 0:
    print("Number is zero")
else:
    print("Number is Negative") 

#Program2: check if a person is eligible to donate blood (age >= 18).

age = 21
if age >= 18:
    print("Eligible to danate blood")
else:
    print("not eligible to donate blood")

#Program3: check if the temperature is above 30 degree celsius and print "Hot Day"

temp = 40
if temp >= 30:
    print("Hot Day")
else:
    print("Cold Day")

#Program4: check wheather a student has attended at least 75% of classes

attendance = 80
if attendance >= 75:
    print("Eligible for appear for Exam")
else:
    print("not eligible for appear exam")    

#Program5: check whether a number is Even or Odd.

num = 67
if num % 2 == 0:
    print("Even Number")
else:
    print("Odd Number")

#Program6: check whether a person  is eligible to apply to apply for driving license.

age = 18
if age >= 18:
    print("Eligible for Applying driving License")
else:
    print("Not Eligible for Applying Driving License")


#Program7: check whether a given year is leap yearelse else.

year = 2023
if year % 400 == 0:
    print("Leap year")
elif year % 100 == 0:
    print("Not a leap year")
elif year % 4 == 0:
    print("Leap year")
else:
    print("Not a leap year")

#Program9: Assign grades based on marks.


marks = 100

if marks >= 90 and marks <= 100:
    print("Grade A")

elif marks >= 80 and marks < 90:
    print("Grade B")

elif marks >= 70 and marks < 80:
    print("Grade C")

elif marks >= 60 and marks < 70:
    print("Grade D")

elif marks < 60:
    print("Fail")

else:
    print("Invalid marks")

# Program 10: electricity usage.

electricity  = 500
if electricity >= 500:
    print("High")
elif electricity >= 300 and electricity <= 500:
    print("medium")
elif electricity >101 and electricity <= 300:
    print("Low")
elif electricity < 100:
    print("Very Low")
else:
    print("Invalid Input")    


# program 11: Scholarship eligibility

marks = float(input("Enter your marks: "))
income = float(input("Enter family income: "))

if marks >= 85 and income < 300000:
    print("Eligible for scholarship")
else:
    print("Not eligible for scholarship")

# program 12 user login

username = input("Enter username: ")
password = input("Enter password: ")

if username == "admin" and password == "12345":
    print("Login successful")
else:
    print("Invalid username or password")

# Display weekday using numbers (1–7)

day = int(input("Enter a number (1-7): "))

if day == 1:
    print("Monday")
elif day == 2:
    print("Tuesday")
elif day == 3:
    print("Wednesday")
elif day == 4:
    print("Thursday")
elif day == 5:
    print("Friday")
elif day == 6:
    print("Saturday")
elif day == 7:
    print("Sunday")
else:
    print("Invalid day number")

# Print numbers from 1 to 20

for i in range(1, 21):
    print(i)

# Print the multiplication table of a given number

num = int(input("Enter a number: "))
for i in range (1,11):
    print(num,"x",i,"=", num*i)

#Print numbers from 10 to 1
i = 10

while i >= 1:
    print(i)
    i = i - 1

# Find the factorial of a number

num = int(input("Enter a number: "))

factorial = 1
i = 1

if num < 0:
    print("Factorial is not defined for negative numbers")
else:
    while i <= num:
        factorial = factorial * i
        i = i + 1

    print("Factorial =", factorial)

# Break Statement

for i in range(1, 21):
    if i == 15:
        break

    print(i)

#Search for a number in a list using break

numbers = [10, 20, 30, 40, 50]

search = int(input("Enter a number to search: "))

for num in numbers:
    if num == search:
        print("Number found")
        break
else:
    print("Number not found")

# Continue Statement

for i in range(1, 21):
    if i % 3 == 0:
        continue

    print(i)

# Print odd numbers from 1 to 50

for i in range(1, 51):
    if i % 2 == 0:
        continue

    print(i)

# Functions

def cube(num):
    return num * num * num


n = int(input("Enter a number: "))

result = cube(n)

print("Cube =", result)

# Find the maximum of two numbers

def maximum(a, b):
    if a > b:
        return a
    else:
        return b


x = int(input("Enter first number: "))
y = int(input("Enter second number: "))

result = maximum(x, y)

print("Maximum number =", result)

# Pass Statement

def display():
    pass


display()

print("Program executed successfully")




