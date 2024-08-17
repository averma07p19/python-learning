def solution(A):
    sorted_A = list(set(A))
    # print(f"sorted_A :\n{sorted_A}")
    sorted_A.sort()
    # print(f"reversed sorted_A :\n{sorted_A.reverse()}")
    # while i <= len(sorted_A):
    #     divisors = [x for x in ]
    cnt_non_divisibles = []
    i = 1
    while i <= len(A):
        cnt_non_div = [x for x in A if A[i-1] % x != 0]
        print(f"cnt_non_div :\n{cnt_non_div}")
        # cnt_greater = [x for x in A if x > i]
        # print(f"cnt_greater :\n{cnt_greater}")
        # cnt_non_divisibles.append(len(cnt_non_div) + len(cnt_greater))
        cnt_non_divisibles.append(len(cnt_non_div))
        i += 1

        

    return cnt_non_divisibles

A = [3,1,2,3,6]*50
print(solution(A))
