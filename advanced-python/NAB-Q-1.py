"""
there is an array A of N integers sorted in on-decreasing order. In one move, you can either remove
and integer form A or insert an integer before or after any element of A.
The goal is to achieve an array in which all X that are present in the array occur exactly X times.
For example, given A = [1,1,3,4,4,4], value 1 occurs twice, value 3 occurs once
and value 4 occurs three times. You can remove one occurrence each of both 1 and 3, and insert one occurrence 4,
resulting in the array [1,4,4,4,4]. In this array, every element X occurs exactly X times?

Write a function:
def solution(A)
    
that, given an array A, returns the minimum number of moves after which every value X in the array occurs exactly X times.
Note that it is permissible to remove some values entirely, if appropriate.

Examples:
1. Given A = [1,1,3,4,4,4], you runction should return 3
2. Given A = [1,2,2,2,5,5,5,8], you function should return 4. you can delete the 8 and one occurrence of 2, 
and insert 5 twice, resulting in an empty array.

Write an efficient algorithm for the following assumptions:
1. N is an integer within the range [1.....100,000]
2. each element of array A in an integer within the range [1.....100,000,000]
3. elements of array A are sorted in non-decreasing order 
"""


def solution(A):
    sorted_A = list(set(A))
    sorted_A.sort()
    cnt_sum = []
    for i in sorted_A:
        cnt = A.count(i)
        print(i)
        print(cnt)
        if cnt > i:
            moves = cnt - i
            print(f"delete moves : {moves}")
            cnt_sum.append(moves)
        if cnt >= i / 2 and cnt < i:
            moves = i - cnt
            print(f"add moves : {moves}")
            cnt_sum.append(moves)
        if cnt < i / 2:
            moves = cnt
            print(f"delete moves : {moves}")
            cnt_sum.append(moves)
    return sum(cnt_sum)
            
            
# print(solution([1, 1, 3, 4, 4, 4]))  # Output: 3


# Test cases
# print(solution([1, 1, 3, 4, 4, 4]))  # Output: 3
# print(solution([1, 2, 2, 2, 5, 5, 5, 8]))  # Output: 4
# print(solution([1, 1, 1, 1]))  # Output: 3
# print(solution([1, 2, 2, 3, 3, 3]))  # Output: 3


# Test cases
# print(solution([1, 1, 3, 4, 4, 4]))  # Output: 3
# print(solution([1, 2, 2, 2, 5, 5, 5, 8]))  # Output: 4
print(solution([10,10,10]))