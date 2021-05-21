import random

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
    current = 1
    while True:
        left_child = 2 * current
        right_child = 2 * current + 1

        # 더 이상 자식노드가 없을 경우
        if left_child > heap_size:
            return
        # 왼쪽 자식 노드만 있는 케이스
        elif right_child > heap_size:
            if heap[current] >= heap[left_child]:
                return
            heap[current], heap[left_child] = heap[left_child], heap[current]
            current = left_child

        # 자식이 두 개 다 있는 케이스
        else:
            if heap[left_child] < heap[right_child]:
                if heap[current] >= heap[right_child]:
                    return
                heap[current], heap[right_child] = heap[right_child], heap[current]
                current = right_child

            else:
                if heap[current] >= heap[left_child]:
                    return
                heap[current], heap[left_child] = heap[left_child], heap[current]
                current = left_child

def max_heap(heap, heap_size):
    while heap_size > 1:
        heap[1], heap[heap_size] = heap[heap_size], heap[1]
        heap_size -= 1
        down_heap(heap, heap_size)

if __name__ == '__main__':
    random.seed(0)
    nums = [random.randint(0, 100001) for _ in range(2000)]
    heap = [None]

    for num in nums:
        insert_num(num, heap)
    heap_size = len(heap) - 1

    max_heap(heap, heap_size)

    print(heap)

    is_sorted = all(heap[i] <= heap[i+1] for i in range(1, len(heap)-1))
    print('CHECK :', is_sorted)

