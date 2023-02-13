
def solution(scores):
    answer = 0
    for i in range(len(scores)):
        scores[i].append(sum(scores[i]))
        scores[i].append(i)
    print(scores)
    dellist = []
    scores.sort(reverse=True)
    for i in range(1, len(scores)):
        print(scores, i, len(scores))
        if scores[i-1][1] > scores[i][1]:
            if scores[i][3] == 0:
                answer = -1
                return answer
            else:
                dellist.append(i)
                # scores[i][2] = -1
    cnttemp = 0
    for i in dellist:
        del scores[i-cnttemp]
        cnttemp += 1
    scores.sort(key = lambda x : x[2] , reverse = True)
    grade = 1
    cnt = 1
    scores[0].append(grade)
    for i in range(1, len(scores)):
        if scores[i-1][2] == scores[i][2]:
            scores[i].append(grade)
            cnt += 1 
        else:
            grade += cnt
            cnt = 0
            scores[i].append(grade)
    scores.sort(key = lambda x : x[3])
    answer = scores[0][4]
    print(scores)
    return answer

print(solution([[2,2],[1,4],[3,2],[3,2],[2,1],[1,1]]))