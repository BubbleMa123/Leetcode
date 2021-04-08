# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


# class Solution:
#     def getDecimalValue(self, head: ListNode) -> int:
#         nums = []
#         while head:
#             nums.append(head.val)
#             head = head.next
#         num = 0
#         for i in range(len(nums) - 1, -1, -1):
#             num += nums[i] * 2 ** (len(nums) - 1 - i)
#         return num


class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        num = 0
        while head:
            num = num * 2 + head.val
            head = head.next
        return num
