def DPCoinChange(n, d, C):
    k = len(d)

    for jdx in range(n+1):
        for idx in range(k):
            if d[idx] <= jdx and C[jdx - d[idx]] +1 < C[jdx]:
                C[jdx] = C[jdx - d[idx]] + 1

    return C[n]

if __name__ == '__main__':
    n = 31
    d = [16, 10, 5, 1]
    C = []
    for idx in range(n+1):
        if idx == 0:
            C.append(0)
        else :
            C.append(987654321)

    print(DPCoinChange(n, d, C))