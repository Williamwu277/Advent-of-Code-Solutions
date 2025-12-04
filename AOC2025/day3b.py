"""
Day 3B
------
Not sure if there is an easier way than DP.
DP[i][j] = Biggest number with j + 1 digits after considering the i-th index
DP[i][j] = Previous biggest number with j + 1 digits DP[i-1][j] OR using the i-th index
as digit j + 1: DP[i-1][j-1] * 10 + digit[i]
"""

NUM_DIGITS = 12
total = 0

with open("input.in", "r") as f:

    for line in f:

        batteries = line.rstrip()
        sz = len(batteries)

        DP = [[-1] * NUM_DIGITS for _ in range(sz)]

        for i in range(sz):

            v = int(batteries[i])

            for j in range(NUM_DIGITS):

                if j == 0:
                    if i == 0: DP[i][j] = v
                    else: DP[i][j] = max(DP[i-1][j], v)
                else:
                    if i == 0: continue
                    else: DP[i][j] = max(DP[i-1][j], DP[i-1][j-1] * 10 + v)

        total += DP[sz - 1][NUM_DIGITS - 1]

print(total)
