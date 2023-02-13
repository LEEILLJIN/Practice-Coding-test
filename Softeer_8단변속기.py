#10분걸림

import sys

numList = list(map(int,input().split(" ")))

def check(numList):
    if 1 < numList[0] < 8:
        print("mixed")
        return
    elif numList[0] == 1:
        pre= 1
        for i in range(1, len(numList)):
            if numList[i] - pre == 1:
                pre =  numList[i]
                continue
            else :
                print("mixed")
                return
        print("ascending")
        return
    elif numList[0] == 8:
        pre= 8
        for i in range(1, len(numList)):
            if pre - numList[i] == 1:
                pre =  numList[i]
                continue
            else :
                print("mixed")
                return
        print("descending")
        return
    
check(numList)