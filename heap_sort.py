def heap_print(heap):
    print("HEAP: ")
    limit = len(heap)
    idx = 0
    while idx < limit:
        print(f"{heap[idx]}:", end="")
        if 2*idx+1 < limit:
            print(f"L{heap[2*idx+1]}", end="")
        if 2*idx+2 < limit:
            print(f",R{heap[2*idx+2]}", end="")

        print()
        idx+=1

def __heapify(heap,i,limit=-1):
    idx = i
    size = len(heap)-1 if limit == -1 else limit
    # Heapify limit
    while idx < size:
        smallest_index = idx
        
        if (2 * idx + 1 <= size) and (heap[2*idx+1] < heap[idx]):
            smallest_index = 2*idx+1
        if (2 * idx + 2 <= size) and (heap[2*idx+2] < heap[idx] and heap[2*idx+2] < heap[2*idx+1]):
            smallest_index = 2 * idx + 2 
        
        if smallest_index != idx:
            heap[smallest_index], heap[idx] = heap[idx], heap[smallest_index]
            idx = smallest_index
        else:
            break

    # In heap removal is always from top (root) so we do not require element to be specified
def remove(arr, limit):
    # Index of root
    idx = 0
    size = limit


    # Swap the root with last element and decrement the size by 1
    arr[idx], arr[limit] = arr[limit], arr[idx]
    size -= 1

    # Call the arrify method to recreate the arr
    if size >= 0:
        __heapify(arr, 0, size)

def heap_sort(heap):
    pass

arr = input("Enter the Array like (1 2 3): ")
heap = [2, 6, 8, 5, 4, 3] if len(arr.split())==0 else list(map(int, arr.split()))
for i in range(len(heap)-1,-1,-1):
    __heapify(heap, i)

print(f"Entered Array: {heap}")

for i in range(len(heap)):
    remove(heap, len(heap)-i-1)
    # print(f"Sorting {i}")
    # print(heap)

print(f"Sorted array: {heap}")