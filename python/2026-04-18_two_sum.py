from typing import List


def two_sum(nums: List[int], target: int) -> List[int]:
    seen = {}
    for index, value in enumerate(nums):
        complement = target - value
        if complement in seen:
            return [seen[complement], index]
        seen[value] = index
    return []


def twoSum(nums: List[int], target: int) -> List[int]:
    return two_sum(nums, target)


if __name__ == "__main__":
    assert two_sum([2, 7, 11, 15], 9) == [0, 1]
    assert two_sum([3, 2, 4], 6) == [1, 2]
    assert two_sum([3, 3], 6) == [0, 1]
    assert twoSum([2, 7, 11, 15], 9) == [0, 1]
    print("All sample checks passed.")
