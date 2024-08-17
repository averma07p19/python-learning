# def solution(N):
#     factor_ls = []
#     for i in range(1,(N // 2)+1):
#         if N % i == 0:
#             # print(i)
#             factor_ls.append(i)
#     factor_ls.append(N)

#     min_perimeter = 2*(factor_ls[0]+factor_ls[len(factor_ls)-1])
#     i = 2
#     if len(factor_ls) // 2 == 0:
#         while i <= len(factor_ls) / 2:
#             min_perimeter = min(min_perimeter, 2*(factor_ls[i-1]+factor_ls[len(factor_ls)-i]))

#             i += 1
#     else:
#         while i <= len(factor_ls) // 2 + 1:
#             min_perimeter = min(min_perimeter, 2*(factor_ls[i-1]+factor_ls[len(factor_ls)-i]))
#             i +=1
#     print(factor_ls)
#     return min_perimeter

def solution(N):
    factor_ls = [x for x in range(2,(N // 2) +1) if N % x == 0]
    print(factor_ls)
    perimeters = [2*(factor_ls[i-1]+factor_ls[len(factor_ls)-i]) for i in range(1,len(factor_ls)+1)]
    print(perimeters)
    # while i <= len(factor_ls) / 2:
    #     min_perimeter = min(min_perimeter, 2*(factor_ls[i-1]+factor_ls[len(factor_ls)-i]))

    return min(perimeters)

N = 3054545345
print(solution(N))