import string
dictionary = {}
indexNum = 0
def solution(msg):
    global indexNum
    global dictionary
    answer = []
    alpabet = string.ascii_uppercase
    indexNum = len(alpabet)
    for i in range(indexNum):
        dictionary[alpabet[i]] = i+1
        
    for i in range(len(msg)):
        answer.append(check(msg, i, len(msg)))
        print(msg[i], answer)
        print(dictionary)
    return answer

def check(msg, i, length):
    global indexNum
    global dictionary
    cnt = 1
    output = 0
    while i+cnt <= length:
        if msg[i:i+cnt] not in list(dictionary.keys()):
            indexNum += 1
            dictionary[msg[i:i+cnt]] = indexNum
            break
        else:
            output = dictionary[msg[i:i+cnt]]
            cnt += 1
    return output

print(solution('KAKAO'))