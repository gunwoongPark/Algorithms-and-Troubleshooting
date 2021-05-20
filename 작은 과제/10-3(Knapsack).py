def Knapsack(C, w, v, K):
    n = len(w)

    for idx in range(1, n+1):
        for weight in range(1, C+1):
            if(w[idx-1] > weight):
                K[idx][weight] = K[idx-1][weight]
            else :
                K[idx][weight] = max(K[idx-1][weight], (K[idx-1][weight-w[idx-1]] + v[idx-1]))

    return K[n][C]

if __name__ == '__main__':
    w = [5, 4, 6, 3]
    v = [10, 40, 30, 50]
    C = 10
    K = [[0 for col in range(C+1)] for row in range(len(w)+1)]

    print(Knapsack(C, w, v, K))