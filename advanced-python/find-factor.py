def solution(N):
    factor_ls = []
    for i in range(1,(N // 2)+1):
        if N % i == 0:
            # print(i)
            factor_ls.append(i)
    factor_ls.append(N)
    print(factor_ls)
    return len(factor_ls)


# import math

# def solution(N):
#     factor_ls = []
#     for i in range(1, int(math.sqrt(N)) + 1):
#         if N % i == 0:
#             factor_ls.append(i)
#             if i != N // i:
#                 factor_ls.append(N // i)
#     return len(factor_ls)

# N = 55
# 55,11,5,1 = 4

# N = 24
# #24,12,8,6,4,3,2,1 = 8

N = 89
# 89, 1 = 2

# N = 214748364

print(solution(N))