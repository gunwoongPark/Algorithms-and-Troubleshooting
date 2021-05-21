import random

def getrdx(l, modulus):
    maxi = 0
    for val in l:
        digit = 0
        while val > 0:
            digit += 1
            val //= modulus
        if (digit > maxi):
            maxi = digit
    return(maxi)

def radix_sort(l):
    radix, modulus, div = 10, 10, 1
    nordx = getrdx(l, modulus)
    for i in range(nordx):
        buckets = [[] for i in range(radix)]
        for value in l:
            buckets[(value % modulus) // div].append(value)
        modulus, div = modulus * 10, div * 10
        l = []
        for x in buckets:
            l.extend(x)
    return(l)

if __name__ == '__main__':
    A = [random.randint(0, 100001) for _ in range(2000)]
    A = radix_sort(A)
    print(A)

    is_sorted = all(A[i] <= A[i+1] for i in range(len(A)-1))
    print('CHECK :', is_sorted)