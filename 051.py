# https://atcoder.jp/contests/joi2014yo/tasks/joi2014yo_d

N = int(input())
S = input()

# dp[day][person having key]
dp = [[0 for i in range(1 << 3)] for _ in range(N+1)]
dp[0][1] = 1
JOI = ['J', 'O', 'I']

for day in range(N):
    for bit in range(1 << 3):

        for next_bit in range(1 << 3):

            ok = True
            for i, name in enumerate(JOI):
                # 当番がいないとダメ
                if name == S[day] and ~(next_bit >> i) & 1:
                    ok = False
                # 前日にいた人が誰かいないと鍵を引き継げない
                if bit & next_bit == 0:
                    ok = False

            if ok and dp[day][bit] != 0:
                # print(bin(bit), bin(next_bit))
                dp[day+1][next_bit] = (dp[day+1]
                                       [next_bit] + dp[day][bit]) % 10007

print(sum(dp[N]) % 10007)
