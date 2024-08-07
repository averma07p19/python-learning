def solution(A):
    A.sort()
    print(A)
    if A[0]*A[1]*A[len(A)-1] > A[len(A)-1]*A[len(A)-2]*A[len(A)-3]:
        return A[0]*A[1]*A[len(A)-1]
    else: 
        return A[len(A)-1]*A[len(A)-2]*A[len(A)-3]




# A = [-6,7,2,9,0,-2,1,-1,5]*100
A = [-5, 5, -5, 4]
print(solution(A))