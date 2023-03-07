The array-form of an integer num is an array representing its digits in left to right order.

For example, for num = 1321, the array form is [1,3,2,1].
Given num, the array-form of an integer, and an integer k, return the array-form of the integer num + k.
class Solution(object):
    def addToArrayForm(self, num, k):
        """
        :type num: List[int]
        :type k: int
        :rtype: List[int]
        """
        count = 0
        is_digits = range(len(num))
        for i in is_digits:
            count *= 10
            count += num[i]
        total = count + k
        return [int(x) for x in str(total)]
