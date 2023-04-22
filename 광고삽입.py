from collections import defaultdict
def secondTotime(second):
    h = str(second//3600)
    m = str((second%3600)//60)
    s = str((second%3600)%60)
    if len(h) < 2:
        h = "0"+h
    if len(m) < 2:
        m = "0" + m
    if len(s) < 2:
        s = "0" +s
    return h +":"+m+":"+s

def timeTosecond(time):
    hms = time.split(":")
    second = int(hms[0])*3600 + int(hms[1])*60 + int(hms[2])
    return second
                    
def solution(play_time, adv_time, logs):
    answer = ''
    start = []
    end = []
    adv_second = timeTosecond(adv_time)

    result = defaultdict(int)

    if timeTosecond(play_time) == timeTosecond(adv_time):
        answer = '00:00:00'
    else:
        for i in range(len(logs)):
            temp = logs[i].split("-")
            start.append(timeTosecond(temp[0]))
            end.append(timeTosecond(temp[1]))
        for i in range(len(logs)):
            currentstart = start[i]
            currentend = currentstart + adv_second
            
            if currentend > timeTosecond(play_time):
                continue
            for j in range(len(logs)):
                if end[j] < currentstart or start[j] > currentend:
                    continue
                if start[j] == currentstart:
                    if end[j] >= currentend:
                        result[currentstart] += adv_second
                    elif end[j] < currentend:
                        result[currentstart] += end[j] - start[j]
                elif start[j] > currentstart:
                    if start[j] > currentend:
                        continue
                    if end[j] >= currentend:
                        result[currentstart] += currentend - start[j]
                    elif end[j] < currentend:
                        result[currentstart] += end[j] - start[j]
                elif start[j] < currentstart:
                    if end[j] < currentstart:
                        continue
                    if end[j] >= currentend:
                        result[currentstart] += adv_second
                    elif end[j] < currentend:
                        result[currentstart] += end[j] - currentstart
                        
        answer = secondTotime(sorted(result.items(), key=lambda x: (-x[1], x[0]))[0][0])

    return answer

print(solution("02:03:55","00:14:15", ["01:20:15-01:45:14", "00:40:31-01:00:00", "00:25:50-00:48:29", "01:30:59-01:53:29", "01:37:44-02:02:30"]))