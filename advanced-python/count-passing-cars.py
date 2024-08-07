# def solution(A):
#     i = 1
#     # tot_passing_cars = []
#     passing_cars = 0
#     while i <= len(A):
#         if A[i-1] == 0:
#             passing_cars = passing_cars + A[i:].count(1)
#             # tot_passing_cars.append(passing_cars)
#         i +=1
#     return passing_cars

def solution(A):
    passing_cars = [sum(A[i:]) for i in range(len(A)) if A[i] == 0]
    print(passing_cars)
    return sum(passing_cars)


A = [1,0,1,1,1,0,1,1]

# A = [1,0,1,0,1,1]
print(solution(A))