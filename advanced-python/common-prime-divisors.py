# def solution(A,B):
#     i = 1
#     com_divs = [False] * len(A)
#     while i <= len(A):
#         comm_divs_A = [A[i-1]]
#         comm_divs_B = [B[i-1]]
#         j = 2
#         k = 2
#         while j <= A[i-1] / 2:
#             if A[i-1] % j == 0:
#                 # comm_div_A[i-1] = j
#                 comm_divs_A.append(j)
#             j += 1
#         while k <= B[i-1] / 2:                
#             if B[i-1] % k == 0:
#                 comm_divs_B.append(k)
#             k += 1
#         if comm_divs_A == comm_divs_B:
#             com_divs[i-1] = True
#         print(comm_divs_A)
#         print(comm_divs_B)
#         i += 1
#     print(com_divs)



# A = [15,10,3]
# B = [15,10,3]

# # B = [75,30,5]

# # if A != B:
# #     print("not matching")
# # else:
# #     print("matcing")

# print(solution(A,B))


import math

def solution(N):
    factor_ls = []
    for i in range(1, int(math.sqrt(N)) + 1):
        if N % i == 0:
            factor_ls.append(i)
            if i != N // i:
                factor_ls.append(N // i)
    return len(factor_ls)

# N = 55
# 55,11,5,1 = 4

N = 24
#24,12,8,6,4,3,2,1 = 8

# N = 89
# 89, 1 = 2

# N = 214748364

print(solution(N))