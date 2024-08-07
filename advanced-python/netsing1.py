def solution(A):
    i = 1
    if len(A) % 2 == 0:
        total_pair = len(A) / 2
        while i <= total_pair:
            A = A.replace("()","")
            print(A)
            i += 1
        if len(A) != 0:
            print(f"string is not nested, remaining string is {A}")
            return 0
        else:
            print(f"string is nested, remaining string is : {len(A)}")
            return 1
    else:
        print(f"odd number string")
        return 0

# def solution(A):
#     i = 1
#     if len(A) % 2 == 0:
#         new_str = (x for x in A if x != "()")
#         print(new_str)
#     else:
#         print(f"odd number string")
#         return 0
    
A = "(((()()))))("
print(solution(A))