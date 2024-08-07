
def solution(A):
    set_A = list(set(A))
    odd_elements = []
    for i in set_A:
        if A.count(i) % 2 != 0:
             odd_elements.append(i)
    return int(odd_elements[0])
    


A = [9,3,9,3,9,7,9]
print(f"odd element in array is : {solution(A)}")