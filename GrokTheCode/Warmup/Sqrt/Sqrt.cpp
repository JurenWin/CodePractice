#include <iostream>

class Solution {
public:
  int mySqrt(int x) {
    if (x < 2) return x; // return x if x is less than 2, since the square root of x = 0 or 1 is x itself.

    int left = 2, right = x / 2; // initialize the left and right pointers, which are used to determine the range of possible square roots.
    int pivot;
    long num; // use long to store result of pivot * pivot to prevent overflow.
    while (left <= right) { // binary search for the square root.
      pivot = left + (right - left) / 2; // find the middle element of the current range.
      num = (long) pivot * pivot;
      if (num > x)
        right = pivot - 1; // if pivot * pivot is greater than x, set right to pivot - 1.
      else if (num < x)
        left = pivot + 1; // if pivot * pivot is less than x, set left to pivot + 1.
      else
        return pivot; // if pivot * pivot is equal to x, return pivot.
    }

    return right; // return right after the loop.
  }
};


int main() {
  Solution solution;

  int input1 = 4;
  int expectedOutput1 = 2;
  int result1 = solution.mySqrt(input1);
  std::cout << (result1 == expectedOutput1) << std::endl; // Expected output: 1

  int input2 = 8;
  int expectedOutput2 = 2;
  int result2 = solution.mySqrt(input2);
  std::cout << (result2 == expectedOutput2) << std::endl; // Expected output: 1

  int input4 = 2;
  int expectedOutput4 = 1;
  int result4 = solution.mySqrt(input4);
  std::cout << (result4 == expectedOutput4) << std::endl; // Expected output: 1

  int input5 = 3;
  int expectedOutput5 = 1;
  int result5 = solution.mySqrt(input5);
  std::cout << (result5 == expectedOutput5) << std::endl; // Expected output: 1

  int input6 = 15;
  int expectedOutput6 = 3;
  int result6 = solution.mySqrt(input6);
  std::cout << (result6 == expectedOutput6) << std::endl; // Expected output: 1

  return 0;
}
