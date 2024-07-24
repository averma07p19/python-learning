class calculator:

    def __init__(self):  #its a construtor
        print("Welcome, what do you want to calculate (sum, multiplication, division, square, cube, square root)")

    @staticmethod
    def sum(n1,n2): # its a sum method
        print(f"Sum of {n1} and {n2} is : {n1 + n2}")

    @staticmethod
    def multi(n1,n2): #its a multiplication method
        print(f"Multiplication of {n1} and {n2} is : {n1 * n2}")
    
    @staticmethod
    def div(n1,n2): #its a division method
        if (n2 != 0):
            print(f"Division of {n1} and {n2} is : {n1 / n2}")
        else:
            print("Second number should not be zero to perform Division of two numbers")

    @staticmethod           
    def square(n1,n2): #its a squre number method
        print(f"Square of {n1} and {n2} is : {pow(n1,2)} and {pow(n2,2)} respectively")
    
    @staticmethod
    def cube(n1,n2):
        print(f"Cube of {n1} and {n2} is : {pow(n1,3)} and {pow(n2,3)} respectively")
    
    @staticmethod
    def sqrt(n1,n2):
        print(f"Square root of {n1} is {pow(n1,1/2)} and for {n2} it is {pow(n2,1/2)}")

maths = calculator()
maths.sum(2,3)
maths.multi(1,7)
maths.div(0,9)
maths.square(2,5)
maths.cube(3,1)
maths.sqrt(9,16)