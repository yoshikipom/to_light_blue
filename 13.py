# https://atcoder.jp/contests/joi2008yo/tasks/joi2008yo_e

import copy


def flip_row(B, row, C):
    for j in range(C):
        B[row][j] = B[row][j] ^ 1


def flip_column_if_needed(B, colmun, R):
    cnt_front = 0
    cnt_back = 0
    for i in range(R):
        if B[i][colmun] == 1:
            cnt_front += 1
        else:
            cnt_back += 1

    if cnt_front > cnt_back:
        for i in range(R):
            B[i][colmun] = B[i][colmun] ^ 1


if __name__ == "__main__":
    R, C = map(int, input().split())
    A = []
    for _ in range(R):
        row = tuple(map(int, input().split()))
        A.append(row)

    result = 0
    for bit in range(1 << R):
        B = [[A[i][j] for j in range(C)] for i in range(R)]
        for i in range(R):
            if bit & (1 << i):
                flip_row(B, i, C)

        # print('--------------------')
        # print(B)
        for j in range(C):
            flip_column_if_needed(B, j, R)

        cnt = R * C - sum(map(sum, B))

        # print(bin(bit))
        # print(B)
        # print(cnt)
        # print('--------------------')
        result = max(result, cnt)

    print(result)
