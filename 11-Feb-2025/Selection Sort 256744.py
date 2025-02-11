# Problem: Selection Sort - https://practice.geeksforgeeks.org/problems/selection-sort/1

#User function Template for python3

class Solution: 
    def selectionSort(self, arr):
        #code here
        for i in range(len(arr)):
            min_idx = i
            for j in range(i,len(arr)):
                if arr[min_idx] > arr[j]:
                    min_idx = j
            
            arr[i],arr[min_idx] = arr[min_idx],arr[i]
        return arr