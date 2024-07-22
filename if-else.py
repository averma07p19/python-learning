# a = input("enter any numbers seprated by comma\n")
# print(a)
# a_list = (a.split(","))
# print(a_list)
# b = [int(x) for x in a_list if int(x)%2==0]
# print(b)
# b.sort()
# print(b)
# print(max(a_list), type(a_list), type(a_list[0:1]))

# l1 = [88,17, 19, 1, 9, 163, 83]
# l1.sort()
# print(l1)

# Ex. 1

# marks = input("enter marks of all the subjects separated by comma :\n")
# marks_list = marks.split(",")
# pass_fail_status = ["Pass" if int(x) >= 33 else "Fail" for x in marks_list]
# print(pass_fail_status)
# pass_counter = 0
# for x in pass_fail_status:
#     if 'Pass' in pass_fail_status:
#         pass_counter = pass_counter+1
# if pass_counter >= 3:
#     print("you passed the exam")

# a1 = [1,4,1,"yo"]
# b1 = [5,"pass",-10,"fail"]
# c1 = a1 + b1
# print(c1)

#EX : seperate numeric and character elemets from a user given list
a = [1, "a", 5,6,"ankur"]
print(a, a[1], type(a[1]), type(a[2]))
i=1
int_l = []
char_l = []
while i <= len(a):
    element = str(a[i-1]).isdigit()
    # num_check = element.isdigit()
    if element:
        int_l.append(a[i-1])
        i = i+1
    else:
        char_l.append(a[i-1])
        i = i+1
print(f"All numeric elemts are in int_1 : {int_l}")
print(f"All numeric elemts are in char_l : {char_l}")



