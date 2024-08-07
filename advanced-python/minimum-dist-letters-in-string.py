# def soluton(P,Q):
#     PQ = list((P + Q))
#     cnt_l = []
#     for i in list(set(PQ)):
#         cnt_l.append(PQ.count(i))
#     if max(cnt_l) >= len(PQ) / 2:
#         print(f"minimul distinct letters would be : 1")
#         return 1
#     more_than_avg = [x for x in cnt_l if x >= len(PQ) // 4]
#     if len(more_than_avg) >= 2:  
#         print(f"minimul distinct letters would be : 2")
#         return 2
#     else:
        #max of sum of elements equal to len

def solution(P,Q):
    if P == Q:
        return len(P)
    else:
        PQ = list(P+Q)
        print(PQ)
        cnt_l = []
        len_of_string = []
        for i in list(set(PQ)):
            cnt_l.append(PQ.count(i))
        cnt_l.sort()
        print(cnt_l)
        i = 1
        while i <= len(cnt_l):
            len_of_string.append(cnt_l[len(cnt_l)-i])
            print(len_of_string)
            # cnt_l.replace(max(cnt_l),0)
            # print(cnt_l)
            if sum(len_of_string) - len(P) >= 0:
                return len(len_of_string)
            i += 1
        

# a = [0,1,1,1,1,1,0,0]
# print(len(a), sum(a))



# P = "abc"
# Q = "bcd"

P = "amz"
Q = "amz"
# P = "bacad"
# Q = "abada"
print(solution(P,Q))

