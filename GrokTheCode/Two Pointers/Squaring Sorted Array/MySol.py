class Solution:
  def makeSquares(self, arr):
    squares = []
    for x in arr:
      squares.append(x ** 2)
    return sorted(squares)
