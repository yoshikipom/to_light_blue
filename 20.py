# https://atcoder.jp/contests/abc077/tasks/arc084_a

import bisect

if __name__ == "__main__":
    N = int(input())
    A = sorted(list(map(int, input().split())))
    B = sorted(list(map(int, input().split())))
    C = sorted(list(map(int, input().split())))
    BB = []
    CC = []

    # print(A)
    # print(B)
    # print(C)
    # print('-------')

    cnt = 0

    for i in range(N):
        b = B[i]
        a_index = bisect.bisect_left(A, b)
        if i == 0:
            BB.append(a_index)
        else:
            BB.append(BB[i-1] + a_index)

    for i in range(N):
        c = C[i]
        b_index = bisect.bisect_left(B, c)
        if b_index == 0:
            CC.append(0)
            continue
        if i == 0:
            CC.append(BB[b_index - 1])
        else:
            CC.append(CC[i-1] + BB[b_index - 1])

    # print(BB)
    # print(CC)

    print(CC[-1])
