def solution(cap, n, deliveries, pickups):
    answer = 0
    
    while sum(deliveries) + sum(pickups) > 0:
        # Dbox = cap
        # Pbox = 0
        print("sum : ",sum(deliveries) + sum(pickups))
        for i in range(n-1, -1, -1):
            Dbox = cap
            Pbox = 0
            #여기서 갱신을 해줘야 하는거 같은데 아닌가?
            if deliveries[i] > 0 or pickups[i] >0:
                answer += (i+1)
                print("i+1", i+1)
                for j in range(i, -1, -1):
                    print(deliveries, pickups)
                    if Dbox == 0 and Pbox == cap:
                        break
                    if Dbox > 0:
                        if Dbox >= deliveries[j]:
                            Dbox -= deliveries[j]
                            deliveries[j]=0
                    if pickups[j] > 0:
                        if pickups[j] > cap - Pbox:
                            Pbox = cap
                            pickups[j] = cap - Pbox 
                        else:
                            Pbox += pickups[j]
                            pickups[j] = 0 
                answer += (i+1)
    return answer

print(solution(4, 5, [1, 0, 3, 1, 2], [0, 3, 0, 4, 0]))