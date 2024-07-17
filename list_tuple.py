"""
different methods for LIST
1. APPEND - it adds new tuple at the end of the list
2. SORT - sorts list of number
3. INSERT - insert new item at specific position
 """

# name_q = input("what is your name?\n")
# with_name = f"My name is {name_q.title()}"
# print(with_name)
# a = with_name.split(" ")
# print(a, type(a))
# print(f"Your first name is : {a[3]}")

# APPEND method
# name_q = input("what is your name?\n")
# with_name = f"My name is {name_q.title()}"
# print(with_name)
# a = with_name.split(" ")
# a.append("WOW!")
# print(a, type(a))
# print(f"Your first name is : {a[3:5]}")

# SORT method
# l1 = [88,17, 19, 1, 9, 163, 83]
# l1.sort()
# print(l1)

# INSERT method
# l1 = [88,17, 19, 1, 9, 163, 83]
# l1.insert(4,"Ankur")
# print(l1)

"""TUPLEs and different methods"""

# a = (1,2,"ankur", "apple")
# print(a, type(a))

# a = (1) 
# print(a, type(a)) # this is an integer not a tuple, if you wish to create a tuple with single entry then do like a = (1,)

# i = 1
# fruit = []
# while i <= 3:
#     fruit_n = input("enter the fruit name : ")
#     fruit.append(fruit_n)
#     i = i + 1
# print(fruit[2])    

# enter marks of students and sort them
# n_students = int(input("how many students : "))
# marks = []
# i = 1
# while i <= n_students:
#     marks1 = input(f"enter the marks of student_{i} : ")
#     marks.append(marks1)
#     i = i+1
# marks.sort()    
# print(marks)

#make a sum of numbers
n = int(input("how many number you want to add : "))
n_sum = []
total_sum = 0
i = 1
while i <= n:
    try:
        numbers = int(input(f"Please enter the {i} number : "))
        n_sum.append(numbers)
        total_sum = total_sum + numbers
        i = i+1
    except ValueError:
        print("Invalid input. Please enter an integer.")
print(n_sum, type(n_sum), total_sum)


#counting 0s in a tuple
# a = (3, 4, 0,1,3,56,2,7,0,0,4,1)
# a.count(0)
# print(a.count(0))




