def merge(left, right):
    result = []
    while left or right:
        if left and right :
            if left[0] < right[0]:
                result.append(left.pop(0))
            else :
                result.append(right.pop(0))

        else :
            if left :
                result.append(left.pop(0))
            else :
                result.append(right.pop(0))

    return result

def mergeSort(alist):
    if len(alist) <= 1:
        return alist
    k = len(alist)//2
    left = mergeSort(alist[:k])
    right = mergeSort(alist[k:])
    return merge(left, right)

alist = [4,26,9,3,1,72,566,43]
blist = mergeSort(alist)
print(blist)