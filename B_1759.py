# a b c d e f g h i j k l m n o p q r s t u v w x y z
from itertools import combinations

l,c = map(int, input().split())
alphabet = list(map(str, input().split()))
alphabet.sort()
answer = []

cnt = 0
vowel = ["a", "e", "i", "o", "u"]
for i in combinations(alphabet, l):
    i = sorted(i)
    for j in vowel:
        if j in i:
            cnt += 1
    if cnt > 0 and l-cnt > 1:
        answer.append("".join(i))
    cnt = 0
setanswer = set(answer)
result = list(answer)
result.sort()

for i in result:
    print(i)