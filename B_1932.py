n = int(input())
dp = []
inttri = []
for i in range(n):
    temp = list(map(int, input().split(" ")))
    inttri.append(temp)

def checkmax(inttri, n):
    if n == 1:
        return inttri[0][0]
    else :
        inttri[1][0] = inttri[0][0] + inttri[1][0]
        inttri[1][1] = inttri[0][0] + inttri[1][1]
        if n == 2:
            return max(inttri[1])
        else :
            for i in range(2, n):
                for j in range(len(inttri[i])):
                    if j == 0:
                        inttri[i][j] = inttri[i-1][j] + inttri[i][j]
                    elif j == len(inttri[i])-1:
                        inttri[i][j] = inttri[i-1][len(inttri[i-1])-1] + inttri[i][j]
                    else:
                        inttri[i][j] = max(inttri[i-1][j-1],inttri[i-1][j]) + inttri[i][j]
            return max(inttri[n-1])
result = checkmax(inttri,n)
print(result)