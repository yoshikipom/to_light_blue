# https://atcoder.jp/contests/abc138/tasks/abc138_d

if __name__ == "__main__":
    N, K = map(int, input().split())
    G = [[] for _ in range(N)]
    for n in range(N-1):
        a, b = map(int, input().split())
        G[a - 1].append(b - 1)
        G[b - 1].append(a - 1)

    C = [0] * N

    for k in range(K):
        p, x = map(int, input().split())
        C[p - 1] += x

    V = [False]*N
    stack = [0]
    while stack:
        x = stack.pop()
        V[x] = True
        for y in G[x]:
            if V[y]:
                continue

            C[y] += C[x]
            stack.append(y)

    print(*C)
