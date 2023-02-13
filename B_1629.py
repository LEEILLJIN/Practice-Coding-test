A, B, C = map(int, input().split())
def power(n, k):
    result = 1

    while k > 0:
        if k % 2:
            result *= n
        n *= n
        k //= 2
    return result
print(power(A, B))
print(power(A,B)%C)
# https://hbj0209.tistory.com/43