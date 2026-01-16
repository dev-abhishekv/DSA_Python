class Heap:
    def __init__(self, max_size: int) -> None:
        self.heap = [0 for _ in range(max_size)]
        self.size = 0

    def insert(self, val: int) -> None:
        self.size += 1
        # We are taking 1 based indexing
        self.heap[self.size] = val
        
        # Newly inserted element index
        idx = self.size

        # Parent of the new element
        parent = idx//2

        # Assuming the heap to be Max Heap fix the relative positioning of elements
        while parent > 0 and self.heap[parent] < self.heap[idx]:
            self.heap[parent], self.heap[idx] = self.heap[idx], self.heap[parent]
            idx = parent
            parent = idx // 2
        
    def print(self) -> None:
        for i in range(1, self.size + 1):
            print(self.heap[i], end=' ')

    def heap_print(self):
        limit = self.size + 1
        idx = 1
        while idx < limit:
            print(f"{self.heap[idx]}:", end="")
            if 2*idx < limit:
                print(f"L{self.heap[2*idx]}", end="")
            if 2*idx+1 < limit:
                print(f",R{self.heap[2*idx+1]}", end="")

            print()
            idx+=1
    
    def __heapify(self):
        idx = 1
        # Heapify limit
        while idx < self.size:
            greatest_index = idx
            
            if (2 * idx < self.size) and (self.heap[2*idx] > self.heap[idx]):
                greatest_index = 2*idx
            if (2 * idx + 1 < self.size) and (self.heap[2*idx+1] > self.heap[idx] and self.heap[2*idx+1] > self.heap[2*idx]):
                greatest_index = 2 * idx + 1 
            
            if greatest_index != idx:
                self.heap[greatest_index], self.heap[idx] = self.heap[idx], self.heap[greatest_index]
                idx = greatest_index
            else:
                break

    # In heap removal is always from top (root) so we do not require element to be specified
    def remove(self):
        # Index of root
        idx = 1

        # Swap the root with last element and decrement the size by 1
        self.heap[idx], self.heap[self.size] = self.heap[self.size], self.heap[idx]
        self.size -= 1

        # Call the heapify method to recreate the heap
        self.__heapify()
        return self.heap[self.size + 1]

if __name__ == "__main__":
    heap = Heap(10)
    heap.insert(10)
    heap.insert(20)
    heap.insert(30)
    heap.insert(25)
    heap.insert(35)
    print("HEAP:::")
    heap.heap_print()
    heap.insert(100)
    heap.insert(1000)
    print("HEAP:::")
    heap.heap_print()

    print(f"Element Removed: {heap.remove()}")
    print("HEAP:::")
    heap.heap_print()