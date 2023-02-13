# def solution(cap, n, deliveries, pickups):
#     answer = 0
    
#     while sum(deliveries) + sum(pickups) > 0:
#         # Dbox = cap
#         # Pbox = 0
#         print("sum : ",sum(deliveries) + sum(pickups))
#         for i in range(n-1, -1, -1):
#             Dbox = cap
#             Pbox = 0
#             if sum(deliveries) + sum(pickups) <= 0:
#                 break
#             if deliveries[i] > 0 or pickups[i] >0:
#                 answer += (i+1)
#                 print("i+1", i+1)
#                 for j in range(i, -1, -1):
#                     print(deliveries, pickups)
#                     if sum(deliveries) + sum(pickups) <= 0:
#                         break
#                     if Dbox == 0 and Pbox == cap:
#                         break
#                     if Dbox > 0:
#                         if Dbox >= deliveries[j]:
#                             Dbox -= deliveries[j]
#                             deliveries[j]=0
#                     if pickups[j] > 0:
#                         if pickups[j] > cap - Pbox:
#                             Pbox = cap
#                             pickups[j] = cap - Pbox 
#                         else:
#                             Pbox += pickups[j]
#                             pickups[j] = 0 
#                 answer += (i+1)
#     return answer
def solution(cap, n, deliveries, pickups):
    deliveries = deliveries[::-1]
    pickups = pickups[::-1]
    answer = 0
    
    d = 0
    p = 0
    
    for i in range(n):
        d += deliveries[i]
        p += pickups[i]
        
        while d > 0 or p > 0:
            d -= cap
            p -= cap
            answer += (n - i) * 2

    return answer
    
print(solution(4, 5, [1, 0, 3, 1, 2], [0, 3, 0, 4, 0]))