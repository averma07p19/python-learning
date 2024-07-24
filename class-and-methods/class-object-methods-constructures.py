""" class is a blueprint/template which can be design or filled with instructions (functions or tasks) and those can be used repeatedly 
"""

# class lbg():
#     name = "Ankur"
#     skill = ["Data Engineer", "Manager", "HR", "BA"]
#     language = ["SAS", "Python", "SQL"]
#     salary = [50000000, 100000, 1000000]
#     experience = 

#     def __init(self):
#         print("Please enter your")

class exl():
    name = "Ankur"             #all these are class attributes
    skill = "Data Engineer"
    language = "Python"
    salary = 100000000

    @staticmethod     #this is used to tell the functions that there is not input argument
    def __init__():  #this is a constructor which will be actuated right after object is assigned to a class
        print("Welcome, have a good day!")

    # @staticmethod
    # def :
        
    def msg(self):
        print(f"you are {self.name} working as a {self.skill} and you work on {self.language}\nYour salary should be {self.salary}")
    
    
    @staticmethod
    def experience(age):
        print(f"Your total experience is {age/3} years")
    

mars = exl()
# mars.name = "Ankur Verma"  #this is instance attribute
age = 30
# mars.age = 
# mars.language = "SAS"
mars.msg()
mars.experience(age)