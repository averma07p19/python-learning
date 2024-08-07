def solution(A,B,K):
    if A > K and A%K != 0:
        new_start = A + K - A%K
    elif A < K: 
        new_start = K
    else:
        new_start = A
        
    # remain_s = A % K
    # print(remain_s)
    remain_e = B % K
    print(remain_e)
    # new_start = A - remain_s
    print(new_start)
    new_end = B - remain_e
    # print(new_end)
    # new_list = [ x for x in range()]
    # while new_start <= new_end:
        # new_start = new_start + K
    num_div = (new_end - new_start) / K + 1
    print(num_div)
    return num_div

print(solution(0,111111111111111111,577))


