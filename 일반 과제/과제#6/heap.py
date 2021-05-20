def insert_num(num, heap):
    heap.append(num)
    idx = len(heap)-1
    while idx > 1:
        if heap[idx] > heap[idx//2]:
            heap[idx], heap[idx//2] = heap[idx//2], heap[idx]
            idx = idx//2
        else:
            break

def down_heap(heap, heap_size):
    idx = 1
    while True:
        # 더 이상 자식노드가 없거나, 한 쪽만 존재할 경우
        if 2*idx > heap_size or 2*idx+1 > heap_size:
            break

        if heap[2*idx] > heap[2*idx+1]:
            if heap[idx] < heap[2*idx]:
                heap[idx], heap[2*idx] = heap[2*idx], heap[idx]
                idx *= 2
            # 본인이 더 클 경우
            else:
                break

        else:
            if heap[idx] < heap[2*idx+1]:
                heap[idx], heap[2*idx+1] = heap[2*idx+1], heap[idx]
                idx = 2*idx+1
            # 본인이 더 클 경우
            else:
                break

def max_heap(heap, heap_size):
    while heap_size > 1:
        heap[1], heap[heap_size] = heap[heap_size], heap[1]
        heap_size -= 1
        down_heap(heap, heap_size)

if __name__ == '__main__':
    nums = [4, 2, 7, 6, 9, 3, 5, 1, 8]
    heap = [None]

    for num in nums:
        insert_num(num, heap)
    heap_size = len(heap) - 1

    max_heap(heap, heap_size)

    print(heap)

