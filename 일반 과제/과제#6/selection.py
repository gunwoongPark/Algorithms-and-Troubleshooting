import random

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
    A = [random.randint(0, 100) for _ in range(10)]
    print(SelectionSort(A))