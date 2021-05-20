import random

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
    A = [random.randint(0, 100) for _ in range(10)]
    print(InsertionSort(A))