# def array_create(n):
#     cust_array = []
#     i = 1
#     while i <= n:
#         cust_array.append(i)
#         i += 1
#     return cust_array

# n = 100000
# A = array_create(n)
# print(A)

def solution(A):
    A_int = [int(x) for x in A]
    A_int.sort()
    # pop_num = A.pop(95555)
    # print(f"pop number is {pop_num}")
    # A_len = len(A)
    i = 1
    while i <= len(A_int):
        if i != A_int[i-1]:
            # print(f"missing integer is : {i} which is matching with pop number {pop_num}")
            return i
        else:
            i += 1


A = [3,5]
print(solution(A))