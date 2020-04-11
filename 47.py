# https://onlinejudge.u-aizu.ac.jp/problems/ALDS1_10_B
import functools

INF = float('inf')
@functools.lru_cache(maxsize=None)
def rec(l, r):
    if l + 1 == r:
        return 0
    ret = INF
    for mid in range(l+1, r):
        ret = min(ret, rec(l, mid) + rec(mid, r)+R[l]*R[mid]*C[r-1])
    return ret


if __name__ == "__main__":
    N = int(input())
    R = []
    C = []
    for _ in range(N):
        r, c = list(map(int, input().split()))
        R.append(r)
        C.append(c)

    print(rec(0, N))
