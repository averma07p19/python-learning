def solution(A):
    n = len(A)
    size = 0
    value = None
    
    # Step 1: Find a candidate for leader using Boyer-Moore majority vote algorithm
    for i in range(n):
        if size == 0:
            size += 1
            value = A[i]
            print(f"value = {value}")
            print(f"size = {size}")
        else:
            if value == A[i]:
                size += 1
            else:
                size -= 1
    
    candidate = -1
    if size > 0:
        candidate = value
    
    # Step 2: Verify if the candidate is a leader
    leader_count = 0
    for i in range(n):
        if A[i] == candidate:
            leader_count += 1
    
    if leader_count <= n // 2:
        return 0
    
    leader = candidate
    equi_leader_count = 0
    left_leader_count = 0
    
    # Step 3: Count the equi-leaders
    for i in range(n):
        if A[i] == leader:
            left_leader_count += 1
        
        if left_leader_count > (i + 1) // 2 and (leader_count - left_leader_count) > (n - i - 1) // 2:
            equi_leader_count += 1
    
    return equi_leader_count

# Test cases
print(solution([4, 3, 4, 4, 4, 2]))  # Output: 2
# print(solution([1, 2, 3, 4, 5]))     # Output: 0
# print(solution([1, 2, 2, 1, 2, 2]))  # Output: 3
