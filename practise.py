# Ex - 1
# a = input("May I know you Full Name please\n")
# print(f"Very good afternoon Mr. {a.title()}")

# Ex - 2
# from datetime import date
# import os
# name = input("May I know your Full Name please\n")
# print(f"Very good afternoon Mr. {name.title()}")
# dob = int(input("Please enter your Date of Birth in DDMMYYYY format\n"))
# print(dob)
# letter = f"""Dear {name.title()}\n As today is {date.today()}\n so you are eligible and seleted for our colloege"""
# print(letter)

# Ex - 3
# mystr = "what a wonderful  day"
# mystr = mystr.replace("  ","      ")
# print(mystr)

# Ex - 4
# file_name = "cards_rds_dod_202403"
# l1 = file_name.split("_")
# print(l1)
# cnt = len(l1) 
# print(cnt)
# file_suffix = int(l1[len(l1) -1])
# # num_chk = file_suffix.isint()
# print(file_suffix, type(file_suffix))

# Ex - 4.1
# file_name = "cards_rds_dod_202403"
file_name = input("enter the file name :\n")
l1 = file_name.split("_")
print(l1)
l1.reverse()
print(l1)
file_suffix = l1[0]
num_chk = file_suffix.isdigit()
print(file_suffix, num_chk, type(file_suffix))