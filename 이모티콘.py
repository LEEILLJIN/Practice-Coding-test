from itertools import combinations_with_replacement
from itertools import product
def solution(users, emoticons):
    answer = []
    DiscList = [10, 20, 30, 40]
    userDiscList = [users[i][0] for i in range(len(users))]
    userDiscmin = min(userDiscList)
    checkDiscindex = 0
    checkDiscList = []
    for i in range(len(DiscList)):
        if userDiscmin <= DiscList[i]:
            checkDiscindex = i
            break
    userDiscList = [users[i][0] for i in range(len(users))]

    temp = [DiscList[i] for i in range(checkDiscindex, len(DiscList))]
    for i in product(temp, repeat = len(emoticons)):
        checkDiscList.append(i)

    totalprice = 0
    cnt = 0
    maxplus = []
    price = 0

    for i in range(len(checkDiscList)):
        for j in range(len(users)):
            for k in range(len(checkDiscList[i])):#이모티콘 len랑 같음
                if users[j][0] <= checkDiscList[i][k]:
                    #이모티콘 할인율이 유저의 할인 상한선보다 같거나 높으면 유저는 이모티콘 산다.
                    price += emoticons[k] *((100-checkDiscList[i][k])/100)
            if price >= users[j][1]:
                print("price > users[j][1]", price, checkDiscList[i][k], users[j])
                price = 0
                cnt += 1
            totalprice += price
            price = 0
        maxplus.append([cnt, totalprice])
        print(checkDiscList[i], cnt, totalprice)
        cnt = 0 
        totalprice = 0
    maxplus.sort(reverse=True)
    answer.append(maxplus[0][0])
    answer.append(maxplus[0][1])
    print(answer)
    return answer

solution([[40, 10000], [25, 10000]], [7000, 9000])
solution([[40, 2900], [23, 10000], [11, 5200], [5, 5900], [40, 3100], [27, 9200], [32, 6900]], [1300, 1500, 1600, 4900])
# (40, 40, 20, 40) 3 19760.0 ??