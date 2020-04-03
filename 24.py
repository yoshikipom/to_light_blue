# https://onlinejudge.u-aizu.ac.jp/courses/lesson/1/ALDS1/11/ALDS1_11_B

G = {}
d = {}
f = {}
used = set()
t = 1


def dfs(cur):
    global G, d, f, t

    used.add(cur)
    d[cur] = t

    for i in G[cur]:
        if i in used:
            continue
        t += 1
        dfs(i)
    t += 1
    f[cur] = t


if __name__ == "__main__":
    N = int(input())

    for _ in range(N):
        u, k, *V = list(map(int, input().split()))
        G[u] = V

    for i in range(1, N+1):
        if i not in used:
            dfs(i)
            t += 1

    for i in G.keys():
        print(i, d[i], f[i])
