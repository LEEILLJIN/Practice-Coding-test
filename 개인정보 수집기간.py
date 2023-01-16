def solution(today, terms, privacies):
    answer = []
    t_y, t_m, t_d = map(int, today.split("."))
    print(t_y, t_m, t_d)
    termsDic = {}
    for i in terms:
        temp = i.split(" ")
        termsDic[temp[0]] = int(temp[1])
    
    for i in range(len(privacies)):
        temp = privacies[i].split(" ")
        print(temp)
        p_y, p_m, p_d = map(int, temp[0].split("."))
        p_m += termsDic[temp[1]]
        if p_m  > 12:
            p_y += p_m // 12

            p_m -= p_m%12

        p_d -= 1
        
        if p_d == 0:
            p_d = 28
            p_m -= 1

        if p_m == 0:
            p_m = 12
            p_y -= 1

        print(p_y, p_m, p_d)
        if (t_y > p_y) or (t_y == p_y and t_m > p_m) or (t_y == p_y and t_m == p_m and t_d > p_d):
            answer.append(i+1)
        

    return answer


print(solution("2022.05.19"	,["A 6", "B 100", "C 3"], ["2021.05.02 A", "2021.07.01 B", "2022.02.19 C", "2022.02.20 C","2022.2.20 C"]))