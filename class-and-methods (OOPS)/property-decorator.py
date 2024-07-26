"""creating class to calculate and return of employee based on their promotions"""

class employee:
    company = "EXL"
    c1_increment = 20
    c2_increment = 25
    
    @property
    def salaryafterincrement(self):
        if (self.current_band=='C1') and (self.new_band=='C2'):
            return self.new_salary + self.new_salary * self.c2_increment / 100
        if (self.current_band=='B2') and (self.new_band=='C1'):
            return self.new_salary + self.new_salary * self.c1_increment / 100
        else:
            return "Not Found"
        
    @property
    def incrementbands(self):
        return f"B2 to C1 : {self.c1_increment}\nC1 to C2 : {self.c2_increment}"
    
    @salaryafterincrement.setter
    def totalincrement(self):
        self.c2_increment = (self.new_salary/self.old_salary-1)*100
        return self.c2_increment

    

ankur = employee()
#one method to get the salary after increment by passing the values to the method
# print(f"Your current salary after promotion is : {ankur.salaryafterincrement(3000000,'C1','C2')} ")  

#another method is to create instance attributes and the pass those attributes
ankur.old_salary = 250000
ankur.new_salary = 300000
ankur.current_band = 'C1'
ankur.new_band = 'C2'
# print(ankur.salaryafterincrement(ankur.salary,ankur.current_band,ankur.new_band))

#another method is by creating a property inside class and the print 
print(ankur.salaryafterincrement)

# ankur.incrementbands
# print(ankur.incrementbands)

#setting new c2_increment in class employee
# ankur.salaryafterincrement = 400000
# print(ankur.totalincrement())