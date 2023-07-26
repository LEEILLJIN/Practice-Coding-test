#하나의 곡괭이는 5번 광물을 캘 수 있음
#광물을 다 캐거나 곡괭이를 다 쓰면 종료
#광물은 주어진 순서대로만 캘 수 있음
#사용할 수 있는 곡괭이 중 아무거나 하나를 선택해 광물을 캔다.
# picks 배열의 0 은 diamond, 1은 iron, 2는 stone
# dia, dia, stone, stone, stone, dia, dia, dia
# 1, 2, 0
# 1 1 1 1 1 5 5 5
# 5 5 1 1 1 1 1 1
#picks를 5개씩 잘라서 다이아몬드, 철, 돌 각각의 곡괭이로 캔 경우에 피로도를 계산하고 최솟값으로 진행
def solution(picks, minerals):
    result = 0
    mineIndex = 0
    checkminerals = [0 for i in range(len(minerals))]
    while True:
        print("ddddd")
        if sum(picks) == 0 or mineIndex > len(minerals)-1:
            break
        else:
            for i in range(0, len(minerals), 5):
                print("i", i)
                flag = False
                temp= [["diamond",0],["iron",0],["stone",0]]
                for j in range(i,i+5):
                    print(j)
                    if j > len(minerals)-1:
                        flag = True
                        mineIndex = j
                        break
                    else:
                        if minerals[j] == "diamond":
                            temp[0][1] += 1
                            temp[1][1] += 5
                            temp[2][1] += 25
                        elif minerals[j] == "iron":
                            temp[0][1] += 1
                            temp[1][1] += 1
                            temp[2][1] += 5
                        else:
                            temp[0][1] += 1
                            temp[1][1] += 1
                            temp[2][1] += 1
                if flag:
                    temp.sort(key = lambda x : x[1])
                    print(temp)
                    for k in temp:
                        if k[0] == "diamond":
                            if picks[0]>0:
                                picks[0] -= 1
                                result += k[1]
                                break
                            else:
                                continue
                        elif k[0] == "iron":
                            if picks[1]>0:
                                picks[1] -= 1
                                result += k[1]
                                break
                            else:
                                continue
                        elif k[0] == "stone":
                            if picks[2] > 0:
                                picks[2] -= 1
                                result += k[1]
                                break
                            else:
                                continue
                    break
                else:
                    temp.sort(key = lambda x : x[1])
                    print(temp)
                    for k in temp:
                        if k[0] == "diamond":
                            if picks[0]>0:
                                picks[0] -= 1
                                result += k[1]
                                break
                            else:
                                continue
                        elif k[0] == "iron":
                            if picks[1]>0:
                                picks[1] -= 1
                                result += k[1]
                                break
                            else:
                                continue
                        elif k[0] == "stone":
                            if picks[2] > 0:
                                picks[2] -= 1
                                result += k[1]
                                break
                            else:
                                continue
                            
    return result
print(solution([1,3,2],["diamond", "diamond", "diamond", "iron", "iron", "diamond", "iron", "stone"]))