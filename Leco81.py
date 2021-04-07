#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/4/7 11:27 上午
# @Author  : MaJiong
# @File    : Leco81.py
# @Software: PyCharm
from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        if target < nums[0]:
            for i in range(len(nums) - 1, -1, -1):
                if target == nums[i]:
                    return True
                if target > nums[i]:
                    return False
        else:
            for i in range(len(nums)):
                if target == nums[i]:
                    return True
                if target < nums[i]:
                    return False
        return False


s = Solution()
print(s.search(nums=[2, 5, 6, 0, 0, 1, 2], target=3))
