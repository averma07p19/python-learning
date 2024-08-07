"""
there are 3 types of class inheritance
1. single inheritance
2. multiple inheritance
3. multilevel inheritance
 """

#multiple inheritance
# class job:
#     name = "Ankur"
#     company = "EXL"

#     def job_msg(self, title):
#         self.title = title
#         print(f"Emplyee name is {self.name} and he works as {self.title} in {self.company}")

# class business:
#     name = "Ankur"        
#     business = "Verma Industries"
#     position = "Chair Person"

#     def business_msg(self):
#         print(f"Mr. {self.name} is the {self.position} in {self.business}")

# class worklife(job,business):
#     def worklife_msg(self):
#         # self.title
#         print(f"{self.name} is working as {ankur_job.title} in {self.company} and also acting as the {self.position} in {self.business}\nThats life, Enjoy!")

# ankur_job = job()
# ankur_job.title = "AVP"
# ankur_buss = business()
# ankur_worklife = worklife()

# ankur_worklife.job_msg(ankur_job.title)
# ankur_worklife.business_msg()
# ankur_worklife.worklife_msg()
# print(ankur_job.title)

#multilevel inheritance
class employee:
    a = 1

class engineer(employee):
    b = 1

class manager(engineer):
    c = 1

o = manager()

print(o.a,o.b,o.c)
