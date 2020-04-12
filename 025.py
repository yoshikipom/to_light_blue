# https://onlinejudge.u-aizu.ac.jp/problems/1160

A = []
w = 0
h = 0


def walk(i, j):
    global A
    stack = [(i, j)]
    while True:
        i, j = stack.pop()
        A[i][j] = 0
        for ii in range(i-1, i+2):
            for jj in range(j-1, j+2):
                if ii < 0 or h <= ii:
                    continue
                if jj < 0 or w <= jj:
                    continue
                if A[ii][jj] == 0:
                    continue
                else:
                    stack.append((ii, jj))

        if len(stack) == 0:
            break


if __name__ == "__main__":
    while True:
        w, h = map(int, input().split())
        if w == 0 and h == 0:
            break

        A = []
        for i in range(h):
            row = list(map(int, input().split()))
            A.append(row)

        cnt = 0
        for i in range(h):
            for j in range(w):
                if A[i][j] == 1:
                    cnt += 1
                    walk(i, j)

        print(cnt)
