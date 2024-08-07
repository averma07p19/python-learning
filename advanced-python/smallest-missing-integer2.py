def solution(A):
    sorted_A = list(set(A))
    sorted_A.sort()
    positive_A = [x for x in sorted_A if x > 0]
    i = 1
    if len(positive_A) == 0:
        return 1
    else:
        while i <= len(positive_A):
            if positive_A[i-1] != i:
                return i
            else:
                i += 1
        return i
        

A = [1,2,3,4,6,8,5]
print(solution(A))
