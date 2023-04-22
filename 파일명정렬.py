def solution(files):
    newfiles = []
    newfile = []
    Head = ""
    Number = ""
    Tail = ""
    for i in files:
        temp = list(i)
        for j in range(len(temp)):
            if temp[j].isdigit():
                Head = "".join(temp[:j])
                newfile.append(Head)
                if j < len(temp)-1:
                    for k in range(j, j+5):
                        if k < len(temp):
                            if temp[k].isdigit:
                                Number += temp[k]
                            else:
                                Tail = k
                                break
                        else:
                            Tail = k
                            break
                else:
                    Number += temp[j:]
                    Tail = j+1
                newfile.append(Number)
                Number = ""
                if int(Tail) < len(temp):
                    Tail = "".join(temp[Tail:])
                    newfile.append(Tail)
                    Tail = ""
                
                newfiles.append(newfile)
                newfile = []
                break     
    newfiles.sort(key=lambda x:(x[0].lower(), int(x[1])))
                
    for i in range(len(newfiles)):
        newfiles[i] = "".join(newfiles[i])
    
    return newfiles

print(solution(["img000012345", "img1.png","img2","IMG02"]))
print(solution(["foo010bar020.zip"]))
# print(solution( ["O00321", "O49qcGPHuRLR5FEfoO00321"]))