# 70 50 80 50
import collections
def solution(people, limit):
    answer = 0
    people.sort(reverse=True)
    print(people)
    Dpeople = collections.deque(people)
    flag = 0
    while Dpeople:
        if len(Dpeople) >= 2:
            print(Dpeople)
            if Dpeople[0] + Dpeople[-1] > limit:
                Dpeople.popleft()
                answer += 1
                continue
            for i in range(len(Dpeople)-1, 0,-1):
                if (Dpeople[0] + Dpeople[i]) <= limit:
                    print("DDD",Dpeople[0] , Dpeople[i])
                    del Dpeople[i]
                    Dpeople.popleft()
                    answer += 1
                    flag = 1
                    break
            if flag == 0:
                Dpeople.popleft()
                answer += 1
        else:
            Dpeople.pop()
            answer += 1
    return answer

print(solution([15,15,15,20, 70, 30, 40], 100))
print(solution([20, 30, 30, 40, 70, 80], 100))
print(solution([50,50, 70,80, 40], 100))





# while Dpeople:
#     if len(Dpeople) >= 2:
#         for i in range(len(Dpeople)-2, -1, -1):
#             if (Dpeople[len(Dpeople)-1] + Dpeople[i]) <= limit:
#                 Dpeople.pop()
#                 del Dpeople[i]
#                 answer += 1
#                 flag = 1
#                 break
#         if flag == 0:
#             Dpeople.pop()
#             answer += 1
#     else:
#         Dpeople.pop()
#         answer += 1




    # while Dpeople:
    #     if len(Dpeople) > 2:
    #         if (Dpeople[-1] + Dpeople[0]) <= limit:
    #             print("dd", Dpeople)
    #             for i in range(len(Dpeople)-1):
    #                 if (Dpeople[-1] + Dpeople[i]) > limit:
    #                     if (Dpeople[-1] + Dpeople[i-1]) <= limit :
    #                         Dpeople.pop()
    #                         del Dpeople[i-1]
    #                         answer += 1
    #                         flag = 1
    #                         break
    #                 else:
    #                     Dpeople.pop()
    #                     Dpeople.pop()
    #                     answer += 1
    #                     flag = 1
    #                     break
    #         else:
    #             Dpeople.pop()
    #             answer += 1
    #             continue
    #         if flag == 0:
    #             Dpeople.pop()
    #             answer += 1
    #         flag = 0
    #     elif len(Dpeople) == 2:
    #         print(Dpeople)
    #         print("SS")
    #         if sum(Dpeople) <= limit:
    #             Dpeople.pop()
    #             Dpeople.pop()
    #             answer += 1
    #         else:
    #             Dpeople.pop()
    #             Dpeople.pop()
    #             answer += 2
    #     else:
    #         Dpeople.pop()
    #         answer += 1
