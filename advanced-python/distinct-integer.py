# def solution(A):
#     sorted_A = list(set(A))
#     sorted_A.sort()
#     dist_val = []
#     for i in sorted_A:
#         if A.count(i) < 2:
#             print(i)
#             dist_val.append(i)
#             return dist_val

def solution(A):
    dist_cnt = len(list(set(A)))
    return dist_cnt

A = [-1,-1,0,3,2,4,5,4,-100,-100,-100]
print(solution(A))
