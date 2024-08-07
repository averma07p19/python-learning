A = [-1000,1000]
# print(sum(a))

def solution(A):
    i = 1
    diff_arr = abs(sum(A[0:i]) - sum(A[i:]))
    print(diff_arr)
    # print(diff_arr)
    while i <= len(A):
        if abs(sum(A[0:i]) - sum(A[i:])) < diff_arr:
            diff_arr = abs(sum(A[0:i]) - sum(A[i:]))
        i += 1
    return diff_arr
    

print(solution(A))
    
