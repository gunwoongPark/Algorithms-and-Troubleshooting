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
    print(radix_sort([9, 89, 70, 35, 131, 910, 1]))