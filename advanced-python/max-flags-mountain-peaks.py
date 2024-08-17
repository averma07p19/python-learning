"""
need to find out max number of flags can be put on the peak of the mountains
1. if 0<P<N-1 and A[P-1]<A[P]>A[P+1], that describes a mountain peak
2. to hoist a flag , distance between mountain peaks should be greater than or equal to |P-Q|
"""

def solution(A):
    flag_num = []
    mountain_peaks = []

    #no. of mountain peaks
    i = 1
    while i <= len(A):
        if i !=1 and i != (len(A)) and A[i-1] > A [i-2] and A[i-1] > A[i]:
            mountain_peaks.append(i-1)
        i += 1
    print(mountain_peaks)

    #no. of flags
    # j = 1
    while j <= len(mountain_peaks):
        if j != mountain_peaks[0] and (mountain_peaks
 







A = [1,5,3,4,3,4,1,2,3,4,6,2]

print(solution(A))

# mountain_peaks = {
#     1 : 5,
#     4 : 6
# }

# mountain_peaks.update({6:3})
# print(mountain_peaks, len(mountain_peaks), mountain_peaks.keys())