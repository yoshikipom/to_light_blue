# https://atcoder.jp/contests/joi2015ho/tasks/joi2015ho_b
# TLE
import functools
import sys

sys.setrecursionlimit(3000)


@functools.lru_cache(maxsize=None)
def rec(l, r):
    global ans

    if abs(l-r) == N+1:
        return 0

    if (r - l) % 2 == 0:
        # IOI
        if A[l % N] > A[r % N]:
            return rec(l-1, r)
        else:
            return rec(l, r+1)
    else:
        # JOI
        ret_left = rec(l-1, r) + A[l % N]
        ret_right = rec(l, r+1) + A[r % N]
        ret = max(ret_left, ret_right)
        ans = max(ans, ret)
        return ret


if __name__ == "__main__":
    N = int(input())
    A = [int(input()) for _ in range(N)]

    ans = -1
    results = []
    for start in range(0, N, 2):
        rec(start, start+1)

    print(ans)
