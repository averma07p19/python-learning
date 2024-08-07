def solution(S,P,Q):
    impact_dict = {
        "A" : 1,
        "C" : 2,
        "G" : 3,
        "T" : 4
    }
    i = 1
    min_im = []
    while i <= len(P):
        im_A = [impact_dict[x] for x in S]
        # print(im_A)
        min_im.append(min(im_A[P[i-1]:Q[i-1]+1]))
        i += 1
    return min_im



"""
DNA Sequece : A C G T with impact factor 1, 2, 3, 4
"""
# S = "GGGGG"
# S = "CGATCCTGA"
# =  123456789
# =  231422431
S = "GGGGGGGGGGGGGGGGGTTGGGGGGGGGGGGGGGGGGGGGGGGGGAGGGGGGGGGGGGGGG"
P = [0,30,20]
Q = [1000,38,45]

print(solution(S,P,Q))