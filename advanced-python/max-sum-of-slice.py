"""based on Kadane's Algorithm"""

def solution(A):
    max_sum = A[0]
    print(f"max_sum = {max_sum}")
    current_sum = A[0]
    print(f"current_sum = {current_sum}")
    
    for num in A[1:]:
        current_sum = max(num, current_sum + num)
        print(f"current_sum for A[{A.index(num)}] = {current_sum}")
        max_sum = max(max_sum, current_sum)
        print(f"max_sum for A[{A.index(num)}] = {max_sum}")
    return max_sum

# A = [3,2,6,-1,4,5,-1,2]
A= [3,2,-6,25,-1,4,2]
print(solution(A))