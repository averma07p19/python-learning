def solution(A):
    i = 1
    # j = 1
    # l = 1
    while i <= len(A)-2:
        j = 1
        while j + i + 1 <= len(A) -1:
            
            k = 1
            while k + j + 1 <= len(A):
                max_triplet = 





A = [3,2,6,-1,4,5,-1,2]
print(solution(A))