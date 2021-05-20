def EditDistance(S, T, E):
    m = len(S)
    n = len(T)

    for idx in range(m+1):
        E[idx][0] = idx
    for jdx in range(n+1):
        E[0][jdx] = jdx
    for idx in range(1, m+1):
        for jdx in range(1, n+1):
            E[idx][jdx] = min(E[idx][jdx-1]+1, E[idx-1][jdx]+1, E[idx-1][jdx-1]+1 if S[idx-1] != T[jdx-1] else E[idx-1][jdx-1])

    return E[m][n]

if __name__ == '__main__':
    S = "string"
    T = "start"
    E = [[0 for col in range(len(T)+1)] for row in range(len(S)+1)]
    print(EditDistance(S, T, E))