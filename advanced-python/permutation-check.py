

def solution(A):
    dedup_A = list(set(A))
    dedup_A.sort()
    print(dedup_A)
    i = 1
    if len(dedup_A) != len(A):
        print("array has duplicates")
        return 0
    else:
        while i <= len(A):
            if dedup_A[i-1] != i:
                return 0
            else:
                i += 1
        return 1

A = [4,1,3]

print(solution(A))