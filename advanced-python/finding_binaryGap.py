# a = int(input("enter the integer : "))
# bin_a = bin(a)[2:]
# print(bin_a)
# bin_a_list = []
# bin_list = bin_a.split("1")
# print(bin_list)
# bin_gap = []
# if bin_list[len(bin_list)] != '':
#         bin_list.pop(len(bin_list)+1)
# if bin_list[0] != "":
#         bin_list.pop(0)        
# for i in bin_list:
#     if i != 1 and i != "":
#         cnt_zero = len(str(bin_list[i]))
#         bin_gap.append(cnt_zero)
#         max(bin_gap)        

# print(f"{bin_gap}")        
# print(f"maximum binary gap is : {max(bin_gap)}")        



# a = 11
# bin_a = bin(a)[2:]
# list_a = []



a = "0000111100110000011000"
b = a.strip("0").split("1")
max_bin_gap = max(len(x) for x in b)
print(b, max_bin_gap)