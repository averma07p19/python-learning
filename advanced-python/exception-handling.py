"""try and expect"""
# try :
#     name = int(input("enter your name brother : "))
#     print(name)
# except Exception as e:
#     print(e)


# print("Thank you")

"""try and raise"""

# try :
#     a = int(input("enter first number : "))
#     b = int(input("enter second number : "))
#     if (b==0):
#         raise ZeroDivisionError("What the fuck man, you cant divide any number by 0, dont do that again")
#     else:
#         print(f"division is : {a/b}")
# except Exception as e:
#     print(e)


# print("Thank you")

"""try, except, else
if try is successfull then it will go in else and execute the code"""

# try :
#     a = int(input("enter first number : "))
#     b = int(input("enter second number : "))
#     if (b==0):
#         raise ZeroDivisionError("What the fuck man, you cant divide any number by 0, dont do that again")
#     else:
#         print(f"division is : {a/b}")
# except Exception as e:
#     print(e)

# else:
#     print("we are in else right now")




"""try, except, finally
use of finally with try and except is meaningful in functions, 
when you give return after a speicific operation but you also want to run a specific piece of code in any case.
Otherwise if we are using finally out of functions then use of it wont make any difference
NOT GOOD FOR USE ACTUALLY, IT FEELS LIKE ERROR PRONE"""

# def finally_func():
#     try :
#         a = int(input("enter first number : "))
#         b = int(input("enter second number : "))
#         if (b==0):
#             raise ZeroDivisionError("What the fuck man, you cant divide any number by 0, dont do that again")
#         else:
#             print(f"division is : {a/b}")
#         return
            
#     except Exception as e:
#         print(e)
#         # return
#     # finally:
#     print("Thank you")

# finally_func()        

