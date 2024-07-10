#User function Template for python3

class Solution:
    #Heapify function to maintain heap property.
    def heapify(self, heap, n, i):
        left = 2 * i + 1
        right = 2 * i + 2
        _min = i
        
        if left < n and heap[left] > heap[_min]:
            _min = left
        if right < n and heap[right] > heap[_min]:
            _min = right
        
        if _min != i:
            heap[i], heap[_min] = heap[_min], heap[i]
            self.heapify(heap, n, _min)
    
    # Function to build a Heap from array.
    def buildHeap(self, arr, n):
        for i in range(n // 2 - 1, -1, -1):
            self.heapify(arr, n, i) 
    
    # Function to sort an array using Heap Sort.    
    def HeapSort(self, arr, n):
        self.buildHeap(arr, n)
        
        for i in range(n - 1, 0, -1):
            arr[0], arr[i] = arr[i], arr[0]
            self.heapify(arr, i, 0)
            
        return arr
            


