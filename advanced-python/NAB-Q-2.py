# def solution(S):
#     N = len(S)
#     occupied_positions = set()
#     success_count = 0

#     for i in range(N):
#         if S[i] == '>':
#             if i + 1 < N and (i + 1) not in occupied_positions:
#                 occupied_positions.add(i + 1)
#                 success_count += 1
#         elif S[i] == '<':
#             if i - 1 >= 0 and (i - 1) not in occupied_positions:
#                 occupied_positions.add(i - 1)
#                 success_count += 1
#         elif S[i] == '*':
#             if i not in occupied_positions:
#                 occupied_positions.add(i)
#                 success_count += 1
#         elif S[i] == 'v':
#             if i not in occupied_positions:
#                 occupied_positions.add(i)
#                 success_count += 1

#     return success_count


def solution(S):
    successful_moves = 0
    N = len(S)
    not_occupied = [False] * N  
    for i in range(N):
        move = S[i] 
        target = -1  
        if move == '<':
            target = i - 1
        elif move == '>':
            target = i + 1
        if target < 0 or target >= N:
            successful_moves += 1
            not_occupied[i] = True
        elif 0 <= target < N:
            if not_occupied[target]:
                successful_moves += 1
                not_occupied[i] = True
    return successful_moves

print(solution("<<^<v>>"))


print(solution("*><v"))  # Output: 2
print(solution("<<^<v>"))  # Output: 6
print(solution("><><"))  # Output: 0