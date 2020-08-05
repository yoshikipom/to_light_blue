# https://atcoder.jp/contests/joi2008ho/tasks/joi2008ho_a

import sys

read = sys.stdin.read
readline = sys.stdin.buffer.readline
sys.setrecursionlimit(10 ** 8)
INF = float('inf')

N = int(input())
stone = []
color = 0

# 1つ目
c = int(input())
stone.append([c, 1])
prev = c

for i in range(2, N + 1):
    c = int(input())

    if i % 2 == 1:
        # 奇数回目は入れるだけ
        if c == prev:
            stone[-1][1] += 1
        else:
            stone.append([c, 1])
            prev = c

    else:
        # 偶数回目は入れるだけ
        if c == prev:
            stone[-1][1] += 1
        else:
            _, n = stone.pop()
            if len(stone) == 0:
                stone.append([c, n+1])
            else:
                stone[-1][1] += n + 1
            prev = c

ans = 0
for c, n in stone:
    if c == 0:
        ans += n
print(ans)
