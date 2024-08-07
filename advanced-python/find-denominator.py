def solution(A):
    # i = 1
    sorted_A = list(set(A))
    sorted_A.sort()
    for i in sorted_A:
        cnt = A.count(i)
        print(f"cnt of {i} = {cnt}", len(A)/2)
        if cnt > len(A)/2:
            print(f"cnt of {i} = {cnt}", len(A)/2)
            return A.index(i)
        
    return -1

A = [0,1,2,1,1,0,4,1,1,1,4,1,3,5,4,1,2,2,1,1,1,1,1,1,1,1]     
# A = [3, 4, 3, 2, 3, -1, 3, 3]   
print(solution(A))