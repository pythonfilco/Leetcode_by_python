# coding: utf-8

'''
Write a function that takes an unsigned
integer and returns the number of ’1' bits
it has (also known as the Hamming weight).

For example, the 32-bit integer ’11' has
binary representation 00000000000000000000000000001011,
so the function should return 3.

Credits:
Special thanks to @ts for adding this problem
and creating all test cases.

Subscribe to see which companies asked this question
'''


class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 0:
            return 0
        count = 1
        while n & (n - 1) != 0:
            n &= n - 1
            count += 1
        return count

solution = Solution()
print solution.hammingWeight(3)