class Solution:
  def findSubarrays(self, arr, target):
    result = []
    curSubarray = []
    iMax = len(arr) - 1
    innerI = 0
    curSum = 0

    for i, x in enumerate(arr):
      curSubarray.append(x)
      curSum = multiplyArr(self, curSubarray)
      innerI = i
      while curSum < target:
        result.append(list(curSubarray))
        if innerI < iMax:
          curSubarray.append(arr[innerI + 1])
          curSum = multiplyArr(self, curSubarray)
          innerI += 1
        else:
          curSum = target + 1
      
      curSubarray = []
      curSum = 0
    
    return result

def multiplyArr(self, arr):
  # Multiply elements one by one
  result = 1
  for x in arr:
    result = result * x
  return result