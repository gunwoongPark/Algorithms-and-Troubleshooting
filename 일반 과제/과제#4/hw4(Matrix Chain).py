def MatrixChain(matrix, C):

    d = [idx[0] for idx in matrix]
    d.append(matrix[-1][1])

    n = len(d)

    for L in range(1, n-1):
        for idx in range(1, n-L):
            jdx = idx + L
            C[idx][jdx] = 987654321
            for kdx in range(idx, jdx):
                temp = C[idx][kdx] + C[kdx+1][jdx] + (d[idx-1] * d[kdx] * d[jdx])
                if temp < C[idx][jdx]:
                    C[idx][jdx] = temp

    return C[1][n-1]

if __name__ == '__main__':
    matrix = [[10, 20], [20, 5], [5, 15], [15, 30]]
    C = [[0 for col in range(len(matrix) + 1)] for row in range(len(matrix)+1)]
    print(MatrixChain(matrix, C))