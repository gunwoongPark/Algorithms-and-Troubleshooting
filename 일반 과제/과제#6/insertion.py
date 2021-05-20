def InsertionSort(A):
    n = len(A)
    for idx in range(1, n):
        cur_el = A[idx]

        jdx = idx-1
        while jdx >= 0 and A[jdx] > cur_el:
            A[jdx+1] = A[jdx]
            jdx = jdx-1
        A[jdx+1] = cur_el

    return A

if __name__ == '__main__':
    A = [5, 8, 1, 2, 0, 6, 9, 3, 7, 4]
    print(InsertionSort(A))