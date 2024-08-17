def solution(N,P,Q):
    if len(P) == len(Q):
        i = 1
        while i <= len(P):
            if (P[i-1] == 2) or (P[i-1] % 2 == 0) or Q[i-1] == 2 or Q[i-1] % 2 == 0:




    else:
        print(f"size of P and Q is different, input again")