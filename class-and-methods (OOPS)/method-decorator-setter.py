
"""super method"""
# class employee:
#     def __init__(self):
#         print("Welcome you are the employee!")

# class engineer(employee):
#     def __init__(self):
#         print("you are the engineer!")

# class manager(engineer):
#     def __init__(self):
#         super().__init__()
#         print('you are the manager!')


# a = employee()
# b = engineer()
# c = manager()


""" class method 
Its a method to directly access of a class into a function of that class """
class testing:
    a = 1
    # @classmethod
    # def __init__(cls):
    #     print(f"print the value of class attribute 'a' == {cls.a}")

    @classmethod
    def test1(cls):
        print(f"print the value of class attribute 'a' == {cls.a}")

    @staticmethod
    def name(name):
        print(f"My name is {name}")

    @staticmethod
    def age1(age):
        print(f"My age is {age}")

o = testing()
o.a = 45
# print(o.a)
# name = 'Ankur'
# o.name(name)

o.age = 34
o.age1(o.age)





""" property decorator"""






""" getter and setter """