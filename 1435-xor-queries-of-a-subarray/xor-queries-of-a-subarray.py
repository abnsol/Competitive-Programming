class Solution:
    def xorQueries(self, arr, queries):
        result = []

        # Step 1: Convert arr into an in-place prefix XOR array
        for i in range(1, len(arr)):
            arr[i] ^= arr[i - 1]

        # Step 2: Resolve each query using the prefix XOR array
        for left, right in queries:
            if left > 0:
                result.append(arr[left - 1] ^ arr[right])
            else:
                result.append(arr[right])

        return result