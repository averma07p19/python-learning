def show_list():
    num_list = input("enter the numbers here separated by comma!\n")
    ls = num_list.split(",")
    # print(ls, type(ls))
    if (n := len(ls)) > 3:
        # print(f"list {num_list} long and has {len(num_list)} elements")
        print(f"list {ls} long and has {len(n)} elements")


show_list()

"""
match funtions
merging of two or more list
import methods from typing like List, Tuple, Union
 """
