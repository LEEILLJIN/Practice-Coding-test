#20221220

#내 코드
def solution(s):
    # temp = [for 0 in range(26)]
    answer = []
    alpabet = {'a':-1,'b':-1,'c':-1,'d':-1,'e':-1,'f':-1,'g':-1,'h':-1,'i':-1,'j':-1,'k':-1,'l':-1,'m':-1,'n':-1,'o':-1,'p':-1,'q':-1,'r':-1,'s':-1,'t':-1,'u':-1,'v':-1,'w':-1,'x':-1,'y':-1,'z':-1}
    for i in range(len(s)):
        if alpabet[s[i]] == -1:
            answer.append(alpabet[s[i]])
            alpabet[s[i]] = i
        else :
            answer.append(i - alpabet[s[i]])
            alpabet[s[i]] = i

    return answer

#같은 로직의 더 단순한 다른사람 코드

# def solution(s):
#     answer = []
#     dic = dict()
#     for i in range(len(s)):
#         if s[i] not in dic:
#             answer.append(-1)
#         else:
#             answer.append(i - dic[s[i]])
#         dic[s[i]] = i

#     return answer