coin = [10, 50, 100, 170, 500]
change = int(input())

d = [10000] * (change + 1)

d[0] = 0

for i in range(len(coin)):
    for j in range(coin[i], change + 1):
        if d[j - coin[i]] != 10000:
            d[j] = min(d[j], d[j-coin[i]]+1)

print(d[change])