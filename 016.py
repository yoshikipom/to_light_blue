# https://atcoder.jp/contests/abc150/tasks/abc150_c

import itertools

if __name__ == "__main__":
    N = int(input())
    P = tuple(map(int, input().split()))
    Q = tuple(map(int, input().split()))

    A = [i for i in range(1, N+1)]
    S = set()
    a = 0
    b = 0
    for i, permutated in enumerate(itertools.permutations(A)):
        if permutated == P:
            a = i
        if permutated == Q:
            b = i

    print(abs(a-b))
