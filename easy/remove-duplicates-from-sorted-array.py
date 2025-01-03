from typing import List


def removeDuplicates(nums: List[int]) -> int:
    if not nums:
        return 0

    slow = 0
    for fast in range(1, len(nums)):
        if nums[slow] != nums[fast]:
            slow += 1
            nums[slow] = nums[fast]

    return slow + 1

print(removeDuplicates([1, 2, 1]))  # [1, 2]
print(removeDuplicates([0, 0, 1, 1, 1, 2, 2, 3, 3, 4]))  # [0, 1, 2, 3, 4]