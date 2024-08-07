import math

def solution(X,Y,D):
    jumps = math.ceil((Y - X) / D)
    return jumps



X = 3
Y = 31
D = 10

print(solution(X,Y,D))