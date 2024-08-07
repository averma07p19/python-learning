def solution(A):
    n = len(A)
    if n > 200_000 or max(A) > n:
        return -1 
    moves = 0

    counts = [0] * (n + 1)
    for num in A:
        if counts[num] == 0:
            counts[num] = 1  
        else:
            distance = 0

            while num - distance > 0 and counts[num - distance] > 0:
                distance += 1

            if num - distance > 0:
                counts[num - distance] = 1  
                moves += distance  
            else:
                
                i = num + 1
                while counts[i] > 0:
                    i += 1
                counts[i] = 1  
                moves += i - num  
    return moves


# import heapq
# from collections import defaultdict, deque

# def solution(A):
#     n = len(A)
    
#     if n > 200_000 or max(A) > n:
#         return -1
    
#     moves = 0
#     counts = defaultdict(int)
#     for num in A:
#         counts[num] += 1
    
#     # Priority queue to keep track of available slots
#     available_positions = []
#     for i in range(1, n + 1):
#         if i not in counts:
#             heapq.heappush(available_positions, i)
    
#     for num, count in sorted(counts.items()):
#         if count > num:
#             moves += count - num
#         elif count < num:
#             # Insert the missing occurrences
#             while count < num and available_positions:
#                 pos = heapq.heappop(available_positions)
#                 if pos > num:
#                     break
#                 moves += 1
#                 count += 1
#             # If there are still missing occurrences, calculate the moves for larger positions
#             moves += num - count
    
#     return moves

# Test cases
# print(solution([1, 1, 3, 4, 4, 4]))  # Output: 3
# print(solution([1, 2, 2, 2, 5, 5, 5, 8]))  # Output: 4
# print(solution([1, 1, 1, 1]))  # Output: 3
# print(solution([1, 2, 2, 3, 3, 3]))  # Output: 3



# A = [6,2,3,5,6,3]
# A = [1,2,1]
A = [2,1,4,4]

print(solution(A*5000))