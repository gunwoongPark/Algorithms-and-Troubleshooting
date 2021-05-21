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
    A = [random.randint(0, 100001) for _ in range(2000)]
    print(InsertionSort(A))

    is_sorted = all(A[i] <= A[i+1] for i in range(len(A)-1))
    print('CHECK :', is_sorted)