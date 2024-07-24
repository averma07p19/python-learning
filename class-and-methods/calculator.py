class calculator:

    def __init__(self, num1, num2):  #its a construtor
        print("Welcome, what do you want to calculate (sum, multiplication, division, square, cube, square root)")
        self.num1 = num1
        self.num2 = num2

    def sum(self): # its a sum method
        print(f"Sum of {self.num1} and {self.num2} is : {self.num1 + self.num2}")

    def multi(self): #its a multiplication method
        print(f"Multiplication of {self.num1} and {self.num2} is : {self.num1 * self.num2}")
    
    def div(self): #its a division method
        if (self.num2 != 0):
            print(f"Division of {self.num1} and {self.num2} is : {self.num1 / self.num2}")
        else:
            print("Second number should not be zero to perform Division of two numbers")

    @staticmethod           
    def square(n1,n2): #its a squre number method
        print(f"Square of {n1} and {n2} is : {pow(n1,2)} and {pow(n2,2)} respectively")
    
    def cube(self):
        print(f"Cube of {self.num1} and {self.num2} is : {pow(self.num1,3)} and {pow(self.num2,3)} respectively")
    
    def sqrt(self):
        print(f"Square root of {self.num1} is {pow(self.num1,1/2)} and for {self.num2} it is {pow(self.num2,1/2)}")

maths = calculator(4,5)
maths.sum()
maths.multi()
maths.div()
maths.square(2,3)
maths.cube()
maths.sqrt()