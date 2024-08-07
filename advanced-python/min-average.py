def solution(A):
    N = len(A)
    if N == 2:
        return 0


    prefix_sum = [0] * (N + 1)
    for i in range(1, N + 1):
        prefix_sum[i] = prefix_sum[i - 1] + A[i - 1]

    min_avg = float('inf')
    min_pos = 0

    for P in range(N - 1):
        for Q in range(P + 1, N):
            current_sum = prefix_sum[Q + 1] - prefix_sum[P]
            current_len = Q - P + 1
            current_avg = current_sum / current_len
            if current_avg < min_avg:
                min_avg = current_avg
                min_pos = P

    return min_pos
 

A = [4, 2, 2, 5, 1, 5, 8]
print(solution(A))