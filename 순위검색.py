import re
def solution(info, query):
    answer = []
    lan = ['-','cpp', 'java', 'python']
    jobG = ['-','backend', 'frontend']
    carr = ['-', 'junior', 'senior']
    food = ['-', 'chicken', 'pizza']
    for i in range(len(query)):
        # re.split('[+|-|*]', expression)
        temp
        print(query[i].split("and"))
    #[java, backend, junior, pizza, 100]
    #for k in range(len(query)):
        #querytemp = query[k].split(" and ")
        #for i in range(len(info)):
        #   temp = info[i].split(" ")
        #   for j in range(len(temp)):
        #       if temp[j] == querytemp[j]
    return answer
solution(["java backend junior pizza 150","python frontend senior chicken 210","python frontend senior chicken 150","cpp backend senior pizza 260","java backend junior chicken 80","python backend senior chicken 50"],["java and backend and junior and pizza 100","python and frontend and senior and chicken 200","cpp and - and senior and pizza 250","- and backend and senior and - 150","- and - and - and chicken 100","- and - and - and - 150"] )