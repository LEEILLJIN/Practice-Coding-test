def solution(n, arr1, arr2):
    answer = []
    for i in range(n):
        temp1 = bin(arr1[i])[2:]
        temp2 = bin(arr2[i])[2:]
        new = appendZero(n, bin(int(temp1) or int(temp2))[2:])
        answer.append(checkMap(n, new))
    return answer

def appendZero(n,a):
    cnt = 0
    cnt = n - len(a)
    result = "0"*cnt + a
    return result
def checkMap(n,a):
    temp = ""
    for i in range(n):
        if a[i] == '0':
            temp += " "
        else :
            temp += "#"
    return temp
            
# def checkMap(n,a,b):
#     temp = ""
#     for i in range(n):
#         if a[i] == '0' and b[i] == '0':
#             temp += " "
#         else :
#             temp += "#"
#     return temp

print(solution(5, [9, 20, 28, 18, 11], [30, 1, 21, 17, 28]))