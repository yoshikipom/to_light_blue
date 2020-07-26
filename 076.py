# https://atcoder.jp/contests/nikkei2019-final/tasks/nikkei2019_final_a
import itertools
N = int(input())
A = list(map(int, input().split()))

B = [0] + list(itertools.accumulate(A))
# print(B)

for w in range(1, N+1):
    result = 0
    for left in range(0, N - w + 1):
        result = max(result, B[left+w] - B[left])
    print(result)
