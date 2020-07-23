# https://onlinejudge.u-aizu.ac.jp/problems/NTL_1_A
n = int(input())
num = n

fct = []
cur = 2
while cur * cur <= n:
    while n % cur == 0:
        n //= cur
        fct.append(cur)
    cur += 1
if n > 1:
    fct.append(n)

print(str(num) + ": " + ' '.join(str(f) for f in fct))
