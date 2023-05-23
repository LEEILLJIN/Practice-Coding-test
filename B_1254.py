#abab
#한번에 펠린드롬이 되거나 이전 문자와 같거나.
#qwertytrewq

s=input()

for i in range(len(s)):
    if s[i:]==s[i:][::-1]:
        print(i)
        print(s[i:])
        print(s[i:][::-1])
        print(len(s)+i)
        break