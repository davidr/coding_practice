#!/usr/bin/env python3


class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        for i, a in enumerate(nums):
            needed_num = target - a
            # only do a nested loop if we know the solution is in there
            if needed_num in nums[i+1:]:
                for j, b in enumerate(nums[i+1:]):
                    if b == needed_num:
                        return [i, (i+j+1)]

    def twoSumTooSlow(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        for i, a in enumerate(nums):
            try:
                for j, b in enumerate(nums[i+1:]):
                    if a + b == target:
                        # the index of b in nums is i + j + 1
                        return [i, (j + i + 1)]
            except IndexError:
                # we went all the way through and found nothing
                return []

    def addTwoNumbers(self, l1, l2):
        # If l1 or l2 are None, l1 + l2 is just whichever is not None
        if l1 == None: return l2
        if l2 == None: return l1

        # Construct the number represented by l1

        i1 = 0
        i2 = 0

        endoflists = False

        while l1.next and l2.next:
            numbers[0] += 10**i * l1.val
            l1 = l1.next
            numbers[1] += 10**i * l2.val
            l2 = l2.next
            i += 1
        numbers[0] += 10**i * l1.val
        numbers[1] += 10**i * l2.val








if __name__ == "__main__":

    # (2 -> 4 -> 3) + (5 -> 6 -> 4)
    l1 = ListNode(2)
    l1.next = ListNode(4)
    l1.next.next = ListNode(3)

    l2 = ListNode(5)
    l2.next = ListNode(6)
    l2.next.next = ListNode(4)

    a = Solution()
    print(a.addTwoNumbers(l1, l2))
