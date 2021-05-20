def BubbleSort(A):
    n = len(A)
    for Pass in range(n-1):
        for idx in range(1, n-Pass):
            if(A[idx-1] > A[idx]):
                temp = A[idx-1]
                A[idx-1] = A[idx]
                A[idx] = temp

    return A


if __name__ == '__main__':
    A = [5, 8, 1, 2, 0, 6, 9, 3, 7, 4]
    print(BubbleSort(A))