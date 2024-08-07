# def solution(A):
#     # i = 1
#     sorted_A = list(set(A))
#     sorted_A.sort()
#     for i in sorted_A:
#         cnt = A.count(i)
#         print(f"cnt of {i} = {cnt}", len(A)/2)
#         if cnt > len(A)/2:
#             print(f"cnt of {i} = {cnt}", len(A)/2)
#             return A.index(i)
        
#     return -1


def solution(A):
    i = 1
    count_of_leader = 0
    while i < len(A):
        if i == 1:
            first_part = [A[i-1]]
        else:
            first_part = A[:i]
        print(f"first_part = {first_part}")
        second_part = A[i:]
        print(f"second_part = {second_part}")
        for x in set(first_part):
            if first_part.count(x) > len(first_part)/2:
                L1 = x
                print(f"L1 = {L1}", first_part.index(L1))
                for y in set(second_part):
                    if second_part.count(y) > len(second_part)/2:
                        L2 = y
                        print(f"L2 = {L2}", second_part.index(L2))
                        if L1 == L2:
                            count_of_leader = count_of_leader + 1
                            print(f"count_of_leaders = {count_of_leader}")
        i += 1
    if count_of_leader != 0:
        return count_of_leader
    else:
        return 0
    
# A = [4,3,4,4,4,2]
A = [1, 2, 2, 1, 2, 2]
print(solution(A))

