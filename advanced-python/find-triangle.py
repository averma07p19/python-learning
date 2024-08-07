

def solution(A):
    i = 1
    # j = 1
    # k = 1
    # P = 0
    # Q = 0
    # R = 0
    while i <= len(A):
        P = A[i-1]
        # print(f"P = {P}")
        j = 1
        while j + i <= len(A):
            Q = A[j + i - 1]
            # print(f"Q = {Q}")
            k = 1
            while k + j + i <= len(A):
                R = A[k + j + i - 1]
                # print(f"R = {R}")
                if (P+Q > R) and (Q+R>P) and (R+P>Q):
                    print(f"P = {P}\nQ = {Q}\nR = {R}")
                    return 1
                k += 1
            j += 1
        i += 1
    return 0

A = [10,2,5,1,8,25,3,7,18,9,10,5,33]
# A = [10,2,5,1,8,20]

print(solution(A))