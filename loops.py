"""while loop"""
# i = 1
# while (i<50):
#     print(i)
#     i +=1


# i = 1
# while i in range(0,55):
#     print(i)
#     i +=1

"""FOR loop"""    
# for i in range(0,60, 2):
#     print(i)
#     i +=1

# Ex - 1
#list iteration
# ls = [1,2,"ankur", "verma", 35]
# for i in ls:
#     print(i)
#     ls.append(str(i)+"_1")
#     if (len(ls) == 20):
#         break
# print(ls)    

#print fibonachi series 1,1,2,3,5,8
# i = 1
# fib_list = []
# fib_next_num = 0
# while i < 25:

#     if i ==1:
#         fib_num = i - 1
#         fib_next_num = fib_num + i
#         fib_list.extend((fib_num, fib_next_num))
#     else:
#         fib_next_num = fib_list[i-2] + fib_list[i-1]
#         fib_list.append(fib_next_num)
#         if (i==20):
#             break
#     i +=1

    
# print(fib_list)        


"""
break : it instructs the program/loop to break and exit (can be used in the beginning or at the end of the program if you want that iteration to complete and then break)
continue : it instructs the loop to skip this specific iteration (should be used in the beginning)
pass : it is a null statement and tells program to to NOTHING but simply pass
"""

# for i in range(10):
#     if i == 5:
#         continue
#     if i == 8:
#         break
#     print(f"hello, my nuber is : {i}")

"""Ex. 1 write a table of any number given by user"""

# user_given_input = int(input("Please enter a number of your choice : "))
# print(user_given_input, type(user_given_input))
# i = 1
# while i <=10:
#     multiplication = user_given_input*i
#     print(f"{user_given_input} * {i} = {multiplication}")
#     i += 1

"""using for loop"""
# user_given_input = int(input("Please enter a number of your choice : "))
# # print(user_given_input, type(user_given_input))
# for i in range(1,11):
#     # multiplication = user_given_input*i
#     print(f"{user_given_input} * {i} = {user_given_input * i}")
#     i += 1

# l1 = ["Ankur", "abhishek", "twikle", "Rinku"]
# for name in l1:
#     if (name.title().startswith("A")):
#         print(f"Hello {name.title()}")

"""find the PRIME number"""
# n = int(input("what number you want to check for Prime number : "))
# for i in range(2,n):
#     if (n%i == 0):
#         print(f"{n} is not a Prime number")
#         break
# else:
#     print(f"*** {n} is a Prime number ***")

"""to calculate a factorial of a number"""
# n = int(input("what number you want to calculate the Factorial : "))
# multiply = 1
# for i in range (1,n+1):
#     multiply = multiply * i
#     i +=1
# print(f"Factorial of {n} is :: {multiply}")

"""to print star pattern
   *
  ***
 *****
*******
"""
# n = int(input("How many lines of STARs you want : "))
# for i in range(n+1):
#     print(" "* (n-i) + "*"*(2*i-1))


"""to print star pattern
*
**
***
****
"""
# n = int(input("How many lines of STARs you want : "))
# for i in range(n+1):
#     print("*"*i)

"""to print star pattern for n = 3
***
* *
***
# """
# n = int(input("How many lines of STARs you want : "))
# for i in range(1,n+1):
#     if ((i==1) or (i==n)): 
#         # pass
#         print("*"*(n))
#     else:
#         # pass
#         print("*" + " "*(n-2) + "*")        

"""to print a table of any user given number in reverse order"""
n = int(input("Give a numer : "))
for i in range(1,11):
    print(f"{n} * {11 - i} = {n * (11-i)}")



