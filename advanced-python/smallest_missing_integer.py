def solution(A):
    new_A = set(x for x in A if x > 0)
    # print(new_A)
    smallest_val = 1
    while smallest_val in new_A:
        smallest_val +=1
    return smallest_val

A = [-1,0,1]
print(f"smallest missing integer is : {solution(A)}")