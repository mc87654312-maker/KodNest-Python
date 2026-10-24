# #def largest of 3 numbers
# # def largest():
# #     first = int(input("Enter first number:"))
# #     second = int(input("Enter second number:"))
# #     third = int(input("Enter third number:"))
# #     if first > second and first > third:
# #         print("First number is largest")
# #     elif second > first and second > third:    
# #         print("second number is largest")

# #     else:   
# #         print("third number is largest")

# # largest()     

# # add 2 numbers
# def add():
#     a = 10
#     b = 20
#     print(a+b)

# add() 

# # Square of a number
# def square():
#     a = 23
#     print(a*a)

# square()    

# #check if anumber is even or odd

# def even_or_odd():
#     a = 8
#     if a%2 == 0:
#         print("Even")
#     else:
#         print("odd")
# even_or_odd()

# # Greet with name

# def greet_with_name():
#     name = "Madhab"
#     print("Hello",name)
# greet_with_name()

# # No arguments + No return value
# def square():
#     a = 5
#     print(a*a)
# square()
# # No input + output
# def square():
#     n = 5 * 5
#     return n
# print(square()) 

# # input + no output
# def square(n):
#     res = n * n 
#     print(res)
# square(10)

# # input + output
# def square(n):
#     return n * n
# res = square(10)
# print(res)    

# Function with local and global variale
# c = 30      # global var
# def add():
#     global a # global var
#     a = 10
#     b = 20   # local var
#     print(a+b)
#     print(c)
# add()
# print(c)    

# local and have same name
# x = 100
# def display():
#     x = 50
#     print("Localb x:",x)
# display()
# print("global x:", x)

# Error

# x = 100
# def display():
#     print(x)
#     x = 50
#     print(x)
# display()
# x = 30
# print(x)

# Function overloading

# def add(a,b):
#     print(a+b)

# def add(a,b,c):
#     print(a+b+c)

# add(10, 20)
# add(10, 20, 30)    

# DEFAULT ARGUMENTS
# default args
# def add(a=0, b=0, c=0):
#     return a+b+c
# print(add(10))  
# print(add(10,20))
# print(add(10,20,30))    
# print(add())

# var args
# def add(*args):
#     total = 0
#     for i in args:
#         total = total + i
#         return total
# print(add(10,20,30))        


# *args - 0 ... n arguments can be passed

# def add(*a):
#     print(sum(a))

# add(10,20) 
# add(10,20,30)
# add(10)
# add()   

#**kwargs - 0 ... n arguments can be passed --> dict

# def stu_info(**kwargs):
#     print(f"Name is{kwargs.get('name')}", end = "")
#     print(f"Age is {kwargs.get('age')}", end = "")
#     print(f"course is {kwargs.get('course')}")

# stu_info(name = "madhab", age = 21, course = "python")  

# Recursion

# def count(n):
#     if n==0:
#         return
#     print(n)
#     count(n-1)
# count(5)        

# Factorial

# def fact(n):
#     if n==0 or n==1:
#         return 1
#     else:
#         return n*fact(n-1)
# print(fact(5))            

# Fibbonaci Series 0,1,1,2,3,5,8......

def fib(n):
    if n==0:
        return 0
    elif n==1:
        return 1
    return fib(n-1)+fib(n-2)

print(fib(5))        