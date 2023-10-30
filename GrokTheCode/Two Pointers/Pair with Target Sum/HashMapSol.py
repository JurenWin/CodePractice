class Solution:
  def pair_with_targetsum(self, arr, target_sum):
    nums = {}  # to store numbers and their indices
    for i, num in enumerate(arr):
      if target_sum - num in nums:
       return [nums[target_sum - num], i]
      else:
       nums[num] = i
    return [-1, -1]


def main():
  sol = Solution()
  print(sol.pair_with_targetsum([1, 2, 3, 4, 6], 6))
  print(sol.pair_with_targetsum([2, 5, 9, 11], 11))


main()