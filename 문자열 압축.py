def solution(s):
    answer = 0
    result = []
    check = []
    result.append(len(s))
    for i in range(1, len(s)):
        eachlen = len(s)
        cnt = 1
        for j in range(0, len(s), i):
            check.append(s[j:j+i])
            if len(check) > 1:
                flag = isright(check,i)
                if flag:
                    cnt += 1
                else:
                    if cnt > 1:
                            eachlen -= (cnt*len(check[-2]))
                            eachlen += (len(str(cnt))+len(check[-2])) 
                    temp = check[-1]
                    check.clear()
                    check.append(temp)
                    cnt = 1
        
        if flag:
            if cnt > 1:
                eachlen -= (cnt*len(check[-2]))
                eachlen += (len(str(cnt))+len(check[-2])) 
        result.append(eachlen)
        check.clear()
    answer = min(result)
    return answer

def isright(check, i):
    if check[-2] == check[-1]:
        return True
    else:
        return False
