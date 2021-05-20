import random

def ShellSort(A):
    n = len(A)
    gap = []
    while n > 1:
        if (n//2) % 2 == 0:
            gap.append((n//2)+1)
            n = n//2 + 1
        else:
            gap.append(n//2)
            n = n//2
    n = len(A)

    for h in gap:
        for idx in range(h, n):
            cur_el = A[idx]
            jdx = idx
            while jdx >= h and A[jdx-h] > cur_el:
                A[jdx] = A[jdx-h]
                jdx = jdx-h
            A[jdx] = cur_el

    return A


if __name__ == '__main__':
    A = [random.randint(0, 100) for _ in range(10)]
    print(ShellSort(A))