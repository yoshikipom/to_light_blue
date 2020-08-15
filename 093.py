# https://atcoder.jp/contests/s8pc-3/tasks/s8pc_3_b
# WA 2ケース

import copy


def delete(M, k):
    point = 0
    for row in M:
        for l in range(len(row)-1):
            for r in range(l + 1, len(row)):
                if row[l] != row[r]:
                    break
            if r - l >= k:
                point += (r - l) * row[l]
                for i in range(l, r):
                    row[i] = 0
                break

    return point


def drop(M):
    for c in range(len(M[0])):
        nums = []
        for i in range(len(M)-1, -1, -1):
            if M[i][c] != 0:
                nums.append(M[i][c])
            M[i][c] = 0

        for i in range(len(nums)):
            M[len(M)-1-i][c] = nums[i]


def solve(M, k):
    result = 0
    drop(M)
    # for row in M:
    #     print(*row)
    itr = 0
    while True:
        point = delete(M, k)
        if point == 0:
            break
        result += point * (2 ** itr)
        # print('-------')
        # for row in M:
        #     print(*row)
        # print('--drop-----')
        drop(M)
        # for row in M:
        #     print(*row)
        # print('-------')
        # print(result)
        itr += 1
    return result


if __name__ == "__main__":
    h, w, k = list(map(int, input().split()))
    M2 = []
    for _ in range(h):
        row_input = input()
        row = []
        for c in row_input:
            row.append(int(c))
        row.append(0)
        M2.append(row)

    result = 0
    for i in range(h):
        for j in range(w):
            M = copy.deepcopy(M2)
            M[i][j] = 0
            result = max(result, solve(M, k))

    print(result)
