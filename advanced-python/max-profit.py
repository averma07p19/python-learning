def solution(A) :
    i = 1
    max_profit_in_tenure = []
    while i < len(A):
        # transaction_day_price = A[i-1]
        profit = [x - A[i-1] for x in A[i:] if x > A[i-1]]
        if len(profit) != 0:
            print(profit, max(profit))
            max_profit_in_tenure.append(max(profit))
            print(max_profit_in_tenure)
        i += 1
    
    if len(max_profit_in_tenure) != 0:
        return max(max_profit_in_tenure)
    else:
        return 0


# def solution(A):
#     if not A:
#         return 0
    
#     min_price = A[0]
#     max_profit = 0
    
#     for price in A[1:]:
#         profit = price - min_price
#         max_profit = max(max_profit, profit)
#         min_price = min(min_price, price)
    
#     return max_profit

# # Test cases
# print(solution([7, 1, 5, 3, 6, 4]))  # Output: 5
# print(solution([7, 6, 4, 3, 1]))     # Output: 0
# print(solution([1, 2, 3, 4, 5]))     # Output: 4
# print(solution([]))                  # Output: 0
# print(solution([3, 3, 3, 3]))        # Output: 0







# A = [23171,21011,21123,21366,21013,21367]
# # print(max(A))
# print(solution(A))