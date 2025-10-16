# Problem Link: https://www.designgurus.io/course-play/grokking-the-coding-interview/doc/smallest-subarray-with-a-greater-sum-easy

import math
from typing import List

class Solution:
  def findMinSubArray(self, s: int, arr: List[int]):
    min_sub_array_len = math.inf
    window_start = 0
    window_sum = 0

    for window_end in range(len(arr)):
       window_sum += arr[window_end]
       while(window_sum >= s):
          min_sub_array_len =  min(min_sub_array_len, (window_end - window_start + 1))
          window_sum -= arr[window_start]
          window_start += 1
    
    return min_sub_array_len if (min_sub_array_len < math.inf) else 0


if __name__ == "__main__":
    sol = Solution()

    # Example 1:
    # Input: arr = [2, 1, 5, 2, 3, 2], S=7
    # Output: 2
    # Explanation: The smallest subarray with a sum greater than or equal to '7' is [5, 2].
    assert sol.findMinSubArray(7, [2, 1, 5, 2, 3, 2]) == 2
    # Example 2:

    # Input: arr = [2, 1, 5, 2, 8], S=7
    # Output: 1 
    # Explanation: The smallest subarray with a sum greater than or equal to '7' is [8].
    assert sol.findMinSubArray(7, [2, 1, 5, 2, 8]) == 1
    # Example 3:

    # Input: arr = [3, 4, 1, 1, 6], S=8
    # Output: 3
    # Explanation: Smallest subarrays with a sum greater than or equal to '8' are [3, 4, 1] or [1, 1, 6].
    assert sol.findMinSubArray(8, [3, 4, 1, 1, 6]) == 3

    # Input: arr = [1, 1, 1, 1], S=8
    # Output: 0
    assert sol.findMinSubArray(8, [1, 1, 1, 1]) == 0