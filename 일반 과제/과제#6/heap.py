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
        current_value = heap[current]
        left_child = 2 * current
        right_child = 2 * current + 1

        # 더 이상 자식노드가 없을 경우
        if left_child > heap_size:
            return
        # 왼쪽 자식 노드만 있는 케이스
        elif right_child > heap_size:
            child_value, selected = heap[left_child], left_child
            if current_value >= child_value:
                return
        # 자식이 두 개 다 있는 케이스
        else:
            child_value, selected = max((heap[right_child], right_child), (heap[left_child], left_child))
            if current >= child_value:
                return
        heap[current], heap[selected] = child_value, current_value
        current = selected

def max_heap(heap, heap_size):
    while heap_size > 1:
        heap[1], heap[heap_size] = heap[heap_size], heap[1]
        heap_size -= 1
        down_heap(heap, heap_size)

if __name__ == '__main__':
    import random
    nums = [random.randint(0, 100) for _ in range(10)]
    # nums = [4,2,7,6,9,3,5]
    heap = [None]

    for num in nums:
        insert_num(num, heap)
    heap_size = len(heap) - 1

    max_heap(heap, heap_size)

    print(heap)

