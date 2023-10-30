class Solution:
  def search(self, arr, target_sum):
    if target_sum == 0:
      return [-1, -1]
    i = 0
    j = len(arr) - 1

    while (arr[i] + arr[j]) != target_sum:
      if (arr[i] + arr[j]) > target_sum:
        j -= 1
      elif (arr[i] + arr[j]) < target_sum:
        i += 1
    
    if i == j:
      return [-1, -1]

    return [i, j]
