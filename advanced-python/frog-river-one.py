def solution(X,A):
    positions = set()
    for second in range(len(A)):
        positions.add(A[second])
        if len(positions) == X:
            return second
    return -1


print(solution(6,[1,3,42,4,5,3,2,1]))
print(solution(5,[1,2,3,43,5]))