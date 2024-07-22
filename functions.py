
# def greet_user(name):
#     print(f"Hello Mr. {name.title()}, its a loveyoly day out there, Enjoy!")
#     # return

# name = input("Please enter your name :\n")
# # greet_user(name)
# statement = greet_user(name)
# print(statement)

"""recursive function to calculate a factorial"""
# n = int(input("enter a number to calculate factorial : "))
# def factorial(n):
#     if (n==0) or (n==1):
#         return 1
#     return n * factorial(n-1)
# print(f"factorial of a '{n}' is : {factorial(n)}")

""" function to find max of 3 number """

# num_list = input("enter the numbers below separated by comma (,) :\n")
# def find_max(num_list):
#     num_list_1 = [int(x) for x in num_list.split(",")]
#     print(f"max number out of {num_list_1} is : {max(num_list_1)}")

# find_max(num_list)

"""celcius to fahrenheit convert
c\5 = (f-9) /32
"""
# f = float(input("Enter the temperature in F : "))
# def f_to_c(f):
#     c = 5 * (f - 32)/9
#     return c
# print(f"Temperature in C is : {round(f_to_c(f), 2)}")

""" print statement without producing any new line"""
# print("ankur", end=" | ")
# print("pallavi", end=" | ")
# print("papa", end=" | ")
# print("mummy", end=" | ")
# print("rishan", end=" | ")

""" function to sum the first n natural numbers 
natural number = +1 to infinity 
sum(n) = 1 + 2 + 3 + 4 + 5... (n-2) + (n-1) + n
sum(n) = sum(n-1) + n
"""
# n = int(input("Enter a positive number : "))
# def sum_of_n(n):
#     if (n==1): #its a base condition to stop the iteration, else it will go beyond and start summing negative values
#         return 1 #return 1 when base condition hits
#     return  n + sum_of_n(n-1)
# print(f"Sum of first Natural numbers is : {sum_of_n(n)}")

# i = 1
# sum = 0
# while i <= n:
#     sum = sum + i
#     i +=1
# print("sum is : ", sum)

"""draw star pattern"""
# n = int(input("Enter how many lines of stars you want :\n"))
# for i in range(1,n+1):
#     print("*"*(n+1-i))

# def star_pattern(n):
#     if n == 0:
#         return
#     print("*"*n)
#     star_pattern(n-1)

# star_pattern(n)

"""multiplication table of a number using function"""
# user_num = int(input("enter the number to get the table : "))
# i = 1
# def multiply(n, i):
#     if i == 11:
#         return
#     print(f"{n} * {i} : {n * i}")
#     multiply(n, i+1)

# multiply(user_num,i)