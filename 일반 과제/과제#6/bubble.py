import random

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
    A = [random.randint(0, 100) for _ in range(10)]
    print(BubbleSort(A))