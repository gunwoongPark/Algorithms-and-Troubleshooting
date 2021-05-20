def DPCoinChange(n, d, C, C2):
    k = len(d)

    for jdx in range(n+1):
        for idx in range(k):
            if d[idx] <= jdx and C[jdx - d[idx]] +1 < C[jdx]:
                C[jdx] = C[jdx - d[idx]] + 1
                temp = []
                for kdx in range(k):
                    temp.append(C2[jdx - d[idx]][kdx] + C2[jdx-(jdx-d[idx])][kdx])
                C2[jdx] = temp

    return C2[n]

if __name__ == '__main__':
    n = 25
    d = [16, 10, 5, 1]
    C = []
    C2 = []
    for idx in range(n+1):
        if idx == 0:
            C.append(0)
        else:
            C.append(987654321)
    for idx in range(n+1):
        if idx in d:
            newArr = []
            index = d.index(idx)
            for jdx in range(len(d)):
                if jdx == index:
                    newArr.append(1)
                else:
                    newArr.append(0)
            C2.append(newArr)
        else:
            C2.append([0,0,0,0])
    result_list = DPCoinChange(n, d, C, C2)
    for coin, nums in zip(d, result_list):
        print("{}원 : {}개".format(coin, nums))