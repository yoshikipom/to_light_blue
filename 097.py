# https://atcoder.jp/contests/abc150/tasks/abc150_d
import math


def lcm(x, y):
    return (x * y) // math.gcd(x, y)


n, m = list(map(int, input().split()))
A = list(map(int, input().split()))
for i in range(len(A)):
    A[i] //= 2

div_two_cnt = None
for a in A:
    cnt = 0
    while a % 2 == 0:
        a //= 2
        cnt += 1
    if div_two_cnt is None:
        div_two_cnt = cnt
    elif cnt != div_two_cnt:
        print(0)
        exit()

tmp = A[0]
for i in range(1, n):
    tmp = lcm(tmp, A[i])

# print(tmp)
print(((m // tmp) + 1)//2)
