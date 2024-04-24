import numpy as np
class Solution:
    def tribonacci(self, n: int) -> int:
        if n == 0:
            return 0
      
        # Base cases: return 1 for the first or second element in the sequence.
        if n < 3:
            return 1
      
        # Define the transition matrix for the Tribonacci sequence.
        # This matrix represents the relationship between successive elements.
        transition_matrix = np.matrix([[1, 1, 0], [1, 0, 1], [1, 0, 0]], np.dtype("O"))
      
        # Initialize the result matrix as the identity matrix aligned with the sequence order.
        result_matrix = np.matrix([[1, 1, 0]], np.dtype("O"))
        n -= 3
      
        # Use the Fast Exponentiation algorithm to raise the matrix to the power of (n-3).
        while n:
            # When the current power is odd, multiply result_matrix with transition_matrix.
            if n & 1:
                result_matrix *= transition_matrix
          
            # Square the transition_matrix to get the next higher power of 2.
            transition_matrix *= transition_matrix
          
            # Shift right to divide n by 2, flooring it.
            n >>= 1
      
        # Return the sum of the elements in the resulting matrix as the answer.
        return result_matrix.sum()