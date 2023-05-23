s = str(input())
result = set()
for i in range(1, len(s)+1):
    for j in range(len(s)):
        if j+i <= len(s):
            print(s[j:j+i])
            result.add(s[j:j+i])
        else:
            break
print(len(result))