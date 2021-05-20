def SelectionSort(A):
    n = len(A)

    for idx in range(n-1):
        min = idx
        for jdx in range(idx+1, n):
            if A[jdx] < A[min]:
                min = jdx

        temp = A[idx]
        A[idx] = A[min]
        A[min] = temp

    return A

if __name__ == '__main__':
    A = [5, 8, 1, 2, 0, 6, 9, 3, 7, 4]
    print(SelectionSort(A))