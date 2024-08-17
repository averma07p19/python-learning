def solution(N,M):
    choco_array = [x for x in range(0,N)]
    # print(choco_array)
    i = 0
    cnt = 0
    while choco_array[i] != -1:
        # print(f"before if i = {i}")
        if choco_array[i] != -1:
            choco_array[i] = -1
            cnt = cnt + 1
            if i + M >= N - 1:
                i = i + M - N
                # print(f"new i = {i}")
            else:
                i = i + M
                # print(f"continued i = {i}")
        else:
            # print(f"total chocolate eaten : {cnt}")
            return cnt



# def solution(N, M):
#     choco_array = [False] * N  # Simplified to a boolean list
#     i = 0
#     cnt = 0
#     while not choco_array[i]:
#         choco_array[i] = True  # Mark as eaten
#         cnt += 1
#         i = (i + M) % N  # Correctly wrap around using modulo
#     return cnt

# import math

# def solution(N, M):
#     return N // math.gcd(N, M)

N = 2000
"""

0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19
*   *   *   *   *   *      *     *     *     *
"""

M = 3
print(solution(N,M))