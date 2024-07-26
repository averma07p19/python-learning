from random import randint

class employee:
    name = "Ankur"
    position = "Project Manager"
    experience = 11
    project = "LBG"
    company = "EXL"

    def __init__(self):
        print(f"Welcome to {self.company} portal, please enter employee details!")
        
    def msg(self):
        print(f"{self.name} works as {self.position} at {self.company}.\nHe is cunrrently engaged in {self.project}")

    # @staticmethod
    def exp(self):
        print(f"He has {self.age/3} years of work experience")
    

verma = employee()
# verma.msg()
# verma.exp(30)
verma.name = "Ankur Verma"
verma.age = 34
verma.msg()
verma.exp()
    